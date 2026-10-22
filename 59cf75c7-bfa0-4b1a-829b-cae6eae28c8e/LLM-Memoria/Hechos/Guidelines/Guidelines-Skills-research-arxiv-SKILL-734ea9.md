---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/research/arxiv/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía describe cómo buscar y recuperar artículos académicos de arXiv utilizando su API REST gratuita sin necesidad de claves ni dependencias complejas. Proporciona comandos `curl` para consultas básicas, scripts en Python para parsear XML y generar formatos como BibTeX, así como instrucciones para extraer contenido completo mediante herramientas web.

## Datos clave
- **Proyecto**: Skill `arxiv` del agente Hermes (versión 1.0.0).
- **Tecnologías**: Bash (`curl`, `grep`, `sed`), Python 3 (`xml.etree.ElementTree`), scripts personalizados (`scripts/search_arxiv.py`).
- **Comandos principales**:
  - Búsqueda: `curl "https://export.arxiv.org/api/query?search_query=all:QUERY&max_results=5"`.
  - Obtención por ID: `curl "https://export.arxiv.org/api/query?id_list=ID"`.
  - Extracción web: `web_extract(urls=["..."])` para abstracts o PDFs.
- **Sintaxis de búsqueda**: Prefijos como `all:`, `ti:`, `au:`, `cat:` y operadores booleanos (`+`, `OR`, `ANDNOT`).
- **Parámetros API**: `sortBy` (relevance, submittedDate), `sortOrder`, `start`, `max_results`.
- **Categorías comunes**: `cs.AI`, `cs.CL`, `cs.CV`, `cs.LG`, `stat.ML`.

## Etiquetas
#arxiv #investigación_académica #python #bash #machine_learning

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\research\arxiv\SKILL.md`
