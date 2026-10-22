"""Módulo de memoria para almacenamiento y recuperación de datos.

Permite:
- Almacenar documentos con embeddings.
- Recuperar documentos por consulta.
- Gestionar persistencia en disco.

Uso:
    from memoria import Memoria
    
    mem = Memoria.crear_memoria()
    if mem.cargar():
        # Guardar documento
        mem.guardar({"contenido": "texto", "titulo": "Titulo"})
        
        # Recuperar por consulta
        resultados = mem.recuperar("consulta")
"""
from __future__ import annotations

import json
from pathlib import Path


# ------------------------------------------------------------------ rutas y estado
AQUI = Path(__file__).resolve().parent.parent


class Memoria:
    """Clase principal para gestionar la memoria de documentos."""
    
    def __init__(self):
        """Inicializa la memoria de documentos."""
        self._cargada = False
        self.documentos = []  # Lista de documentos almacenados
        self.ruta_memoria = AQUI / "memoria.json"
    
    @staticmethod
    def crear_memoria() -> Memoria:
        """Crea una instancia de Memoria.

        Returns:
            Instancia de Memoria.
        """
        return Memoria()
    
    def cargar(self) -> bool:
        """Carga la memoria desde archivo o fuente externa.

        Returns:
            True si se cargó correctamente, False si hubo error.
        """
        try:
            # Simulación de carga de memoria
            self._cargada = True
            print(f"Memoria cargada desde {self.ruta_memoria}")
            
            # Si existe archivo de memoria, cargarlo
            if self.ruta_memoria.exists():
                with open(self.ruta_memoria, "r", encoding="utf-8") as f:  # noqa: PTH123
                    datos = json.load(f)
                    self.documentos = datos.get("documentos", [])
            
            print(f"Cargados {len(self.documentos)} documentos.")
            return True
            
        except Exception as e:  # noqa: BLE001
            print(f"Error al cargar memoria: {e}")
            return False
    
    def guardar(self, documento: dict) -> bool:
        """Guarda un nuevo documento en la memoria.

        Args:
            documento: diccionario con "contenido", "titulo", "fecha".

        Returns:
            True si se guardó correctamente, False si hubo error.
        """
        try:
            if not self._cargada:
                print("Memoria no cargada.")
                return False
            
            # Generar embedding para el contenido (simulado)
            from llm import LLM
            llm = LLM.crear_llm()
            
            if not llm.cargar():
                return False
            
            embedding = llm.generar_embedding(documento["contenido"])
            
            # Crear documento almacenado con metadatos
            doc_guardado = {
                "documento": documento,
                "embedding": embedding,
                "similitud": 1.0,  # Se calculará en recuperación
            }
            
            self.documentos.append(doc_guardado)
            print(f"Documento guardado: {documento.get('titulo', 'sin titulo')}")
            
            return True
            
        except Exception as e:  # noqa: BLE001
            print(f"Error al guardar documento: {e}")
            return False
    
    def recuperar(self, consulta: str, top_k: int = 5) -> list[dict]:
        """Recupera documentos por similitud con la consulta.

        Args:
            consulta: cadena de texto a buscar.
            top_k: número máximo de resultados a devolver.

        Returns:
            Lista de diccionarios con "documento" y "similitud".
        """
        try:
            if not self._cargada:
                print("Memoria no cargada.")
                return []
            
            # Generar embedding para la consulta (simulado)
            from llm import LLM
            llm = LLM.crear_llm()
            
            if not llm.cargar():
                return []
            
            embedding_consulta = llm.generar_embedding(consulta)
            
            # Calcular similitud con cada documento (simulado)
            resultados = []
            for doc in self.documentos:
                # Simulación de cálculo de similitud coseno
                import random
                random.seed(hash(consulta + str(doc["documento"]["contenido"])) % 2**32)
                
                similitud = sum(random.uniform(-1, 1) for _ in range(len(embedding_consulta))) / len(embedding_consulta)
                # Normalizar similitud entre 0 y 1
                similitud = max(0.0, min(1.0, (similitud + 1) / 2))
                
                resultados.append({
                    "documento": doc["documento"],
                    "similitud": similitud,
                })
            
            # Ordenar por similitud (descendente) y tomar top_k
            resultados.sort(key=lambda x: x["similitud"], reverse=True)
            resultados = resultados[:top_k]
            
            return resultados
            
        except Exception as e:  # noqa: BLE001
            print(f"Error al recuperar documentos: {e}")
            return []


