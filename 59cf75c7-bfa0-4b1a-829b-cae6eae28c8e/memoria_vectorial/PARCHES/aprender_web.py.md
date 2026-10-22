# Parche: aprender_web.py

## 1. arXiv con comillas

```python
tema_q = f'all:"{tema}"' if " " in tema.strip() else f"all:{tema.strip()}"
params = {"search_query": tema_q, "start": 0, "max_results": max(1, n)}
```

## 2. Wikipedia solo introduccion

```python
params = {"action": "query", "format": "json", "prop": "extracts",
          "explaintext": 1, "exintro": 1, "redirects": 1, "titles": tema}
```

## 3. GitHub con token

```python
CABECERAS_GH = {"Accept": "application/vnd.github+json"}
if (tok := os.environ.get("GITHUB_TOKEN")):
    CABECERAS_GH["Authorization"] = f"Bearer {tok}"
```

## 4. Indexado inmediato

```python
    ruta = guardar_nota(...)
    if ruta:
        memoria.indexar_archivo(f"{aprender.MEM_DIR.name}/Web/{rel}")
```

## 5. Triple filtro + navegador

Anyade `import navegador, perfil` y las funciones `prioridad(texto)`, `pasa_filtro(url, texto)`,
`temas_desde_sitemap()`, `aprender_url(fuente, url)`, `fuente_aislada()`, `anotar_fallo()`,
`anotar_exito()`, `temas_nuevos()`.

Cada candidato pasa: lista blanca -> robots -> relevancia -> prioridad.
Si falla, `navegador.descartar(url, motivo)` y sigue.

## 6. Aislamiento a los 5 fallos

```python
def anotar_fallo(fuente: str, error: str) -> None:
    incidencias.registrar(f"web:{fuente}", error, "baja", fuente)
    if incidencias.fallos_de(f"web:{fuente}") >= int(config.get("web.fallos_para_aislar", 5)):
        horas = int(config.get("web.horas_aislamiento", 24))
        incidencias.aislar(f"web:{fuente}", f"{horas}h por fallos repetidos", horas)
        eventos.emitir("web.fuente_aislada", {"fuente": fuente, "horas": horas})
```

## 7. Reintento de URLs fallidas

Guarda `estado["urls"][url] = {"ok": False, "intentos": n}` y reintenta hasta 3.

## 8. Deduplicacion semantica de temas

`temas_nuevos(candidatos, vistos, umbral=0.85)` usando `memoria.embed`.

## 9. Presupuesto

Antes de cada ciclo: `navegador.presupuesto_ok()`.
