---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-search-academic/references/paper.md"
tags: [hecho]
---
# paper.md

## Resumen
Este documento describe `paper.py`, un script de Python que actúa como entrada unificada para leer y procesar el contenido completo o secciones específicas de artículos académicos. Su función principal es orquestar múltiples proveedores (como arXiv y PMC) mediante una cadena de reintentos, devolviendo siempre un formato JSON consistente para facilitar la integración con modelos de lenguaje.

## Datos clave
- **Proyecto**: `SenseNova-Skills` (módulo `sn-search-academic`).
- **Tecnologías**: Python 3, CLI, JSON output.
- **Decisiones de diseño**: Implementación de una cadena de reintentos (*fallback chain*) para arXiv (`arxiv_html` -> `deepxiv` -> `pdf`) y PMC; normalización automática de IDs antes de llamar a los proveedores internos.
- **Comandos principales**:
  - Leer全文: `python3 scripts/paper.py <ID>`
  - Leer sección: `--section <nombre>`
  - Listar secciones: `--list_section`
  - Guardar archivo: `--output <ruta>`
- **Formato de salida**: JSON estructurado con campos como `success`, `content`, `attempts` (historial de proveedores) y metadatos específicos según la fuente (`title`, `pmid`, etc.).

## Etiquetas
#SenseNova #Python #AcademicSearch #CLI #JSON

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-search-academic\references\paper.md`
