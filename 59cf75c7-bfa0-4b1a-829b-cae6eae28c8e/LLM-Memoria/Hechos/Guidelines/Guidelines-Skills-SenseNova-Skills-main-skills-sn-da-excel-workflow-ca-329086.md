---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-cell-coloring/outlier-coloring/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define una habilidad técnica para detectar y resaltar automáticamente en Excel los valores que superan límites establecidos y las celdas con errores de fórmula. El proceso combina análisis de texto, lógica condicional y manipulación de estilos para generar reportes visuales claros y datos resumidos.

## Datos clave
- **Proyecto**: Flujo de trabajo SenseNova-Skills (Excel).
- **Tecnologías**: Python, pandas, openpyxl, expresiones regulares (`re`).
- **Pasos principales**:
  1. Extraer límites numéricos usando regex y comparar con valores reales en filas específicas.
  2. Identificar errores de fórmula (ej. `#DIV/0!`) recorriendo celdas del libro.
  3. Aplicar relleno rojo (`PatternFill`) a las filas excedentes y celdas erróneas.
  4. Generar un archivo de resumen separado con los detalles de las anomalías detectadas.
- **Rutas de salida**: `highlighted_report.xlsx` (archivo resaltado) y `outlier_summary.xlsx` (reporte de datos).

## Etiquetas
#Python #ExcelAutomation #DataQuality #OutlierDetection

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-cell-coloring\outlier-coloring\SKILL.md`
