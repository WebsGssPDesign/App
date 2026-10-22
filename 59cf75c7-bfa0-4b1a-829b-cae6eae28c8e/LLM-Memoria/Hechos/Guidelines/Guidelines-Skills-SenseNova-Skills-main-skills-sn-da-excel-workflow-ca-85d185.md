---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-data-analysis/comparison-analysis/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe un flujo de trabajo en Excel para realizar análisis comparativos entre dos categorías de datos. El proceso permite contar registros, calcular diferencias y proporciones, y generar visualizaciones gráficas (barras y pastel) junto con un informe final exportable.

## Datos clave
- **Proyecto**: Flujo de trabajo de análisis de datos en Excel (SenseNova).
- **Tecnologías**: Python, Pandas (`read_excel`, `ExcelWriter`), Matplotlib.
- **Pasos principales**:
  1. Contar filas totales en todas las hojas para evaluar tamaño del archivo.
  2. Limpiar datos: rellenar celdas fusionadas (`ffill`) y eliminar valores nulos o marcadores de cabecera ("代码").
  3. Calcular conteos, diferencias absolutas y porcentajes relativos.
  4. Generar gráficos (barras y pastel) con configuración de fuente china ('SimHei').
  5. Exportar resultados a un archivo `.xlsx` y mostrar enlace de descarga.

## Etiquetas
#análisis-de-datos #python-pandas #visualización-gráfica #excel-workflow

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-data-analysis\comparison-analysis\SKILL.md`
