---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-non-spreadsheet-analysis/capability/word-analysis/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento detalla una metodología para el análisis exhaustivo de archivos Word (.docx y .doc), permitiendo la extracción de texto, tablas estructuradas y metadatos visuales como colores y resaltados. Su objetivo es facilitar la comparación entre múltiples documentos y la generación automática de descripciones para imágenes incrustadas mediante scripts externos.

## Datos clave
- **Tecnologías**: `python-docx`, `pandas`, `lxml`, `subprocess` (LibreOffice), `zipfile`.
- **Conversión**: Los archivos `.doc` antiguos se convierten a `.docx` usando `libreoffice --headless` antes del procesamiento.
- **Extracción de formato**: Se accede al nivel XML (`w:rPr`, `w:highlight`, `w:shd`) para leer colores de fondo y resaltados de texto específicos (ej. amarillo).
- **Imágenes**: Las imágenes incrustadas se extraen desde el archivo ZIP interno del `.docx` y se procesan con un script externo (`caption.py`).
- **Rutas**: Se asume una estructura de directorios como `/mnt/data/` para la entrada de archivos.

## Etiquetas
#procesamiento-de-documentos #python-docx #extracción-de-datos #automatización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-non-spreadsheet-analysis\capability\word-analysis\SKILL.md`