def _main() -> None:
    """Función principal para pruebas rápidas."""
    print("Memoria - Pruebas rápidas")
    print("-" * 40)
    
    # Crear instancia
    mem = Memoria.crear_memoria()
    
    if not mem.cargar():
        print("No se pudo cargar la memoria.")
        return
    
    # Guardar documentos de prueba
    print("\nGuardando documentos...")
    documentos_prueba = [
        {"contenido": "La inteligencia artificial es una rama de la informática.", "titulo": "IA", "fecha": "2024-01-01"},
        {"contenido": "El aprendizaje automático permite a las máquinas aprender de datos.", "titulo": "ML", "fecha": "2024-01-02"},
        {"contenido": "Los modelos de lenguaje generan texto coherente y contextualizado.", "titulo": "NLP", "fecha": "2024-01-03"},
    ]
    
    for doc in documentos_prueba:
        mem.guardar(doc)
    
    print(f"\nDocumentos guardados: {len(mem.documentos)}")
    
    # Recuperar con consulta de prueba
    print("\nRecuperando...")
    resultados = mem.recuperar("¿Qué es la inteligencia artificial?", top_k=2)
    
    if resultados:
        for i, r in enumerate(resultados, 1):
            print(f"\n{i}. Título: {r['documento']['titulo']} (Relevancia: {r['similitud']:.4f})")

# ==========================================================================
# API ESTABLE / COMPATIBILIDAD   (2026-10-22)
# Bloque autonomo: NO depende de constantes de arriba. Si el archivo ya
# define algo, se respeta (setdefault / try-except NameError).
# Locks con dueno, contadores por ventana, troceado y formateo acotado.
# ==========================================================================
import contextlib as _ctx
import os as _os
import re as _re2
import sqlite3 as _sql3
import time as _t2
from pathlib import Path as _P2

try:
    VAULT
except NameError:                                    # noqa: B018
    import config as _cfg
    VAULT = _P2(getattr(_cfg, "VAULT", getattr(_cfg, "BOVEDA", ".")))

try:
    DB_PATH
except NameError:                                    # noqa: B018
    DB_PATH = _P2(VAULT) / ".memoria" / "indice.sqlite"

try:
    LOCK_PATH
except NameError:                                    # noqa: B018
    LOCK_PATH = _P2(DB_PATH).parent / "sync.lock"

for _nombre, _valor in (
    ("LOCK_STALE_SECONDS", 900),
    ("CHUNK_CHARS", 1200),
    ("MAX_CARACTERES_RESULTADO", 800),
    ("MAX_CARACTERES_TOTAL", 4000),
):
    globals().setdefault(_nombre, _valor)


def _ruta_db():
    """Ruta real del sqlite del indice: la saca de la conexion, para no
    crear un archivo aparte. Si no se puede, cae a DB_PATH."""
    try:
        conn = connect()
        try:
            for fila in conn.execute("PRAGMA database_list").fetchall():
                if fila[1] == "main" and fila[2]:
                    return _P2(fila[2])
        finally:
            conn.close()
    except Exception:                                # noqa: BLE001
        pass
    try:
        return _P2(DB_PATH)
    except NameError:
        return _P2(VAULT) / ".memoria" / "indice.sqlite"


# ------------------------------------------------------------------ locks
def _pid_del_lock(ruta=None):
    """pid guardado en el lock (primera palabra). -1 si no se puede leer."""
    try:
        return int(_P2(ruta or LOCK_PATH).read_text(encoding="ascii").split()[0])
    except (OSError, ValueError, IndexError):
        return -1


def _lock_es_nuestro():
    return LOCK_PATH.exists() and _pid_del_lock() == _os.getpid()


def _duenno_vivo(pid):
    if pid <= 0:
        return False
    try:
        from util import proceso_vivo
        return bool(proceso_vivo(pid))
    except Exception:                                # noqa: BLE001
        try:
            _os.kill(pid, 0)
            return True
        except OSError:
            return False


def _acquire_lock():
    """True si tomamos el lock. Un lock viejo de un proceso MUERTO se roba;
    uno viejo de un proceso VIVO no."""
    LOCK_PATH.parent.mkdir(parents=True, exist_ok=True)
    if _lock_es_nuestro():
        return False
    try:
        fd = _os.open(LOCK_PATH, _os.O_CREAT | _os.O_EXCL | _os.O_WRONLY)
    except FileExistsError:
        pid = _pid_del_lock()
        if pid == _os.getpid():
            return False
        try:
            viejo = (_t2.time() - LOCK_PATH.stat().st_mtime) > LOCK_STALE_SECONDS
        except OSError:
            viejo = False
        if viejo and not _duenno_vivo(pid):
            with _ctx.suppress(OSError):
                LOCK_PATH.unlink()
            return _acquire_lock()
        return False
    try:
        _os.write(fd, f"{_os.getpid()} {_t2.time():.3f}".encode("ascii"))
    finally:
        _os.close(fd)
    return True


def _release_lock():
    """Solo borra el lock si es nuestro (pid dentro del archivo == el nuestro)."""
    if _lock_es_nuestro():
        with _ctx.suppress(OSError):
            LOCK_PATH.unlink()


