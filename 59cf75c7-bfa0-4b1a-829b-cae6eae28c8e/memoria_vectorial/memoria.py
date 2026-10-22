# -*- coding: utf-8 -*-
"""Nucleo vectorial de la memoria. Unico dueno del indice: sqlite + LM Studio.

Contrato publico (consumido por guardian, estado, escritor, perfil, navegador,
indexer, mcp_server, aprender, crear_skills y aprender_web):

    connect() embed() sync() search() indexar_archivo() estado() parado()
    chunk_text() chunk_con_encabezado() formatear()
    contador_sumar() contador_leer()
    EmbeddingError ConexionError _http() prefijo()
    constantes: VAULT MEM_DIR HECHOS WEB_DIR ESTADO_DIR DB_PATH LOCK_PATH
                STOP_PATH STOP_INDEXER MIN_SIM POOL CHUNK_CHARS OVERLAP BATCH
                TIMEOUT LOCK_STALE_SECONDS MAX_CARACTERES_RESULTADO
                MAX_CARACTERES_TOTAL MAX_SYNC_SEGUNDOS SYNC_MIN_INTERVAL
                WEB_PREFIX DOC_EXT EXTENSIONS IGNORE_DIRS IGNORE_FILES
                MAX_CODE_BYTES MAX_FILE_BYTES EMBED_DOC_PREFIX MODELO_EMBED

Los embeddings son REALES: se piden al servidor OpenAI de LM Studio via llm.py.
Si no hay servidor o no hay modelo embed, se lanza EmbeddingError/SinConexion;
nunca se simulan vectores ni similitudes.

Reconstruido el 2026-10-22 a partir de PARCHES/memoria.py.md (secciones 0-9),
tests/test_memoria.py y los consumidores reales del proyecto.
"""
from __future__ import annotations

import contextlib
import hashlib
import json
import os
import re
import shutil
import sqlite3
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import numpy as np

import config
import incidencias
import llm
from util import proceso_vivo

# ------------------------------------------------------------------ constantes
VAULT      = config.VAULT
MEM_DIR    = config.MEM_DIR
HECHOS     = config.HECHOS
WEB_DIR    = config.WEB_DIR
ESTADO_DIR = config.ESTADO_DIR
DB_PATH    = ESTADO_DIR / "indice.sqlite"
LOCK_PATH  = ESTADO_DIR / "sync.lock"
STOP_PATH  = ESTADO_DIR / "STOP"
STOP_INDEXER = ESTADO_DIR / "STOP_INDEXER"

MIN_SIM   = float(config.get("memoria.min_sim", 0.35))
POOL      = int(config.get("memoria.pool", 30))
CHUNK_CHARS = int(config.get("memoria.chunk_chars", 1200))
OVERLAP   = int(config.get("memoria.overlap", 150))
BATCH     = int(config.get("memoria.batch", 32))
TIMEOUT   = float(config.get("memoria.timeout", 120))
LOCK_STALE_SECONDS = float(config.get("memoria.lock_vencimiento", 900))
MAX_CARACTERES_RESULTADO = int(config.get("memoria.max_caracteres_resultado", 800))
MAX_CARACTERES_TOTAL = int(config.get("memoria.max_caracteres_total", 4000))
MAX_SYNC_SEGUNDOS = float(config.get("memoria.max_sync_segundos", 0))
SYNC_MIN_INTERVAL = 5.0
WEB_PREFIX = f"{MEM_DIR.name}/Web/"

DOC_EXT      = {".md", ".txt"}
EXTENSIONS   = set(config.get("indice.extensiones", []))
IGNORE_DIRS  = set(config.get("indice.ignorar_dirs", []))
IGNORE_FILES = set(config.get("indice.ignorar_archivos", []))
MAX_CODE_BYTES = int(config.get("indice.max_bytes_archivo", 300000))
MAX_FILE_BYTES = MAX_CODE_BYTES  # alias historico usado por aprender.py

# Prefijo oficial qwen3 para busqueda asimetrica: "Instruct: {t}\nQuery:" SIN
# espacio extra. Esta documentado y NO se debe "arreglar" (PARCHES §No se toca).
EMBED_INSTRUCT = "Instruct: {task}\nQuery:{query}"

# Los documentos se embeben SIN prefijo (formato estandar qwen3). La combinacion
# (doc_prefix, modelo) es la firma del indice: si no coincide, indexar_archivo = -1.
EMBED_DOC_PREFIX = ""

TAREAS_INSTRUCT = {
    "mios": "Recuerda un apunte o documento propio guardado en la boveda.",
    "web": "Encuentra documentacion tecnica aprendida de fuentes web.",
    "query": "Encuentra el fragmento mas relevante del conocimiento guardado.",
}


def prefijo(tipo: str) -> str:
    """Plantilla instruct para el tipo de consulta, con la Query vacia."""
    return EMBED_INSTRUCT.format(task=TAREAS_INSTRUCT.get(tipo, TAREAS_INSTRUCT["query"]), query="")


def _texto_embed(texto: str, tipo: str) -> str:
    """Aplica el prefijo instruct solo a las consultas (tipo='doc' va crudo)."""
    if tipo == "doc":
        return texto
    return prefijo(tipo) + texto


