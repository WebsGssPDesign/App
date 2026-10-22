---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-cell-coloring/category-coloring/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía describe un flujo de trabajo automatizado para analizar archivos Excel grandes (más de 10.000 filas). Su objetivo es mejorar el rendimiento convirtiendo los datos a formato Parquet, extraer métricas específicas y generar un reporte final donde la fila con el valor máximo está resaltada en verde.

## Datos clave
- **Proyecto**: SenseNova-Skills (sn-da-excel-workflow)
- **Tecnologías**: Python, pandas, openpyxl
- **Decisiones**: Se activa la conversión a Parquet solo si las filas totales superan 10.000 para optimizar la lectura.
- **Pasos importantes**:
    1. Leer todos los sheets y sumar filas usando `usecols=[0]` para velocidad.
    2. Cargar el archivo `.parquet`, identificar la fila del indicador objetivo y calcular el máximo.
    3. Crear un nuevo Excel, escribir resultados y aplicar fondo verde (`PatternFill`) a la celda correspondiente al valor máximo antes de guardar.

## Etiquetas
#análisis-de-datos #excel-python #optimización-parquet

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-cell-coloring\category-coloring\SKILL.md`
