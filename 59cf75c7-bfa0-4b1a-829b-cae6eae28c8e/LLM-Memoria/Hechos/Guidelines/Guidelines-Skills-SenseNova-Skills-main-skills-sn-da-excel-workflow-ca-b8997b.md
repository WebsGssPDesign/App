---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-table-styling/table-theme-styling/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía define un flujo de trabajo en Python para analizar archivos Excel masivos, optimizando la lectura mediante conversión a Parquet cuando el volumen supera las 10.000 filas. El proceso permite filtrar datos por valores específicos y generar resúmenes estadísticos con totales y porcentajes antes de exportar los resultados.

## Datos clave
- **Proyecto**: sn-da-excel-workflow (capacidad de estilización y análisis).
- **Tecnologías**: Python, pandas (`pd.read_parquet`, `pd.read_excel`), lógica condicional global.
- **Decisiones**: Uso automático de Parquet para archivos grandes; conversión a Excel para la exportación final.
- **Pasos importantes**:
  1. Verificar existencia del skill `da_large_file_analysis` para decidir entre lectura directa o vía Parquet.
  2. Filtrar filas que contengan un valor objetivo en una columna específica usando `str.contains`.
  3. Realizar agrupación (`value_counts`) y calcular porcentajes, añadiendo manualmente una fila de "总计" (Total).
  4. Guardar el DataFrame resultante como archivo Excel con índice desactivado.

## Etiquetas
#análisis-de-datos #excel-python #optimización-parquet #automatización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-table-styling\table-theme-styling\SKILL.md`
