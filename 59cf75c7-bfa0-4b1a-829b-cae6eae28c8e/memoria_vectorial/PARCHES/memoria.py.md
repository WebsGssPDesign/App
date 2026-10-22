# Parche: memoria.py

Nueve cambios. Ninguno altera firmas publicas.

## 0. Imports y constantes

Anade a los imports:

```python
import contextlib
import shutil

import config
import incidencias
from util import proceso_vivo
```

Sustituye el bloque de constantes por:

```python
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

_ultimo_sync = {"t": 0.0}
```

Anade tambien:

```python
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
```

## 1. connect() con busy_timeout

```python
def connect() -> sqlite3.Connection:
    ESTADO_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH, timeout=30.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode = WAL")
    conn.execute("PRAGMA synchronous = NORMAL")
    conn.execute("PRAGMA busy_timeout = 30000")
    _crear_esquema(conn)
    return conn
```

## 2. Tabla contadores + funciones

En `_crear_esquema()`, al final:

```python
    conn.execute("CREATE TABLE IF NOT EXISTS contadores (k TEXT PRIMARY KEY, v INTEGER, ts REAL)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_contadores_ts ON contadores(ts)")
```

Y las funciones `contador_sumar(clave, n=1, ventana_horas=1)` y
`contador_leer(clave, ventana_horas=1)`. Sobreviven a `_wipe()` porque este solo borra
`files`, `chunks`, `chunks_fts` y `meta`.

## 3. Lock con propiedad

Reemplaza `_acquire_lock` y `_release_lock` por las versiones con `_lock_pid()`,
`_lock_es_nuestro()`, `_lock_viejo_y_ajeno()` y `_refrescar_lock()`.

Puntos clave:
- el lock guarda `"<pid> <timestamp>"`
- no se libera si el pid no es el propio
- no se roba si el duenno sigue vivo, aunque el mtime sea viejo

## 4. embed() con reintento por lote

Renombra el cuerpo actual a `_embed_una_vez(texts, tipo)`, anyade `_embed_lote` con
`llm.reintentos` intentos y backoff, y que `embed()` itere por lotes llamando a `_embed_lote`.

## 5. indexar_archivo devuelve -1

```python
    fila = conn.execute("SELECT v FROM meta WHERE k='doc_prefix'").fetchone()
    if fila and fila[0] != EMBED_DOC_PREFIX:
        return -1
    fila = conn.execute("SELECT v FROM meta WHERE k='modelo'").fetchone()
    if fila and fila[0] != MODELO_EMBED:
        return -1
```

## 6. sync() con .bak, refresco y presupuesto

Anyade `_hay_filas(conn)` y reescribe `sync(max_segundos=None, forzar=False)` con:
- copia a `indice.sqlite.bak` antes de `_wipe`
- `_refrescar_lock()` cada 50 archivos
- corte por presupuesto con `resumen["parcial"] = True`
- `incidencias.registrar("indice", ...)` en los errores de embedding

## 7. search() con min_sim

```python
def search(consulta: str, k: int = 5, ambito: str = "todo",
           auto_sync: bool = True, min_sim: float | None = None) -> list[dict]:
    umbral = MIN_SIM if min_sim is None else float(min_sim)
    if auto_sync:
        sync(max_segundos=MAX_SYNC_SEGUNDOS)
```

## 8. formatear() con truncado

Trunca a `MAX_CARACTERES_RESULTADO` por bloque y `MAX_CARACTERES_TOTAL` en total.

## 9. parado()

```python
def parado() -> bool:
    return STOP_PATH.exists() or STOP_INDEXER.exists() or (MEM_DIR / "STOP").exists()
```

## No se toca

`chunk_text` esta bien: respeta bloques de codigo y no confunde `#` con encabezado.
`prefijo()` para qwen3 tambien: `Instruct: {t}\nQuery:` sin espacio es el formato oficial.
Documentalo en un comentario para que nadie lo "arregle".
