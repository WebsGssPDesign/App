"""
Aprendizaje por lotes, dirigido por código (no por el LLM).

Recorre la bóveda archivo por archivo. Para cada uno le pide al LLM local UNA nota
corta y la guarda en LLM-Memoria\\Hechos\\<carpeta>\\. El LLM no usa herramientas ni
decide qué leer: solo resume lo que este script le entrega. Por eso no puede entrar en
bucles, inventar rutas ni borrar el inventario.

  python aprender.py --max 5                 prueba con 5 archivos y revisa la calidad
  python aprender.py                         procesa todo lo pendiente (reanudable)
  python aprender.py --model NOMBRE          elige el modelo de chat de LM Studio
  python aprender.py --max-minutes 480       se detiene solo tras 8 horas
  python aprender.py --status                cuántos archivos van y cuántos faltan
  python aprender.py --retry-failed          reintenta los archivos que fallaron

El estado queda en <bóveda>\\.memoria\\aprendido.json: si lo cortas, continúa donde quedó.
Las notas nuevas las vectoriza solas `python indexer.py --watch`.
"""
import argparse
import hashlib
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import memoria

VAULT = memoria.VAULT
MEM_DIR = Path(os.environ.get("MEMORIA_NOTAS", str(VAULT / "LLM-Memoria")))
HECHOS = MEM_DIR / "Hechos"
STATE_PATH = VAULT / ".memoria" / "aprendido.json"
STOP_PATH = VAULT / ".memoria" / "STOP"   # crea este archivo vacío para detener con calma
EXCLUIR = set(memoria.IGNORE_DIRS) | {
    ".venv", "venv", "memoria_vectorial", "_descartados", "__pycache__", MEM_DIR.name,
}
# El resumen por archivo se hace solo con documentos; el código se indexa tal cual (indexer.py).
APRENDER_EXT = {e.strip().lower() for e in os.environ.get("APRENDER_EXTENSIONS", ".md,.txt").split(",") if e.strip()}
MAX_CHARS = int(os.environ.get("APRENDER_MAX_CHARS", "6000"))   # texto que se le entrega al modelo
MAX_TOKENS = int(os.environ.get("APRENDER_MAX_TOKENS", "1500"))  # margen por si el modelo "piensa"
MAX_INTENTOS = 3                 # intentos por archivo antes de saltarlo
ESPERA_CONEXION = 60             # segundos entre reintentos si LM Studio no responde
MAX_SIN_CONEXION = 30 * 60       # tope total sin conexión antes de detenerse

SISTEMA = (
    "Eres un archivista técnico. Recibes el contenido de UN archivo y escribes una nota de memoria "
    "breve en español, con tus propias palabras. Máximo 250 palabras. Formato exacto:\n\n"
    "## Resumen\n<2 a 4 frases: de qué trata y para qué sirve>\n\n"
    "## Datos clave\n- <proyecto, tecnologías, decisiones, rutas, comandos o pasos importantes>\n\n"
    "## Etiquetas\n#etiqueta1 #etiqueta2 #etiqueta3\n\n"
    "Reglas: no copies bloques largos; no incluyas contraseñas, claves ni tokens; no inventes nada "
    "que no esté en el texto; responde SOLO con la nota, sin saludos ni explicaciones."
)


# --------------------------------------------------------------------------
def inventario():
    """{ruta_relativa: Path} de los archivos a aprender."""
    out = {}
    for raiz, dirs, archivos in os.walk(VAULT):
        dirs[:] = [d for d in dirs if d not in EXCLUIR]
        for nombre in archivos:
            p = Path(raiz) / nombre
            if p.suffix.lower() not in APRENDER_EXT:
                continue
            try:
                if not 0 < p.stat().st_size <= memoria.MAX_FILE_BYTES:
                    continue
            except OSError:
                continue
            out[p.relative_to(VAULT).as_posix()] = p
    return dict(sorted(out.items()))


def cargar_estado():
    try:
        return json.loads(STATE_PATH.read_text(encoding="utf-8")).get("archivos", {})
    except (OSError, ValueError):
        return {}


def guardar_estado(estado):
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps({"archivos": estado}, ensure_ascii=False, indent=1), encoding="utf-8")
    os.replace(tmp, STATE_PATH)


def modelo_chat(arg):
    m = (arg or os.environ.get("LLM_MODEL", "")).strip()
    if m:
        return m
    ids = [x.get("id", "") for x in memoria._http("GET", "/models").get("data", [])]
    candidatos = [i for i in ids if "embed" not in i.lower()]
    if not candidatos:
        raise memoria.EmbeddingError("LM Studio no muestra ningún modelo de chat cargado.")
    if len(candidatos) > 1:
        print("Modelos de chat disponibles:", ", ".join(candidatos))
        print(f"Se usará '{candidatos[0]}'. Para otro: python aprender.py --model NOMBRE")
    return candidatos[0]


