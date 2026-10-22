---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-reading/single-sheet-reading/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define un flujo de trabajo en Python para leer, limpiar y analizar datos de una sola hoja de Excel. Su objetivo es facilitar la extracción de métricas clave mediante limpieza avanzada, clasificación automática y generación de visualizaciones de alta resolución listas para descargar.

## Datos clave
- **Proyecto**: `sn-da-excel-workflow` (módulo de lectura de hojas simples).
- **Tecnologías**: Python, Pandas, NumPy, Matplotlib, Seaborn, IPython.
- **Decisiones técnicas**: Uso de fuentes SimHei y WenQuanYi para evitar caracteres chinos rotos; conversión a Parquet para archivos grandes; exportación CSV codificada en Base64 para enlaces de descarga directa.
- **Pasos críticos**: Normalización de nombres de columnas, limpieza con expresiones regulares para extraer números, algoritmo de puntuación basado en umbrales (A/B/C), y generación de gráficos de barras con DPI=300.

## Etiquetas
#Python #DataCleaning #ExcelAnalysis #Visualization

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-reading\single-sheet-reading\SKILL.md`
