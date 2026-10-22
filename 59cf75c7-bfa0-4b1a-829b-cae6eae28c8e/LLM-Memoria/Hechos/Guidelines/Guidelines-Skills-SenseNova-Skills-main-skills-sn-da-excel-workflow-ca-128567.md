---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-data-filtering/range-filtering/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe una habilidad técnica para optimizar la filtración de datos en Excel mediante Python, permitiendo procesar grandes volúmenes de información con múltiples condiciones numéricas. Su objetivo es automatizar el flujo de trabajo que incluye lectura, limpieza, filtrado condicional y exportación de resultados específicos.

## Datos clave
- **Proyecto**: Optimización de filtrado condicional en Excel (Excel_Conditional_Filtering_Optimization).
- **Tecnologías**: Python, librería pandas (`pd.ExcelFile`, `read_excel`, `to_numeric`, `drop_duplicates`).
- **Pasos importantes**:
  1. Leer todos los *sheets* y contar filas totales para evaluar escala.
  2. Limpiar datos: forzar conversión a numérico en columnas clave (`val_a`, `val_b`, `val_c`) y manejar encabezados.
  3. Aplicar máscara de filtrado lógico (ejemplo: `val_a == 0` y otros) y eliminar duplicados/NA.
  4. Guardar resultado en nuevo archivo Excel (`filtered_analysis_result.xlsx`).

## Etiquetas
#Python #ExcelAutomation #DataCleaning #pandas

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-data-filtering\range-filtering\SKILL.md`
