# Parche: indexer.py

## 1. --watch con parada limpia

Sustituye el bucle de `--watch`:

```python
if args.watch:
    parar_idx = memoria.STOP_PATH.with_name("STOP_INDEXER")
    print(f"[watch] vigilando cada {args.watch}s. Crea {parar_idx.name} para salir.")
    while not memoria.parado():
        try:
            r = memoria.sync()
        except Exception as e:
            incidencias.registrar("indice", type(e).__name__, "media", str(e)[:200])
            r = {}
        if r and any(r.get(k) for k in ("nuevos", "modificados", "eliminados")):
            print(f"[watch] +{r.get('nuevos',0)} ~{r.get('modificados',0)} -{r.get('eliminados',0)}"
                  + (" (parcial)" if r.get("parcial") else ""))
            tablero.actualizar_si_toca()
        time.sleep(args.watch)
    print("[watch] salida limpia.")
    return 0
```

Imports nuevos: `incidencias`, `tablero`.

## 2. --eval para calibrar MIN_SIM

Anyade `--eval JSON` y `--k N` al argparse, y la funcion `evaluar(ruta_json, k)` que
prueba umbrales de 0.25 a 0.65 y reporta recall y precision.

Formato de `Sistema\eval.json`:

```json
[
  { "consulta": "como configuro el lock de sqlite", "esperado": "memoria" },
  { "consulta": "hooks de react con dependencias",   "esperado": "react" }
]
```

## 3. --check

Al inicio del main:

```python
    if "--check" in sys.argv:
        import config
        return config.main(["--check"])
```
