---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-data-analysis/pivot-table-analysis/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe un flujo de trabajo en Python para analizar datos estructurados en Excel mediante tablas dinámicas y gráficos de calor. Su objetivo es limpiar la información, calcular distribuciones porcentuales por categoría y visualizar los resultados para identificar líderes en métricas como premios o rendimiento.

## Datos clave
- **Proyecto**: sn-da-excel-workflow (análisis de datos con Excel).
- **Tecnologías**: Python, Pandas, Matplotlib, Seaborn.
- **Pasos críticos**:
  - Limpieza: Manejo de celdas fusionadas con `ffill` y eliminación de filas vacías.
  - Análisis: Uso de `pd.crosstab` para frecuencias y cálculo de proporciones por columna.
  - Visualización: Configuración de fuentes chinas (`SimHei`) para generar mapas de calor legibles.
  - Exportación: Guardado de múltiples hojas (frecuencias, porcentajes, rankings) en un único archivo Excel.

## Etiquetas
#análisis-de-datos #python-pandas #visualización #excel

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-data-analysis\pivot-table-analysis\SKILL.md`