MODELO_EMBED = ""  # se resuelve perezosamente con llm.modelo_embed()


def _modelo_embed() -> str:
    global MODELO_EMBED
    if not MODELO_EMBED:
        MODELO_EMBED = llm.modelo_embed()
    return MODELO_EMBED


_ultimo_sync = {"t": 0.0}


class EmbeddingError(RuntimeError):
    """El servicio de embeddings no devolvio vectores validos."""


ConexionError = llm.SinConexion


# --------------------------------------------------------------------- HTTP
def _http(metodo: str, ruta: str, cuerpo: dict | None = None, timeout: float = 900.0) -> dict:
    """Cliente OpenAI-compatible de LM Studio. Reutiliza cabeceras y endpoint de llm.py."""
    if metodo.upper() == "GET":
        return llm.http_get_json(ruta, timeout=min(float(timeout), 30.0))
    return llm.http_post_json(ruta, cuerpo or {}, timeout=float(timeout))


# -------------------------------------------------------------------- rutas
def _ruta_ignorada(rel: str) -> bool:
    rel = rel.replace("\\", "/")
    partes = rel.split("/")
    for d in IGNORE_DIRS:
        d = d.strip("/")
        if not d:
            continue
        if "/" in d:
            if rel.startswith(d + "/"):
                return True
        elif d in partes[:-1]:
            return True
    return partes[-1] in IGNORE_FILES


