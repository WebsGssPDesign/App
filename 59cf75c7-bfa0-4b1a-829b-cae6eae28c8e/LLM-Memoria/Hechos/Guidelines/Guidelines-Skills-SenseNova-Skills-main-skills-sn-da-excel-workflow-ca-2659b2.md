---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-data-cleaning/numeric-format-normalization/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe una habilidad para normalizar formatos numéricos y limpiar datos en Excel, asegurando la integridad mediante la comparación de totales calculados contra valores esperados. Sirve como paso específico dentro del flujo de trabajo SenseNova para validar datos antes de su conversión a Parquet o exportación final.

## Datos clave
- **Proyecto**: SenseNova-Skills (flujo de trabajo Excel).
- **Tecnologías**: Python, Pandas (`pd.read_excel`, `to_numeric`), formatos `.xlsx` y `.csv`.
- **Pasos importantes**:
  1. Limpieza: Eliminación de valores nulos y conversión forzada a tipo numérico con errores coercidos.
  2. Validación: Cálculo del total y comparación con la fila "合计" (Total) en una hoja de resumen, tolerando diferencias menores a `1e-6`.
  3. Exportación: Guardado de resultados estadísticos en archivos `.xlsx` y `.csv` con codificación UTF-8-SIG.
- **Decisiones**: Uso de `errors='coerce'` para manejar datos no numéricos y manejo de excepciones durante la lectura del archivo de resumen.

## Etiquetas
#Python #DataCleaning #ExcelAutomation #SenseNova

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-data-cleaning\numeric-format-normalization\SKILL.md`
