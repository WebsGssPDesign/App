---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/productivity/ocr-and-documents/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía detalla estrategias para extraer texto de PDFs y documentos escaneados, priorizando la conversión remota cuando es posible. Establece criterios claros para elegir entre extractores ligeros como `pymupdf` o herramientas avanzadas con OCR como `marker-pdf`, además de ofrecer comandos para manipular archivos.

## Datos clave
- **Proyecto**: Skill de productividad para extracción de documentos (versión 2.3.0).
- **Tecnologías**: `pymupdf`, `marker-pdf`, `python-docx`, `web_extract` (Firecrawl), `python-pptx`.
- **Decisiones**: Usar `web_extract` primero para URLs; elegir `pymupdf` por defecto salvo que se necesite OCR, ecuaciones o análisis de layout complejo.
- **Rutas y comandos**:
  - Instalación: `pip install pymupdf pymupdf4llm`, `pip install marker-pdf`.
  - Extracción local: `python scripts/extract_pymupdf.py document.pdf --markdown` o `python scripts/extract_marker.py scanned.pdf`.
  - Manipulación: Scripts de Python para dividir, fusionar y buscar texto dentro de PDFs usando `pymupdf`.

## Etiquetas
#OCR #PDF #ExtracciónDeTexto #Automatización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\productivity\ocr-and-documents\SKILL.md`
