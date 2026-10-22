---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-data-analysis/kpi-metric-analysis/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía define un flujo de trabajo en Python para analizar KPIs en Excel, automatizando la validación de consistencia de unidades y el ordenamiento de métricas clave. Su objetivo es generar tablas de resultados verificadas listas para su descarga y uso posterior.

## Datos clave
- **Proyecto**: SenseNova Skills (flujo de trabajo de análisis de datos).
- **Tecnologías**: Python, Pandas (`pd.DataFrame`), Openpyxl.
- **Pasos principales**:
  1. Verificación de consistencia de unidades mediante conversión y cálculo de tolerancia ($1e^{-6}$).
  2. Ordenamiento descendente de métricas por grupo (ej. nombre de zona de desarrollo).
  3. Generación de archivo Excel (`analysis_result.xlsx`) con columnas renombradas para claridad.
- **Comandos/Funciones**: `to_excel`, `sort_values`, operaciones aritméticas en DataFrames.

## Etiquetas
#análisis-de-datos #validación-unidades #excel-python #kpi

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-data-analysis\kpi-metric-analysis\SKILL.md`
