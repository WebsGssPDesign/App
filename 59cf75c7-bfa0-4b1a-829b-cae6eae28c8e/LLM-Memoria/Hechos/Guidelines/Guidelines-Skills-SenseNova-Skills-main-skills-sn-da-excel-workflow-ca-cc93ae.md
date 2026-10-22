---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-cell-coloring/duplicate-value-coloring/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe una capacidad del flujo de trabajo en Excel para extraer coeficientes específicos de múltiples hojas, compararlos contra un estándar y generar un informe con valores anómalos resaltados en rojo. Sirve para automatizar la detección de inconsistencias en grandes archivos Excel sin necesidad de intervención manual.

## Datos clave
- **Proyecto**: SenseNova-Skills (flujo de trabajo Excel).
- **Tecnologías**: Python, pandas (`pd.read_excel`), openpyxl (`PatternFill`, `Workbook`).
- **Lógica principal**: Función `extract_target_value` busca etiquetas en columnas específicas y recupera valores con un offset definido.
- **Umbral estándar**: 0.6 (cualquier valor distinto se marca como anómalo).
- **Pasos clave**:
  1. Leer hojas 'Sheet1' y 'Sheet2'.
  2. Iterar sobre los coeficientes extraídos y comparar con el estándar.
  3. Generar `comparison_report.xlsx` aplicando un relleno rojo (`FF0000`) a las filas con valores anómalos.

## Etiquetas
#excel #python #automatización #datos #análisis

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-cell-coloring\duplicate-value-coloring\SKILL.md`
