---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-cell-coloring/top-value-coloring/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento detalla una habilidad técnica para automatizar el análisis de datos en Excel mediante Python. Su objetivo es consolidar información de múltiples hojas, filtrar los valores más altos y generar un informe final con estilos visuales (colores y fuentes) aplicados dinámicamente usando la librería openpyxl.

## Datos clave
- **Proyecto**: SenseNova-Skills (flujo de trabajo Excel).
- **Tecnologías**: Python, pandas, openpyxl.
- **Pasos principales**:
  1. Lectura y limpieza de datos desde múltiples hojas (`Sheet1`, `Sheet2`).
  2. Fusión de datos y selección de los top 5 valores mediante `nlargest`.
  3. Creación de un nuevo archivo Excel con encabezados estilizados, bordes y resaltado condicional (ej. rojo para columnas específicas).
- **Comandos/Funciones clave**: `pd.read_excel`, `pd.concat`, `merged_df.nlargest(5)`, configuración de estilos en openpyxl (`PatternFill`, `Font`), generación de enlace de descarga con prefijo `sandbox:`.

## Etiquetas
#Python #AutomatizaciónExcel #DataAnalysis #openpyxl

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-cell-coloring\top-value-coloring\SKILL.md`