# ------------------------------------------------------------------ sqlite
def _crear_esquema(conn: sqlite3.Connection) -> None:
    # Migracion: indices antiguos (esqueleto corrupto) tenian chunks sin file_id.
    # El indice vectorial es reproducible: se reconstruye desde cero (contadores se conserva).
    try:
        cols = [r[1] for r in conn.execute("PRAGMA table_info(chunks)").fetchall()]
    except sqlite3.Error:
        cols = []
    if cols and "file_id" not in cols:
        conn.executescript("DROP TABLE IF EXISTS chunks_fts;\n"
                           "DROP TABLE IF EXISTS chunks;\n"
                           "DROP TABLE IF EXISTS files;")
        # los indices huérfanos de las tablas viejas no deben interferir
        for idx in ("idx_chunks_file", "idx_chunks_ruta"):
            conn.execute(f"DROP INDEX IF EXISTS {idx}")
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS files(
            id TEXT PRIMARY KEY,
            ruta TEXT UNIQUE NOT NULL,
            hash TEXT NOT NULL,
            tamano INTEGER NOT NULL DEFAULT 0,
            mtime REAL NOT NULL DEFAULT 0,
            n INTEGER NOT NULL DEFAULT 0,
            ts REAL NOT NULL DEFAULT 0
        );
        CREATE TABLE IF NOT EXISTS chunks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_id TEXT NOT NULL REFERENCES files(id) ON DELETE CASCADE,
            ruta TEXT NOT NULL,
            idx INTEGER NOT NULL,
            encabezado TEXT NOT NULL DEFAULT '',
            texto TEXT NOT NULL,
            emb BLOB,
            dim INTEGER,
            modelo TEXT NOT NULL DEFAULT ''
        );
        CREATE INDEX IF NOT EXISTS idx_chunks_file ON chunks(file_id);
        CREATE INDEX IF NOT EXISTS idx_chunks_ruta ON chunks(ruta);
        CREATE TABLE IF NOT EXISTS meta(k TEXT PRIMARY KEY, v TEXT);
        CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts USING fts5(
            texto, content='chunks', content_rowid='id'
        );
        CREATE TRIGGER IF NOT EXISTS chunks_ai AFTER INSERT ON chunks BEGIN
            INSERT INTO chunks_fts(rowid, texto) VALUES (new.id, new.texto);
        END;
        CREATE TRIGGER IF NOT EXISTS chunks_ad AFTER DELETE ON chunks BEGIN
            INSERT INTO chunks_fts(chunks_fts, rowid, texto) VALUES('delete', old.id, old.texto);
        END;
        CREATE TRIGGER IF NOT EXISTS chunks_au AFTER UPDATE ON chunks BEGIN
            INSERT INTO chunks_fts(chunks_fts, rowid, texto) VALUES('delete', old.id, old.texto);
            INSERT INTO chunks_fts(rowid, texto) VALUES (new.id, new.texto);
        END;
        """
    )
    # PARCHES §2: contadores sobreviven a _wipe (que solo borra files/chunks/chunks_fts/meta)
    cols_ctr = [r[1] for r in conn.execute("PRAGMA table_info(contadores)").fetchall()]
    if cols_ctr and set(cols_ctr) != {"k", "v", "ts"}:
        # esquema del esqueleto corrupto (clave/valor): se migra a k/v/ts conservando datos
        try:
            antiguos = conn.execute(
                f"SELECT {cols_ctr[0]}, {cols_ctr[1]} FROM contadores").fetchall()
        except sqlite3.Error:
            antiguos = []
        conn.execute("DROP TABLE contadores")
        cols_ctr = []
        with conn:
            conn.execute("CREATE TABLE contadores (k TEXT PRIMARY KEY, v INTEGER, ts REAL)")
            for fila in antiguos:
                try:
                    conn.execute("INSERT OR REPLACE INTO contadores(k, v, ts) VALUES(?,?,?)",
                                 (str(fila[0]), int(fila[1]), time.time()))
                except (TypeError, ValueError):
                    continue
    if not cols_ctr:
        conn.execute("CREATE TABLE IF NOT EXISTS contadores (k TEXT PRIMARY KEY, v INTEGER, ts REAL)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_contadores_ts ON contadores(ts)")


def connect() -> sqlite3.Connection:
    """PARCHES §1: conexion canonica con busy_timeout. Compatible con guardian.py."""
    ESTADO_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH, timeout=30.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode = WAL")
    conn.execute("PRAGMA synchronous = NORMAL")
    conn.execute("PRAGMA busy_timeout = 30000")
    _crear_esquema(conn)
    return conn


def _hay_filas(conn: sqlite3.Connection) -> bool:
    try:
        return conn.execute("SELECT COUNT(*) FROM files").fetchone()[0] > 0
    except sqlite3.Error:
        return False


def _fijar_documento(conn: sqlite3.Connection) -> None:
    """Guarda en meta el prefijo de documentos y el modelo: cambian el indice."""
    conn.execute("INSERT OR REPLACE INTO meta(k, v) VALUES('doc_prefix', ?)", (EMBED_DOC_PREFIX,))
    conn.execute("INSERT OR REPLACE INTO meta(k, v) VALUES('modelo', ?)", (_modelo_embed(),))


_REBUILD_PATH = Path(os.environ.get("MEMORIA_TEST_DIR", str(ESTADO_DIR))) / "rebuild_hechos.json"


def _rebuild_en_curso() -> bool:
    """True si hay una reconstruccion por tandas a medias (progreso persistido)."""
    return _REBUILD_PATH.exists()


def _marcar_rebuild(activo: bool) -> None:
    try:
        if activo:
            _REBUILD_PATH.write_text('{"en_curso": true}', encoding="utf-8")
        else:
            _REBUILD_PATH.unlink(missing_ok=True)
    except OSError:
        pass


def _wipe(conn: sqlite3.Connection) -> None:
    """Vacia el indice vectorial. NO toca `contadores`: son del sistema, no del indice."""
    # Orden obligatorio: DELETE FROM chunks PRIMERO (el disparador chunks_ad limpia
    # chunks_fts fila a fila). Borrar chunks_fts antes deja el indice FTS inconsistente
    # y el siguiente DELETE falla con "database disk image is malformed".
    conn.execute("DELETE FROM chunks")
    conn.execute("DELETE FROM files")
    conn.execute("DELETE FROM meta")
    with contextlib.suppress(sqlite3.Error):
        conn.execute("DELETE FROM chunks_fts")  # red de seguridad por si quedara algo
    # Reinicia el contador AUTOINCREMENT de chunks (evita rowids huerfanos en fts).
    with contextlib.suppress(sqlite3.Error):
        conn.execute("DELETE FROM sqlite_sequence WHERE name='chunks'")


# -------------------------------------------------------------- locks (§3)
def _pid_del_lock() -> int:
    """pid guardado en el lock (primera palabra). -1 si no se puede leer."""
    try:
        return int(LOCK_PATH.read_text(encoding="ascii").split()[0])
    except (OSError, ValueError, IndexError):
        return -1


def _lock_es_nuestro() -> bool:
    return LOCK_PATH.exists() and _pid_del_lock() == os.getpid()


def _lock_viejo_y_ajeno() -> bool:
    """True si el lock es viejo Y su dueno esta muerto (solo entonces se roba)."""
    try:
        viejo = (time.time() - LOCK_PATH.stat().st_mtime) > LOCK_STALE_SECONDS
    except OSError:
        return False
    if not viejo:
        return False
    pid = _pid_del_lock()
    if pid == os.getpid():
        return False
    return not proceso_vivo(pid)


def _acquire_lock() -> bool:
    """True si tomamos el lock. El archivo guarda '<pid> <timestamp>'."""
    LOCK_PATH.parent.mkdir(parents=True, exist_ok=True)
    if _lock_es_nuestro():
        return False
    try:
        fd = os.open(str(LOCK_PATH), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        if _lock_viejo_y_ajeno():
            with contextlib.suppress(OSError):
                LOCK_PATH.unlink()
            return _acquire_lock()
        return False
    try:
        os.write(fd, f"{os.getpid()} {time.time():.3f}".encode("ascii"))
    finally:
        os.close(fd)
    return True


def _release_lock() -> None:
    """Solo borra el lock si es nuestro (pid dentro del archivo == el nuestro)."""
    if _lock_es_nuestro():
        with contextlib.suppress(OSError):
            LOCK_PATH.unlink()


def _refrescar_lock() -> None:
    """Reafirma el lock (pid + timestamp nuevo) durante un sync largo."""
    if _lock_es_nuestro():
        with contextlib.suppress(OSError):
            LOCK_PATH.write_text(f"{os.getpid()} {time.time():.3f}", encoding="ascii")


# ----------------------------------------------------------- contadores (§2)
def _ventana(ventana_horas: float | None) -> tuple[str, int]:
    """(sufijo legible, segundos de corte). Por defecto: 1 hora."""
    if ventana_horas is None:
        ventana_horas = 1.0
    ventana_horas = float(ventana_horas)
    if abs(ventana_horas - 1.0) < 1e-9:
        sufijo = "hora"
    elif abs(ventana_horas - 24.0) < 1e-9:
        sufijo = "dia"
    elif abs(ventana_horas - 168.0) < 1e-9:
        sufijo = "semana"
    else:
        sufijo = f"{int(round(ventana_horas))}h"
    return sufijo, max(1, int(ventana_horas * 3600))


def _conn_contadores() -> sqlite3.Connection:
    """Conexion minima para contadores. Crea la tabla si el indice aun no existe."""
    ESTADO_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH, timeout=30.0)
    conn.execute("PRAGMA busy_timeout = 30000")
    conn.execute("CREATE TABLE IF NOT EXISTS contadores (k TEXT PRIMARY KEY, v INTEGER, ts REAL)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_contadores_ts ON contadores(ts)")
    return conn


def contador_sumar(clave: str, n: int = 1, ventana_horas: float = 1) -> int:
    """Suma n al contador de la ventana actual. Devuelve el total de esa ventana."""
    sufijo, corte = _ventana(ventana_horas)
    k = f"{clave}@{sufijo}"
    ahora = time.time()
    conn = _conn_contadores()
    try:
        with conn:
            conn.execute("DELETE FROM contadores WHERE k=? AND ts < ?", (k, ahora - corte))
            fila = conn.execute("SELECT v FROM contadores WHERE k=?", (k,)).fetchone()
            if fila is None:
                conn.execute("INSERT INTO contadores(k, v, ts) VALUES(?, ?, ?)", (k, int(n), ahora))
                return int(n)
            nuevo = int(fila[0]) + int(n)
            conn.execute("UPDATE contadores SET v=?, ts=? WHERE k=?", (nuevo, ahora, k))
            return nuevo
    finally:
        conn.close()


def contador_leer(clave: str, ventana_horas: float = 1) -> int:
    """Valor del contador dentro de la ventana vigente (0 si esa ventana esta vacia)."""
    sufijo, corte = _ventana(ventana_horas)
    k = f"{clave}@{sufijo}"
    conn = _conn_contadores()
    try:
        fila = conn.execute(
            "SELECT v FROM contadores WHERE k=? AND ts >= ?", (k, time.time() - corte)
        ).fetchone()
        return int(fila[0]) if fila else 0
    finally:
        conn.close()


# ------------------------------------------------------------ troceado (no se toca)
_ENCABEZADO = re.compile(r"^(#{1,6})\s+(.*)$")


def _trocear(texto: str, markdown: bool = True) -> list[tuple[str, str]]:
    """[(encabezado, texto)]. Respeta bloques ``` (un # dentro NO es titulo)
    y corta los parrafos gigantes sin perder nada."""
    secciones: list[tuple[str, str]] = []
    enc, buf, en_codigo = "", [], False
    for linea in (texto or "").splitlines():
        if linea.strip().startswith("```"):
            en_codigo = not en_codigo
        m = None if (en_codigo or not markdown) else _ENCABEZADO.match(linea)
        if m:
            secciones.append((enc, "\n".join(buf)))
            enc, buf = m.group(2).strip(), []
        else:
            buf.append(linea)
    secciones.append((enc, "\n".join(buf)))

    trozos: list[tuple[str, str]] = []
    for head, cuerpo in secciones:
        cuerpo = cuerpo.strip()
        if not cuerpo:
            continue
        for parrafo in re.split(r"\n\s*\n", cuerpo):
            parrafo = parrafo.strip()
            if not parrafo:
                continue
            if len(parrafo) <= CHUNK_CHARS:
                trozos.append((head, parrafo))
            else:
                # Corte en huecos de palabra para no duplicar texto (OVERLAP es
                # solo orientativo; solapar reenviaria palabras y el test
                # "chunk_text_no_pierde_nada" exige que cada palabra aparezca
                # exactamente una vez).
                sin_rebanar = True
                while sin_rebanar and len(parrafo) > CHUNK_CHARS:
                    corte = parrafo.rfind(" ", 0, CHUNK_CHARS)
                    if corte <= 0:
                        corte = CHUNK_CHARS
                    trozos.append((head, parrafo[:corte].rstrip()))
                    parrafo = parrafo[corte:].lstrip()
                    sin_rebanar = True
                if parrafo:
                    trozos.append((head, parrafo))
    return trozos


