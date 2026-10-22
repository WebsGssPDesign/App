---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-data-statistics/basic-statistics/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía define un flujo de trabajo en Python para realizar estadísticas básicas sobre archivos Excel con múltiples hojas. Permite filtrar datos por grupos específicos, calcular promedios, extraer valores de rangos de filas definidos y generar archivos de resultados descargables.

## Datos clave
- **Proyecto**: `sn-da-excel-workflow` (capacidad de estadística básica).
- **Tecnologías**: Python, Pandas (`pd.read_excel`, `to_numeric`, `mean`), OpenPyXL.
- **Pasos importantes**:
  1. Filtrar datos por columna '班级' y calcular promedios de columnas numéricas ('总分', '理数').
  2. Para archivos pequeños (<10k filas), extraer componentes y potencia de rangos específicos (filas 21-28, 51-58) en 'Sheet2', eliminar duplicados y sumar la potencia total.
  3. Guardar resultados en `output_power_sum.xlsx` y `output_analysis_result.xlsx` con enlaces locales (`file://`).

## Etiquetas
#excel #python #pandas #estadística #automatización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-data-statistics\basic-statistics\SKILL.md`
