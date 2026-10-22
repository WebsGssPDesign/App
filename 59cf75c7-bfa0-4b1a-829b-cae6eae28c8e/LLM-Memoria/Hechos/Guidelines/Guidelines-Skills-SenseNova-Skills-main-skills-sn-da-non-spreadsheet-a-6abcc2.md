---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-non-spreadsheet-analysis/capability/ppt-analysis/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe un conjunto de funciones en Python para el análisis exhaustivo de presentaciones PowerPoint (.pptx y .ppt). Su objetivo es extraer texto, tablas estructuradas, datos de gráficos y generar descripciones automáticas para diapositivas que solo contienen imágenes.

## Datos clave
- **Proyecto**: `sn-da-non-spreadsheet-analysis` (módulo `ppt-analysis`).
- **Tecnologías principales**: `python-pptx`, `pandas`, `subprocess` (para conversiones), `libreoffice`.
- **Flujo de trabajo**:
  1. Conversión automática de archivos `.ppt` antiguos a formato `.pptx` usando LibreOffice en modo headless.
  2. Extracción de texto plano, tablas y títulos de gráficos de todas las diapositivas.
  3. Recuperación de datos numéricos de series gráficas (categorías y valores).
  4. Para diapositivas sin texto extraíble, se renderizan como imágenes PNG para ser procesadas por un script de *captioning* externo (`caption.py`).
- **Comandos clave**: `subprocess.run(['libreoffice', '--headless', ...])`.

## Etiquetas
#análisis-de-presentaciones #extracción-de-datos #python-pptx #automatización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-non-spreadsheet-analysis\capability\ppt-analysis\SKILL.md`