def chunk_text(texto: str, markdown: bool = True) -> list[str]:
    """Lista de fragmentos (texto plano). Se conserva todo el contenido."""
    return [cuerpo for _, cuerpo in _trocear(texto, markdown)]


def chunk_con_encabezado(texto: str, markdown: bool = True) -> list[tuple[str, str]]:
    """Igual, pero [(encabezado, texto)] para el indexador."""
    return _trocear(texto, markdown)


# ---------------------------------------------------------------- embeddings (§4)
def _embed_una_vez(texts: list[str], tipo: str) -> np.ndarray:
    """Una sola llamada a /v1/embeddings. Lanza EmbeddingError/SinConexion si falla."""
    modelo = _modelo_embed()
    if not modelo:
        raise EmbeddingError("no hay modelo de embeddings cargado en LM Studio")
    cuerpo = {
        "model": modelo,
        "input": [_texto_embed(t, tipo) for t in texts],
        "encoding_format": "float",
    }
    try:
        datos = _http("POST", "/embeddings", cuerpo, timeout=TIMEOUT)
    except (llm.ErrorLLM, KeyError, IndexError, TypeError) as e:
        raise EmbeddingError(f"embeddings fallaron: {str(e)[:200]}") from e
    filas = datos.get("data") or []
    if len(filas) != len(texts):
        raise EmbeddingError(f"el modelo devolvio {len(filas)} vectores para {len(texts)} textos")
    orden = sorted(filas, key=lambda f: f.get("index", 0))
    matriz = np.asarray([f["embedding"] for f in orden], dtype=np.float32)
    if matriz.ndim != 2 or matriz.shape[0] != len(texts) or matriz.shape[1] == 0:
        raise EmbeddingError("respuesta de embeddings con forma inesperada")
    return matriz


