---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/docs/sn-data-analysis_cn.md"
tags: [hecho]
---
# sn-data-analysis_cn.md

## Resumen
Este documento describe un conjunto de habilidades para el análisis de datos, enfocadas en la automatización del flujo de trabajo con Excel, la extracción de información de imágenes y el procesamiento eficiente de archivos masivos. Su propósito es permitir a los usuarios delegar tareas complejas de limpieza, agregación y visualización mediante comandos simples o integración con agentes inteligentes.

## Datos clave
- **Proyecto**: SenseNova Skills (módulo `sn-data-analysis`).
- **Tecnologías**: Python 3.9+, pandas, openpyxl, pyarrow, matplotlib, numpy.
- **Decisión de arquitectura**: El flujo principal (`sn-da-excel-workflow`) detecta automáticamente el tamaño del archivo; si supera las 10k filas activa optimizaciones Parquet y delega a `sn-da-large-file-analysis` para archivos mayores a 100k filas.
- **Requisitos específicos**: La habilidad de imagen (`sn-da-image-caption`) requiere credenciales de API VLM configuradas en variables de entorno (`VISION_API_KEY`, `VISION_API_BASE`).
- **Comandos de uso**: Invocar habilidades mediante `/skill sn-da-excel-workflow` o descripciones naturales como "analiza este Excel".

## Etiquetas
#análisis-de-datos #excel #python #automatización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\docs\sn-data-analysis_cn.md`
