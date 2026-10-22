# Parche: crear_skills.py

## 1. Escritura segura con .tmp

```python
def escribir_skill(nombre: str, contenido: str, forzar: bool = False) -> bool:
    d = SKILLS_DIR / nombre
    if d.exists():
        if not forzar:
            return False
        objetivo = d / "SKILL.md"
        if objetivo.exists():
            objetivo.replace(objetivo.with_suffix(".md.bak"))
    d.mkdir(parents=True, exist_ok=True)
    tmp = d / "SKILL.md.tmp"
    try:
        tmp.write_text(contenido, encoding="utf-8")
        os.replace(tmp, d / "SKILL.md")
    except OSError:
        tmp.unlink(missing_ok=True)
        if not any(d.iterdir()):
            d.rmdir()
        return False
    return True
```

## 2. --regenerar

Anyade el flag y pasalo a `escribir_skill(nombre, contenido, forzar=args.regenerar)`.

## 3. Validar las 6 secciones

```python
    faltan = [s for s in config.get("skills.secciones", []) if s not in txt]
    if len(txt) < 200 or faltan:
        raise ValueError(f"faltan secciones: {faltan}")
```

## 4. Constantes desde config

`MAX_POR_CORRIDA`, `MIN_MATERIAL`, `RONDAS_VACIAS`, `MAX_TOKENS` desde `config.get("skills.*")`.

## 5. Chat via llm.py

`llm.prompt("skills_candidatos")` y `llm.prompt("skills_cuerpo")`.

## 6. Fuentes en wikilink

`escritor.wikilink(f)` en lugar de `- {f}`.

## 7. Reintento de saltadas

Guarda `saltadas[nombre] = {"motivo": ..., "fecha": ...}` y permite reintentar tras
`config.get("skills.reintentar_dias")` dias.

## 8. except limpio

`except (memoria.EmbeddingError, Exception)` es redundante: deja `except Exception as e`.
