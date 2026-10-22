---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/docs/sn-data-analysis.md"
tags: [hecho]
---
# sn-data-analysis.md

## Resumen
Este documento define un conjunto de habilidades para el análisis de datos que automatiza la limpieza, agregación y exportación de archivos Excel multi-hoja. Además, permite el procesamiento eficiente de grandes volúmenes de datos mediante optimizaciones de memoria y la extracción de información estructurada a partir de imágenes o gráficos.

## Datos clave
- **Proyecto**: SenseNova Skills (análisis de datos).
- **Tecnologías**: Python 3.9+, pandas, openpyxl, pyarrow, matplotlib, numpy.
- **Habilidades principales**: `sn-da-excel-workflow` (orquestador), `sn-da-image-caption` (extracción visual), `sn-da-large-file-analysis` (alto rendimiento).
- **Lógica de enrutamiento**: Archivos con ≥10k filas activan optimización Parquet; ≥100k filas derivan a la habilidad de análisis masivo.
- **Requisitos especiales**: La habilidad de imágenes requiere credenciales de API VLM (`VISION_API_KEY`).
- **Entrada**: Se invoca desde OpenClaw proporcionando el archivo y una descripción del objetivo o llamando directamente al nombre del skill.

## Etiquetas
#análisis-de-datos #excel-python #automatización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\docs\sn-data-analysis.md`