def _embed_lote(texts: list[str], tipo: str) -> np.ndarray:
    """Reintento por lote con backoff (PARCHES §4). Usa llm.reintentos/pausa_reintento."""
    intentos = max(1, int(config.get("llm.reintentos", 3)))
    pausa = float(config.get("llm.pausa_reintento", 5.0))
    ultimo: Exception | None = None
    for i in range(intentos):
        try:
            return _embed_una_vez(texts, tipo)
        except (EmbeddingError, llm.SinConexion) as e:
            ultimo = e
            if i < intentos - 1:
                time.sleep(pausa * (i + 1))
    assert ultimo is not None
    raise ultimo


def embed(textos: list[str], tipo: str = "doc") -> np.ndarray:
    """Embebe una lista de textos DE FORMA REAL via LM Studio. Devuelve ndarray (n, dim).

    tipo='doc' para indexar; 'query'|'mios'|'web' para buscar (prefijo instruct qwen3).
    """
    textos = [str(t) for t in textos]
    if not textos:
        return np.zeros((0, 0), dtype=np.float32)
    partes: list[np.ndarray] = []
    for inicio in range(0, len(textos), BATCH):
        partes.append(_embed_lote(textos[inicio:inicio + BATCH], tipo))
    return partes[0] if len(partes) == 1 else np.vstack(partes)


# ---------------------------------------------------------------- escaneo
def _hash_de(contenido: bytes) -> str:
    return hashlib.sha256(contenido).hexdigest()[:16]


def _leer(rel: str) -> str | None:
    """Lee un archivo de la boveda como texto. None si ilegible/binario."""
    try:
        crudo = (VAULT / rel).read_bytes()
    except OSError:
        return None
    try:
        return crudo.decode("utf-8-sig")
    except UnicodeDecodeError:
        return crudo.decode("latin-1", errors="replace")


def _escanear() -> dict[str, dict]:
    """{rel: {'texto','hash','tamano','mtime'}} de todos los archivos indexables."""
    salida: dict[str, dict] = {}
    if not VAULT.exists():
        return salida
    for raiz, dirs, archivos in os.walk(VAULT):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith(".")]
        for nombre in archivos:
            if Path(nombre).suffix.lower() not in EXTENSIONS:
                continue
            try:
                p = Path(raiz) / nombre
                st = p.stat()
                rel = p.relative_to(VAULT).as_posix()
            except (OSError, ValueError):
                continue
            if _ruta_ignorada(rel) or not 0 < st.st_size <= MAX_FILE_BYTES:
                continue
            texto = _leer(rel)
            salida[rel] = {
                "texto": texto,
                "hash": _hash_de(texto.encode("utf-8")) if texto is not None else None,
                "tamano": st.st_size,
                "mtime": float(st.st_mtime),
            }
    return salida


def _insertar_chunks(conn: sqlite3.Connection, rel: str, file_id: str,
                     trozos: list[tuple[str, str]], vectores: np.ndarray) -> None:
    for i, ((enc, cuerpo), vec) in enumerate(zip(trozos, vectores)):
        conn.execute(
            "INSERT INTO chunks(file_id, ruta, idx, encabezado, texto, emb, dim, modelo)"
            " VALUES(?,?,?,?,?,?,?,?)",
            (file_id, rel, i, enc, cuerpo, np.ascontiguousarray(vec, dtype=np.float32).tobytes(),
             int(vec.shape[0]), _modelo_embed()),
        )


def _file_id_de(rel: str) -> str:
    return hashlib.sha1(rel.encode("utf-8")).hexdigest()[:24]


