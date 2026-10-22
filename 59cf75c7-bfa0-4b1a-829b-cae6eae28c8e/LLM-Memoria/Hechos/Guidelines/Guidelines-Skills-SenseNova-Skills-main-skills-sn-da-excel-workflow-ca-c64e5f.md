---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-data-cleaning/text-normalization/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía detalla un flujo de trabajo para limpiar datos en archivos Excel, enfocándose en la normalización de texto y el manejo eficiente de grandes volúmenes de información. Su objetivo es estandarizar campos numéricos eliminando prefijos extraños y purificar columnas de texto para retener únicamente caracteres chinos, generando finalmente un archivo limpio listo para descarga.

## Datos clave
- **Proyecto**: Flujo de trabajo de Excel (SenseNova-Skills).
- **Tecnologías**: Python, pandas, NumPy, librería `re` (expresiones regulares), motor `openpyxl`.
- **Pasos importantes**:
  - Identificar columnas objetivo para limpieza numérica y textual.
  - Eliminar prefijos como `.`, `_`, `■ `, etc., de valores numéricos usando un bucle iterativo.
  - Extraer caracteres chinos (Unicode `\u4e00-\u9fff`) de cadenas de texto mediante expresiones regulares.
  - Guardar el resultado en `/mnt/data/标准化清洗结果.xlsx` y generar un enlace de descarga sandbox.
- **Gestión de memoria**: Liberación explícita del DataFrame (`del df`) y recolección de basura (`gc.collect()`) para procesar archivos grandes sin saturar la RAM.

## Etiquetas
#limpieza-de-datos #excel-python #procesamiento-de-texto #optimización-memoria

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-data-cleaning\text-normalization\SKILL.md`
