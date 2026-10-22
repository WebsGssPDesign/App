---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-reading/specific-sheet-reading/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe un flujo de trabajo automatizado para analizar archivos Excel con múltiples hojas. El sistema evalúa dinámicamente el volumen de datos, realiza limpieza y análisis estadístico avanzado (como tablas cruzadas), genera visualizaciones y exporta los resultados en un archivo único con enlaces de descarga.

## Datos clave
- **Proyecto**: `sn-da-excel-workflow` (módulo `excel-reading`).
- **Tecnologías**: Python, Pandas (`openpyxl`, `matplotlib`, `seaborn`), IPython.
- **Pasos principales**:
  1. Iteración sobre todas las hojas para contar ocurrencias de patrones específicos (ej. tipo 'varchar').
  2. Limpieza de datos: manejo de celdas fusionadas (`ffill`), extracción numérica con regex y mapeo de categorías.
  3. Cálculo de puntuaciones multidimensionales y generación de tablas de contingencia (`crosstab`).
  4. Visualización de barras con etiquetas optimizadas y configuración de fuentes (SimHei).
- **Salida**: Archivo Excel timestampado (`analysis_result_...xlsx`) con pestañas para resumen, detalles, estadísticas y análisis cruzado, seguido de un enlace HTML de descarga.

## Etiquetas
#Python #ExcelAnalysis #DataCleaning #Visualization

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-reading\specific-sheet-reading\SKILL.md`