# ------------------------------------------------------------ indexar_archivo (§5)
def indexar_archivo(rel: str) -> int:
    """Indexa (o reindexa) UN archivo ya escrito en disco.

    Devuelve: -1 indice de otro modelo/prefijo incompatible,
               0 sin cambios o archivo ilegible,
              >0 numero de fragmentos indexados.
    """
    rel = str(rel).replace("\\", "/").strip("/")
    conn = connect()
    try:
        fila = conn.execute("SELECT v FROM meta WHERE k='doc_prefix'").fetchone()
        if fila and fila[0] != EMBED_DOC_PREFIX:
            return -1
        fila = conn.execute("SELECT v FROM meta WHERE k='modelo'").fetchone()
        if fila and fila[0] != _modelo_embed():
            return -1

        try:
            st = (VAULT / rel).stat()
        except OSError:
            return 0
        texto = _leer(rel)
        if texto is None or not 0 < st.st_size <= MAX_FILE_BYTES:
            return 0
        hash_actual = _hash_de(texto.encode("utf-8"))
        anterior = conn.execute("SELECT id, hash FROM files WHERE ruta=?", (rel,)).fetchone()
        if anterior and anterior["hash"] == hash_actual:
            return 0

        trozos = chunk_con_encabezado(texto, markdown=Path(rel).suffix.lower() in DOC_EXT)
        if not trozos:
            return 0
        try:
            vectores = embed([c for _, c in trozos], tipo="doc")
        except (EmbeddingError, llm.SinConexion) as e:
            incidencias.registrar_si_toca("indice", type(e).__name__, "media", str(e)[:200])
            raise

        file_id = _file_id_de(rel)
        with conn:
            if anterior:
                conn.execute("DELETE FROM chunks WHERE file_id=?", (anterior["id"],))
                conn.execute("DELETE FROM files WHERE id=?", (anterior["id"],))
            conn.execute(
                "INSERT INTO files(id, ruta, hash, tamano, mtime, n, ts) VALUES(?,?,?,?,?,?,?)",
                (file_id, rel, hash_actual, st.st_size, float(st.st_mtime),
                 len(trozos), time.time()),
            )
            _insertar_chunks(conn, rel, file_id, trozos, vectores)
            if not conn.execute("SELECT v FROM meta WHERE k='doc_prefix'").fetchone():
                _fijar_documento(conn)
        return len(trozos)
    finally:
        conn.close()


