---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-cell-coloring/threshold-cell-coloring/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe una habilidad para automatizar el análisis de datos en Excel, detectando automáticamente si un archivo es grande para optimizar la lectura y generando informes con formato condicional. Sirve para identificar visualmente los periodos donde las métricas de un entidad específica caen por debajo del promedio histórico.

## Datos clave
- **Proyecto**: SenseNova-Skills (flujo de trabajo Excel).
- **Tecnologías**: Python, pandas, openpyxl.
- **Lógica principal**: El script cuenta las filas totales en todos los sheets; si el archivo es grande, activa una lectura acelerada con Parquet antes de procesar.
- **Pasos clave**:
  1. Leer y sumar filas para determinar la estrategia de carga.
  2. Extraer series temporales de un entidad objetivo (ej. 'Target_Entity') y calcular su promedio.
  3. Generar un nuevo Excel con estilos personalizados: encabezados azules, datos centrados y celdas verdes si el valor es menor al promedio.
- **Rutas**: Entrada `input_data.xlsx`, salida `output_report.xlsx`.

## Etiquetas
#Python #ExcelAutomation #DataAnalysis #OpenPyXL

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-cell-coloring\threshold-cell-coloring\SKILL.md`