def pedir_nota(modelo, rel, texto, recortado):
    usuario = (
        f"Archivo: {rel}\n\nContenido{' (recortado)' if recortado else ''}:\n<<<\n{texto}\n>>>"
    )
    data = memoria._http(
        "POST",
        "/chat/completions",
        {
            "model": modelo,
            "messages": [{"role": "system", "content": SISTEMA}, {"role": "user", "content": usuario}],
            "temperature": 0.2,
            "max_tokens": MAX_TOKENS,
            "chat_template_kwargs": {"enable_thinking": False},
        },
        timeout=900,
    )
    contenido = (data["choices"][0]["message"].get("content") or "")
    contenido = re.sub(r"<think>.*?</think>", "", contenido, flags=re.S)
    contenido = contenido.split("<think>")[0].strip()  # razonamiento cortado sin cerrar
    if len(contenido) < 40:
        raise ValueError("el modelo devolvió una nota vacía o demasiado corta")
    if "## Resumen" not in contenido:
        contenido = "## Resumen\n" + contenido
    return contenido


def ruta_nota(rel):
    partes = rel.split("/")
    carpeta = re.sub(r'[<>:"/\\|?*]+', "-", partes[0] if len(partes) > 1 else "raiz")
    slug = re.sub(r"[^\w]+", "-", Path(rel).with_suffix("").as_posix(), flags=re.U).strip("-")[:70] or "nota"
    sello = hashlib.sha1(rel.encode("utf-8")).hexdigest()[:6]
    return HECHOS / carpeta / f"{slug}-{sello}.md"


def escribir_nota(rel, nota):
    destino = ruta_nota(rel)
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(
        "---\n"
        f"fecha: {datetime.now():%Y-%m-%d}\n"
        "etapa: aprendizaje\n"
        f'fuente: "{rel}"\n'
        "tags: [hecho]\n"
        "---\n"
        f"# {Path(rel).name}\n\n{nota}\n\nFuente: `{VAULT / rel}`\n",
        encoding="utf-8",
    )
    return destino.relative_to(VAULT).as_posix()


def escribir_progreso(inv, estado):
    """Genera LLM-Memoria\\Progreso.md (solo lo escribe este script; nadie más)."""
    try:
        hechos = [r for r in inv if estado.get(r, {}).get("ok")]
        fallidos = [r for r in inv if estado.get(r) and not estado[r].get("ok") and estado[r].get("fallos", 0) >= MAX_INTENTOS]
        lineas = ["# Progreso de aprendizaje", "", "_Generado automáticamente por aprender.py. No editar a mano._", "",
                  f"- Archivos a aprender: {len(inv)}", f"- Con nota: {len(hechos)}",
                  f"- Fallidos: {len(fallidos)}", f"- Pendientes: {len(inv) - len(hechos) - len(fallidos)}",
                  f"- Actualizado: {datetime.now():%Y-%m-%d %H:%M}", ""]
        if fallidos:
            lineas += ["## Fallidos", ""] + [f"- `{r}`: {estado[r].get('error', '')}" for r in fallidos] + [""]
        MEM_DIR.mkdir(parents=True, exist_ok=True)
        (MEM_DIR / "Progreso.md").write_text("\n".join(lineas), encoding="utf-8")
    except OSError:
        pass


def indexar_nota(destino):
    """Deja la nota buscable al instante. Si falla (p. ej. el modelo de embeddings no está
    cargado) no pasa nada: indexer.py la tomará después."""
    try:
        memoria.indexar_archivo(destino)
    except Exception as e:  # noqa: BLE001
        print(f"   (aviso: no se pudo indexar al instante: {str(e)[:80]})")


def registrar_sesion(texto):
    """Agrega una línea al registro del día (solo agrega, como pide la memoria)."""
    try:
        d = MEM_DIR / "Sesiones"
        d.mkdir(parents=True, exist_ok=True)
        f = d / f"{datetime.now():%Y-%m-%d}.md"
        if not f.exists():
            f.write_text(f"---\nfecha: {datetime.now():%Y-%m-%d}\netapa: aprendizaje\n---\n# Sesión\n", encoding="utf-8")
        with f.open("a", encoding="utf-8") as fh:
            fh.write(f"\n- {datetime.now():%H:%M} aprender.py: {texto}\n")
    except OSError:
        pass


# --------------------------------------------------------------------------
def pendientes(inv, estado, reintentar):
    """Lista [(rel, path, digest)] de archivos nuevos, cambiados o (opcional) fallidos."""
    lista, omitidos_fallo = [], 0
    for rel, p in inv.items():
        try:
            digest = hashlib.sha256(p.read_bytes()).hexdigest()
        except OSError:
            continue
        e = estado.get(rel)
        if e and e.get("hash") == digest:
            if e.get("ok"):
                continue
            if e.get("fallos", 0) >= MAX_INTENTOS and not reintentar:
                omitidos_fallo += 1
                continue
        lista.append((rel, p, digest))
    return lista, omitidos_fallo


