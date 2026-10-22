# Parche: aprender.py

## 1. Recorte cabeza+cola

```python
def recortar(texto: str, limite: int) -> tuple[str, bool]:
    if len(texto) <= limite:
        return texto, False
    mitad = limite // 2
    return (f"{texto[:mitad]}\n\n[...recorte de {len(texto) - limite} caracteres...]\n\n{texto[-mitad:]}", True)
```

Usalo donde hoy haces `texto[:MAX_CHARS]`.

## 2. Constantes desde config

```python
MAX_CHARS   = int(config.get("aprender.max_chars", 6000))
MAX_TOKENS  = int(config.get("aprender.max_tokens", 1500))
MAX_INTENTOS = int(config.get("aprender.max_intentos", 3))
PAUSA       = float(config.get("aprender.pausa", 0.5))
TIMEOUT     = float(config.get("aprender.timeout", 900))
MAX_SIN_CONEXION = int(config.get("aprender.sin_conexion_seg", 1800))
APRENDER_EXT = set(config.get("aprender.extensiones", [".md", ".txt"]))
EXCLUIR     = set(config.get("aprender.excluir", []))
```

## 3. Chat via llm.py

```python
import llm
SISTEMA = llm.prompt("aprender", SISTEMA_POR_DEFECTO)
# ...
texto = llm.chat(SISTEMA, prompt, modelo=args.model, max_tokens=MAX_TOKENS,
                 temperature=0.2, timeout=TIMEOUT, etapa="aprender", etiqueta=rel)
# y donde capturabas memoria.ConexionError -> llm.SinConexion
```

## 4. Validacion de la nota

```python
    if len(contenido) < 40 or "## Resumen" not in contenido or "## Etiquetas" not in contenido:
        raise ValueError("nota incompleta")
```

## 5. Hash por (mtime, size)

En `pendientes()`, antes de hashear:

```python
        info = estado.get(rel) or {}
        if info.get("ok") and info.get("size") == p.stat().st_size \
           and info.get("mtime") == int(p.stat().st_mtime):
            continue
```

## 6. escribir_nota con frontmatter completo

Titulo `# {Path(rel).stem}`, fuente en wikilink, y frontmatter con `origen: local`,
`tipo`, `confianza` desde `reglas.json`, `estado: sin-revisar`, `repasar`,
`generador: aprender.py@<version>`, `generado: true`.

## 7. indexar_archivo devuelve -1

```python
    n = memoria.indexar_archivo(destino)
    if n < 0:
        print("   indice de otro modelo: lanza `python indexer.py` una vez")
```

## 8. --check y --dry-run

Al inicio del main, `--check` delega en `config.main(["--check"])`.
