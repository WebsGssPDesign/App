---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-data-cleaning/duplicate-removal/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe una habilidad para analizar múltiples hojas de Excel, filtrar datos por palabras clave y eliminar duplicados. El proceso genera automáticamente un informe de resumen estadístico y una lista detallada de los elementos únicos encontrados.

## Datos clave
- **Proyecto**: SenseNova Skills (flujo de trabajo de Excel).
- **Tecnologías**: Python, librería `pandas`.
- **Pasos principales**:
  1. Cargar archivo `.xlsx` y especificar la hoja objetivo (`Sheet1`).
  2. Iterar filas para extraer valores basados en palabras clave (ej: "综合楼", "控制中心") y limpiar espacios.
  3. Utilizar `set` para realizar la deduplicación eficiente por categorías.
  4. Exportar resultados a dos archivos: un resumen (`summary_report.xlsx`) y una lista detallada (`detail_list.xlsx`).

## Etiquetas
#Python #Excel #LimpiezaDeDatos #Deduplicacion

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-data-cleaning\duplicate-removal\SKILL.md`
