---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-result-export/single-sheet-export/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía describe una habilidad para procesar archivos Excel multi-hoja mediante Python. Permite filtrar datos según condiciones específicas, limpiar formatos y generar estadísticas básicas antes de exportar un archivo resultante con campos renombrados y enlaces de descarga.

## Datos clave
- **Proyecto**: SenseNova-Skills (flujo de trabajo Excel).
- **Tecnologías**: Python, Pandas (`pd.read_excel`, `to_excel`).
- **Pasos principales**:
  1. Leer la hoja objetivo ('Sheet1'), limpiar espacios en blanco y filtrar por un valor específico.
  2. Calcular conteos y porcentajes de categorías únicas para generar estadísticas.
  3. Seleccionar columnas específicas, renombrarlas (ej: '筛选维度', '分析维度') y guardar el resultado como `filtered_result_output.xlsx`.
- **Comandos/Puntos clave**: Uso de máscaras booleanas para filtrado, `value_counts()` para estadísticas y generación de enlaces sandbox.

## Etiquetas
#Python #Excel #DataProcessing #Pandas

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-result-export\single-sheet-export\SKILL.md`