def mostrar_estado():
    inv = inventario()
    estado = cargar_estado()
    hechos = sum(1 for r in inv if estado.get(r, {}).get("ok"))
    fallidos = sum(1 for r in inv if estado.get(r) and not estado[r].get("ok") and estado[r].get("fallos", 0) >= MAX_INTENTOS)
    print(f"Archivos a aprender: {len(inv)}")
    print(f"Con nota: {hechos}  |  Fallidos: {fallidos}  |  Pendientes o cambiados: {len(inv) - hechos - fallidos}")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="Aprendizaje por lotes de la bóveda")
    ap.add_argument("--max", type=int, default=0, metavar="N", help="procesar como máximo N archivos")
    ap.add_argument("--max-minutes", type=float, default=0, metavar="M", help="detenerse tras M minutos")
    ap.add_argument("--model", help="modelo de chat de LM Studio (por defecto: el primero que no sea de embeddings)")
    ap.add_argument("--status", action="store_true", help="mostrar avance")
    ap.add_argument("--retry-failed", action="store_true", help="reintentar archivos fallidos")
    args = ap.parse_args()

    if not VAULT.is_dir():
        print(f"Error: la bóveda no existe: {VAULT}", file=sys.stderr)
        return 1
    if args.status:
        mostrar_estado()
        return 0

    try:
        modelo = modelo_chat(args.model)
    except memoria.EmbeddingError as e:
        print("Error:", e, file=sys.stderr)
        return 1

    inv = inventario()
    estado = cargar_estado()
    lista, omitidos = pendientes(inv, estado, args.retry_failed)
    if args.max:
        lista = lista[: args.max]
    print(f"Bóveda: {VAULT}\nModelo: {modelo}\nPor procesar: {len(lista)} de {len(inv)} archivos"
          + (f" ({omitidos} omitidos por fallos; usa --retry-failed)" if omitidos else ""))

    inicio, ok, fallos, sin_conexion = time.time(), 0, 0, 0
    detenido = False
    try:
        for n, (rel, p, digest) in enumerate(lista, 1):
            if args.max_minutes and (time.time() - inicio) / 60 >= args.max_minutes:
                print("Tiempo máximo alcanzado.")
                break
            if STOP_PATH.exists():
                print("Archivo STOP detectado: me detengo. El avance está guardado.")
                break
            e = estado.get(rel, {})
            intentos = e.get("fallos", 0) if e.get("hash") == digest else 0
            while True:  # se repite solo mientras LM Studio no responde
                t0 = time.time()
                try:
                    texto = p.read_text(encoding="utf-8", errors="replace").strip()
                    if len(texto) < 20:
                        estado[rel] = {"hash": digest, "ok": True, "nota": None, "fecha": f"{datetime.now():%F}"}
                        print(f"[{n}/{len(lista)}] {rel}: vacío, se omite")
                        break
                    nota = pedir_nota(modelo, rel, texto[:MAX_CHARS], len(texto) > MAX_CHARS)
                    destino = escribir_nota(rel, nota)
                    indexar_nota(destino)
                    estado[rel] = {"hash": digest, "ok": True, "nota": destino, "fecha": f"{datetime.now():%F}"}
                    ok += 1
                    sin_conexion = 0
                    print(f"[{n}/{len(lista)}] {rel} -> ok ({time.time() - t0:.0f} s)")
                    break
                except memoria.ConexionError as err:
                    # No es culpa del archivo: no cuenta intento; se espera y se reintenta.
                    if STOP_PATH.exists():
                        detenido = True
                        break
                    if sin_conexion >= MAX_SIN_CONEXION:
                        print("LM Studio lleva 30 min sin responder: me detengo. El avance está guardado.")
                        detenido = True
                        break
                    print(f"[{n}/{len(lista)}] LM Studio no responde; reintento en {ESPERA_CONEXION} s...")
                    time.sleep(ESPERA_CONEXION)
                    sin_conexion += ESPERA_CONEXION
                    continue
                except (memoria.EmbeddingError, ValueError, KeyError, IndexError, OSError) as err:
                    intentos += 1
                    msg = str(err)[:200]
                    if intentos >= MAX_INTENTOS:
                        estado[rel] = {"hash": digest, "ok": False, "fallos": intentos, "error": msg}
                        fallos += 1
                        print(f"[{n}/{len(lista)}] {rel} -> FALLÓ {intentos} veces, se salta: {msg[:120]}")
                        break
                    print(f"[{n}/{len(lista)}] {rel} -> intento {intentos}/{MAX_INTENTOS} falló: {msg[:100]}")
                    continue
            guardar_estado(estado)
            if detenido:
                break
            if n % 10 == 0:
                escribir_progreso(inv, estado)
    except KeyboardInterrupt:
        print("\nInterrumpido: el avance ya está guardado.")
    finally:
        guardar_estado(estado)
        escribir_progreso(inv, estado)

    resumen = f"{ok} notas nuevas, {fallos} fallos, {(time.time() - inicio) / 60:.1f} min"
    print("Resumen:", resumen)
    if ok or fallos:
        registrar_sesion(resumen)
    mostrar_estado()
    return 2 if detenido else 0


if __name__ == "__main__":
    sys.exit(main())
