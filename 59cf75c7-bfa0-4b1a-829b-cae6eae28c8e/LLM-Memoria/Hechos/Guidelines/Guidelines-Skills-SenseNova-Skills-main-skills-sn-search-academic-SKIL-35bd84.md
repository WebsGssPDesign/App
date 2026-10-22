---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-search-academic/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define la habilidad `sn-search-academic`, diseñada para automatizar investigaciones académicas, lectura de papers y trazado de referencias. Sirve como guía operativa para ejecutar scripts que buscan en múltiples fuentes (arXiv, Semantic Scholar, etc.), extraen contenido específico de artículos y construyen árboles de citas utilizando credenciales gestionadas vía variables de entorno.

## Datos clave
- **Scripts principales**: `search.py` (búsqueda), `paper.py` (lectura de secciones/contenido), `refTree.py` (referencias/citas).
- **Configuración**: Credenciales (API keys, tokens) deben ir en `.env`; no escribir claves en payloads o logs.
- **Entornos necesarios**: Python 3 (`pip install -r requirements.txt`) y Playwright (`playwright install firefox`). Algunos crawlers requieren Node.js con `camoufox-js`.
- **Convenios de ejecución**: No iniciar scripts en paralelo; usar `--output <path>` para resultados grandes.
- **Fuentes soportadas**: arxiv, semantic, google_scholar, pubmed, ssrn, wikipedia.
- **Formato de salida**: JSON estructurado con campos como `success`, `source_results[*].items` y detalles específicos por fuente (ej. `arxiv_id`, `paper_id`).

## Etiquetas
#investigación_académica #automatización #python_scripts #papers

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-search-academic\SKILL.md`