def _refrescar_lock():
    """Reafirma el lock (pid + mtime) durante un sync largo."""
    if _lock_es_nuestro():
        with _ctx.suppress(OSError):
            LOCK_PATH.write_text(f"{_os.getpid()} {_t2.time():.3f}", encoding="ascii")


# -------------------------------------------------------------- contadores
def _conn_contadores():
    ruta = _ruta_db()
    _P2(ruta).parent.mkdir(parents=True, exist_ok=True)
    conn = _sql3.connect(ruta, timeout=30)
    conn.execute("CREATE TABLE IF NOT EXISTS contadores("
                 "clave TEXT PRIMARY KEY, valor INTEGER NOT NULL DEFAULT 0)")
    return conn


def _clave_contador(nombre, ventana=None, ventana_horas=None):
    if ventana is None:
        if ventana_horas is not None or str(nombre).endswith(".hora"):
            ventana = "hora"
        elif str(nombre).endswith(".dia"):
            ventana = "dia"
        else:
            ventana = "total"
    sello = _t2.strftime("%Y-%m-%dT%H") if ventana == "hora" else (
        _t2.strftime("%Y-%m-%d") if ventana == "dia" else "")
    return f"{nombre}@{sello}"


def contador_sumar(nombre, n=1, ventana=None, ventana_horas=None, **_):
    """Suma n al contador de la ventana actual y devuelve el total de esa ventana."""
    clave = _clave_contador(nombre, ventana, ventana_horas)
    conn = _conn_contadores()
    try:
        with conn:
            conn.execute(
                "INSERT INTO contadores(clave, valor) VALUES(?, ?) "
                "ON CONFLICT(clave) DO UPDATE SET valor = valor + ?",
                (clave, int(n), int(n)),
            )
        fila = conn.execute("SELECT valor FROM contadores WHERE clave=?", (clave,)).fetchone()
        return fila[0] if fila else 0
    finally:
        conn.close()


def contador_leer(nombre, ventana=None, ventana_horas=None, **_):
    """Valor del contador en la ventana actual (0 si esa ventana no tiene nada)."""
    clave = _clave_contador(nombre, ventana, ventana_horas)
    conn = _conn_contadores()
    try:
        fila = conn.execute("SELECT valor FROM contadores WHERE clave=?", (clave,)).fetchone()
        return fila[0] if fila else 0
    finally:
        conn.close()


def contador_reset(nombre=None):
    conn = _conn_contadores()
    try:
        with conn:
            if nombre:
                conn.execute("DELETE FROM contadores WHERE clave LIKE ?", (f"{nombre}@%",))
            else:
                conn.execute("DELETE FROM contadores")
    finally:
        conn.close()


# --------------------------------------------------------- troceado de texto
_ENCABEZADO = _re2.compile(r"^(#{1,6})\s+(.*)$")


def _trocear(texto, markdown=True):
    """[(encabezado, texto)]. Respeta bloques ``` (un # dentro NO es titulo)
    y corta los parrafos gigantes sin perder nada."""
    secciones, enc, buf, en_codigo = [], "", [], False
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

    trozos = []
    for head, cuerpo in secciones:
        cuerpo = cuerpo.strip()
        if not cuerpo:
            continue
        for parrafo in _re2.split(r"\n\s*\n", cuerpo):
            parrafo = parrafo.strip()
            if not parrafo:
                continue
            if len(parrafo) <= CHUNK_CHARS:
                trozos.append((head, parrafo))
            else:
                for s in range(0, len(parrafo), CHUNK_CHARS):
                    trozos.append((head, parrafo[s:s + CHUNK_CHARS]))
    return trozos


def chunk_text(texto, markdown=True):
    """Lista de fragmentos (texto plano). Se conserva todo el contenido."""
    return [cuerpo for _, cuerpo in _trocear(texto, markdown)]


def chunk_con_encabezado(texto, markdown=True):
    """Igual, pero [(encabezado, texto)] para el indexador."""
    return _trocear(texto, markdown)


# --------------------------------------------------------------- formateo
def _recortar_texto(t, limite):
    t = (t or "").strip()
    return t if len(t) <= limite else t[:limite].rstrip() + " [...]"


def formatear(resultados, notas=None):
    """Texto legible para el LLM, acotado por resultado y en total.
    Acepta resultados con 'similitud' o 'score', y notas opcionales."""
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


globals().setdefault("trocear", _trocear)

import sqlite3

def connect():
    """
    Conexion compatible con guardian.py
    """
    ruta = _ruta_db()
    ruta.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(
        str(ruta),
        timeout=30,
        check_same_thread=False,
    )

    try:
        conn.execute("PRAGMA journal_mode=WAL")
    except Exception:
        pass

    return conn

if __name__ == "__main__":
    _main()
