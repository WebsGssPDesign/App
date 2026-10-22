---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-data-filtering/threshold-filtering/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe una habilidad para analizar datos en Excel, determinando estrategias de procesamiento según el volumen y ejecutando limpieza, filtrado por umbral y marcado visual. Sirve como paso específico dentro de un flujo de trabajo mayor para preparar y resaltar datos numéricos relevantes antes de la exportación final.

## Datos clave
- **Proyecto**: Flujo de trabajo de análisis de Excel (Skills/SenseNova).
- **Tecnologías**: Python, pandas, openpyxl.
- **Pasos importantes**:
  1. Leer todos los archivos y hojas para contar el total de filas y evaluar la escala.
  2. Limpiar columnas objetivo convirtiendo no numéricos en NaN y eliminando filas vacías.
  3. Filtrar registros donde una columna específica supere un umbral definido (ej. >10).
  4. Utilizar `openpyxl` para aplicar estilos a las celdas que cumplen los criterios en el archivo original.

## Etiquetas
#Python #ExcelAutomation #DataCleaning #ThresholdFiltering

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-data-filtering\threshold-filtering\SKILL.md`