# --------------------------------------------------------------------- sync (§6)
def sync(max_segundos: float | None = None, forzar: bool = False) -> dict:
    """Pone el indice al dia. Escanea la boveda e indexa lo nuevo/modificado/eliminado.

    Devuelve resumen {'nuevos','modificados','eliminados','sin_cambios'[, 'parcial']}.
    Si otro proceso tiene el lock, devuelve {'omitido': 'lock'} sin esperar.
    Con `forzar=True` reconstruye todo desde cero (tras copia a indice.sqlite.bak).
    """
    presupuesto = MAX_SYNC_SEGUNDOS if max_segundos is None else float(max_segundos)
    if not forzar and tiempo_desde_sync() < SYNC_MIN_INTERVAL:
        return {"nuevos": 0, "modificados": 0, "eliminados": 0, "sin_cambios": 0,
                "omitido": "reciente"}
    if not _acquire_lock():
        return {"nuevos": 0, "modificados": 0, "eliminados": 0, "sin_cambios": 0,
                "omitido": "lock"}
    t0 = time.time()
    resumen = {"nuevos": 0, "modificados": 0, "eliminados": 0, "sin_cambios": 0}
    try:
        conn = connect()
        try:
            presentes = _escanear()
            conocidos = {r["ruta"]: (r["hash"], r["id"]) for r in
                         conn.execute("SELECT id, ruta, hash FROM files").fetchall()}

            if forzar and _hay_filas(conn):
                # Reconstruccion completa POR TANDAS (memoria por archivo, no todo
                # en RAM). Progreso persistido en un hecho de indice: la primera
                # pasada vacia el indice; cada tanda indexa archivos hasta agotar el
                # presupuesto y los terminos ya reindexados (hash actual) se saltan.
                # Si LM Studio cae a mitad, la siguiente ejecucion continua sin
                # repetir trabajo. Copia a .bak ANTES del primer _wipe (PARCHES §6).
                if not _rebuild_en_curso():
                    with contextlib.suppress(OSError):
                        shutil.copy2(DB_PATH, DB_PATH.with_name(DB_PATH.name + ".bak"))
                    with conn:
                        _wipe(conn)
                    _marcar_rebuild(True)
                pendientes = [rel for rel, info in sorted(presentes.items())
                              if info["texto"] is not None]
                resumen["sin_cambios"] = len(presentes) - len(pendientes)
                procesados = 0
                try:
                    for rel in pendientes:
                        info = presentes[rel]
                        if conocidos.get(rel, (None,))[0] == info["hash"]:
                            continue  # ya reindexado en una tanda anterior
                        if presupuesto and (time.time() - t0) > presupuesto:
                            resumen["parcial"] = True
                            break
                        if parado():
                            resumen["parcial"] = True
                            break
                        trozos = chunk_con_encabezado(
                            info["texto"],
                            markdown=Path(rel).suffix.lower() in DOC_EXT)
                        if not trozos:
                            continue
                        vectores = embed([c for _, c in trozos], tipo="doc")
                        file_id = _file_id_de(rel)
                        viejo = conocidos.get(rel)
                        with conn:
                            if viejo:
                                conn.execute("DELETE FROM chunks WHERE file_id=?",
                                             (viejo[1],))
                                conn.execute("DELETE FROM files WHERE id=?",
                                             (viejo[1],))
                            conn.execute(
                                "INSERT INTO files(id, ruta, hash, tamano, mtime, n, ts)"
                                " VALUES(?,?,?,?,?,?,?)",
                                (file_id, rel, info["hash"], info["tamano"],
                                 info["mtime"], len(trozos), time.time()),
                            )
                            _insertar_chunks(conn, rel, file_id, trozos, vectores)
                        resumen["nuevos"] += 1
                        procesados += 1
                        if procesados % 50 == 0:
                            _refrescar_lock()
                except (EmbeddingError, llm.SinConexion) as e:
                    incidencias.registrar("indice", type(e).__name__, "media",
                                          str(e)[:200])
                    raise
                finally:
                    if not resumen.get("parcial"):
                        with conn:
                            _fijar_documento(conn)
                        _marcar_rebuild(False)
                _ultimo_sync["t"] = time.time()
                return resumen

            obsoletos = set(conocidos) - set(presentes)
            pendientes = []
            for rel, info in sorted(presentes.items()):
                viejo = conocidos.get(rel)
                if info["hash"] is None:
                    continue
                if viejo and viejo[0] == info["hash"]:
                    resumen["sin_cambios"] += 1
                    continue
                resumen["nuevos" if not viejo else "modificados"] += 1
                pendientes.append(rel)

            with conn:
                for rel in sorted(obsoletos):
                    _, fid = conocidos[rel]
                    conn.execute("DELETE FROM chunks WHERE file_id=?", (fid,))
                    conn.execute("DELETE FROM files WHERE id=?", (fid,))
            resumen["eliminados"] = len(obsoletos)

            procesados = 0
            for rel in pendientes:
                if presupuesto and (time.time() - t0) > presupuesto:
                    resumen["parcial"] = True
                    break
                if parado():
                    resumen["parcial"] = True
                    break
                info = presentes[rel]
                trozos = chunk_con_encabezado(
                    info["texto"], markdown=Path(rel).suffix.lower() in DOC_EXT)
                try:
                    vectores = embed([c for _, c in trozos], tipo="doc") if trozos else None
                except (EmbeddingError, llm.SinConexion) as e:
                    incidencias.registrar("indice", type(e).__name__, "media", str(e)[:200])
                    raise
                file_id = _file_id_de(rel)
                viejo = conocidos.get(rel)
                with conn:
                    if viejo:
                        conn.execute("DELETE FROM chunks WHERE file_id=?", (viejo[1],))
                        conn.execute("DELETE FROM files WHERE id=?", (viejo[1],))
                    conn.execute(
                        "INSERT INTO files(id, ruta, hash, tamano, mtime, n, ts)"
                        " VALUES(?,?,?,?,?,?,?)",
                        (file_id, rel, info["hash"], info["tamano"], info["mtime"],
                         len(trozos), time.time()),
                    )
                    if vectores is not None:
                        _insertar_chunks(conn, rel, file_id, trozos, vectores)
                procesados += 1
                if procesados % 50 == 0:
                    _refrescar_lock()
            if procesados:
                with conn:
                    if not conn.execute("SELECT v FROM meta WHERE k='doc_prefix'").fetchone():
                        _fijar_documento(conn)
        finally:
            conn.close()
        _ultimo_sync["t"] = time.time()
        return resumen
    finally:
        _release_lock()


def tiempo_desde_sync() -> float:
    return time.time() - _ultimo_sync["t"]


# ------------------------------------------------------------------- search (§7)
def _filtro_ambito(ambito: str) -> tuple[str, tuple]:
    a = (ambito or "todo").lower()
    if a in ("mios", "notas", "propias"):
        return f"ruta LIKE '{MEM_DIR.name}/%' AND ruta NOT LIKE ?", (WEB_PREFIX,)
    if a == "web":
        return "ruta LIKE ?", (WEB_PREFIX,)
    if a == "skills":
        return "ruta LIKE ?", (f"{config.SKILLS_DIR.name}/",)
    if a == "codigo":
        return "ruta NOT LIKE '%.md' AND ruta NOT LIKE '%.txt'", ()
    return "", ()


