---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-result-export/formatted-export/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define una habilidad para procesar archivos Excel con múltiples hojas, identificando y filtrando registros que contienen valores nulos o inválidos. El resultado se exporta como un nuevo archivo donde las filas afectadas están resaltadas en rojo para facilitar su visualización y validación durante procesos de limpieza de datos.

## Datos clave
- **Proyecto**: SenseNova Skills (flujo de trabajo Excel).
- **Tecnologías**: Python, pandas, pyarrow, openpyxl.
- **Lógica de detección**: Búsqueda de columnas mediante coincidencia parcial de palabras clave ('keyword1', 'keyword2', etc.) y filtrado de celdas vacías o con texto "nan".
- **Formato de salida**: Archivo Excel (.xlsx) con rellón rojo sólido en todas las filas filtradas (desde la fila 2).
- **Pasos críticos**: Iteración sobre todos los sheets, concatenación de resultados y aplicación manual de estilos mediante `openpyxl`.

## Etiquetas
#limpieza-de-datos #excel-python #automatización #sensenova

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-result-export\formatted-export\SKILL.md`
