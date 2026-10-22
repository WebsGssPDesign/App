---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-reading/large-excel-reading/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define una habilidad técnica para analizar y formatear archivos Excel de gran volumen. Su objetivo es optimizar el procesamiento mediante la conversión a Parquet cuando los datos superan un umbral, generar informes con estilos personalizados y resaltar automáticamente las filas con valores máximos.

## Datos clave
- **Proyecto**: SenseNova-Skills (sn-da-excel-workflow).
- **Tecnologías**: Python, pandas, openpyxl, PyArrow.
- **Lógica de decisión**: Si el total de filas >= 10,000, se convierte a Parquet para mejorar la eficiencia antes del análisis.
- **Pasos críticos**:
    1. Contar filas en todos los sheets; si es grande, guardar como `.parquet`.
    2. Agrupar datos por columna de clasificación y sumar valores objetivo.
    3. Identificar el tipo con el valor máximo usando `idxmax()`.
- **Estilización**: Uso de `PatternFill` para encabezados azules y resaltado verde en la fila del máximo; ajuste de anchos de columnas A (18) y B (25).
- **Salida**: Generación de enlace de descarga tipo `sandbox:`.

## Etiquetas
#Python #ExcelAutomation #DataAnalysis #OpenPyXL

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-reading\large-excel-reading\SKILL.md`