def search(consulta: str, k: int = 5, ambito: str = "todo",
           auto_sync: bool = True, min_sim: float | None = None) -> list[dict]:
    """Busqueda vectorial REAL (coseno) sobre los chunks, con refuerzo léxico FTS5.

    Devuelve list[dict] con claves: ruta, texto, score, encabezado.
    Filtra por `min_sim` (por defecto MIN_SIM de reglas.json).
    """
    umbral = MIN_SIM if min_sim is None else float(min_sim)
    if auto_sync:
        sync(max_segundos=MAX_SYNC_SEGUNDOS)
    consulta = (consulta or "").strip()
    if not consulta:
        return []
    conn = connect()
    try:
        where, params = _filtro_ambito(ambito)
        sql = "SELECT id, ruta, encabezado, texto, emb FROM chunks"
        if where:
            sql += f" WHERE {where}"
        filas = conn.execute(sql, params).fetchall()
    finally:
        conn.close()
    if not filas:
        return []

    q = embed([consulta], tipo=ambito if ambito in ("mios", "web") else "query")[0]
    matriz = np.stack([np.frombuffer(f["emb"], dtype=np.float32) for f in filas])
    normas = np.linalg.norm(matriz, axis=1) * np.linalg.norm(q)
    scores = np.divide(matriz @ q, normas, out=np.zeros(len(filas), dtype=np.float32),
                       where=normas > 0)

    # Refuerzo léxico modesto via FTS5 (no sustituye la busqueda vectorial).
    try:
        conn = connect()
        try:
            palabras = [w for w in re.findall(r"\w+", consulta.lower()) if len(w) > 3][:6]
            if palabras:
                match = " OR ".join(f'"{w}"' for w in palabras)
                ids_lex = {r[0] for r in conn.execute(
                    "SELECT rowid FROM chunks_fts WHERE chunks_fts MATCH ? LIMIT 200",
                    (match,)).fetchall()}
                for idx, f in enumerate(filas):
                    if f["id"] in ids_lex:
                        scores[idx] = min(1.0, float(scores[idx]) + 0.05)
        finally:
            conn.close()
    except sqlite3.Error:
        pass

    resultados: list[dict] = []
    for idx in np.argsort(scores)[::-1][: max(int(k), 1) * 2]:
        s = float(scores[int(idx)])
        if s < umbral:
            break
        f = filas[int(idx)]
        resultados.append({"ruta": f["ruta"], "texto": f["texto"],
                           "score": round(s, 4), "encabezado": f["encabezado"]})
        if len(resultados) >= int(k):
            break
    return resultados


# ------------------------------------------------------------------ formatear (§8)
def _recortar_texto(t: str, limite: int) -> str:
    t = (t or "").strip()
    return t if len(t) <= limite else t[:limite].rstrip() + " [...]"


def formatear(resultados: list[dict], notas: list[str] | None = None) -> str:
    """Texto legible para el LLM, acotado por bloque y en total."""
    notas = list(notas or [])
    partes = [f"Aviso: {n}" for n in notas]
    if not resultados:
        partes.append("Sin resultados relevantes en la memoria.")
    for i, r in enumerate(resultados, 1):
        ruta = r.get("ruta", "?")
        enc = r.get("encabezado") or ""
        donde = f"{ruta} › {enc}" if enc else ruta
        sim = r.get("similitud", r.get("score"))
        etiqueta = f" (similitud {sim:.2f})" if isinstance(sim, (int, float)) else ""
        cuerpo = _recortar_texto(r.get("texto"), MAX_CARACTERES_RESULTADO)
        partes.append(f"[{i}] {donde}{etiqueta}\n{cuerpo}")
    salida = "\n\n".join(partes)
    if len(salida) > MAX_CARACTERES_TOTAL:
        salida = salida[:MAX_CARACTERES_TOTAL].rstrip() + " [...]"
    return salida


# ------------------------------------------------------------- estado / parado (§9)
def estado() -> dict:
    """Resumen del indice para estado.py y guardian.py. Nunca lanza."""
    salida = {"archivos": 0, "fragmentos": 0, "db_mb": 0.0, "modelo": "",
              "listo": False, "parado": parado()}
    try:
        if DB_PATH.exists():
            salida["db_mb"] = round(DB_PATH.stat().st_size / 1e6, 2)
        conn = connect()
        try:
            salida["archivos"] = conn.execute("SELECT COUNT(*) c FROM files").fetchone()["c"]
            salida["fragmentos"] = conn.execute("SELECT COUNT(*) c FROM chunks").fetchone()["c"]
            fila = conn.execute("SELECT v FROM meta WHERE k='modelo'").fetchone()
            salida["modelo"] = fila[0] if fila else ""
            salida["listo"] = salida["archivos"] > 0
        finally:
            conn.close()
    except sqlite3.Error:
        pass
    return salida


def parado() -> bool:
    """PARCHES §9: STOP global, STOP solo-del-indexador o STOP dentro de las notas."""
    return STOP_PATH.exists() or STOP_INDEXER.exists() or (MEM_DIR / "STOP").exists()


# ---------------------------------------------------------------------- CLI
def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--check" in argv:
        print(f"boveda : {VAULT} ({'existe' if VAULT.exists() else 'AUSENTE -> defaults'})")
        print(f"indice : {DB_PATH}")
        print(f"estado : {estado()}")
        print(f"lock   : {LOCK_PATH} ({'tomado' if LOCK_PATH.exists() else 'libre'})")
        print(f"parado : {parado()}")
        return 0
    if "--estado" in argv:
        print(json.dumps(estado(), ensure_ascii=False, indent=2))
        return 0
    print(__doc__)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
