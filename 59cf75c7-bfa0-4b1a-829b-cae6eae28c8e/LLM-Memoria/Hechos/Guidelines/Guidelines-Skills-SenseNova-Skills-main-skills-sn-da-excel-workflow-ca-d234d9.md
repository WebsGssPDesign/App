---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-reading/multi-sheet-reading/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe un flujo de trabajo automatizado para analizar archivos Excel con múltiples hojas. Su función principal es optimizar el rendimiento mediante la conversión a Parquet en grandes volúmenes, limpiar datos con expresiones regulares y generar informes visuales detallados.

## Datos clave
- **Proyecto**: sn-da-excel-workflow (SenseNova).
- **Tecnologías**: Python, Pandas, OpenPyXL, NumPy, Matplotlib, PyArrow.
- **Lógica de optimización**: Si las filas totales ≥ 10,000, se convierte a Parquet usando `engine='pyarrow'` antes de leer.
- **Limpieza de datos**: Uso de regex `[一-鿿]` para extraer solo caracteres chinos en columnas específicas.
- **Análisis**: Cálculo de máximos por categoría y ajuste lineal (`np.polyfit`) entre dos variables.
- **Generación de reportes**: Creación de Excel con estilos condicional (resaltado del máximo) y gráficos de dispersión con tendencia en `/mnt/data/`.

## Etiquetas
#Python #ExcelAutomation #DataCleaning #Visualization #SenseNova

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-reading\multi-sheet-reading\SKILL.md`
