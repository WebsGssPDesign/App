---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-data-cleaning/invalid-data-cleaning/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía describe un flujo de trabajo para limpiar datos masivos en Excel, optimizando el rendimiento mediante la conversión a Parquet y utilizando expresiones regulares para extraer únicamente caracteres chinos de columnas específicas. El proceso finaliza exportando los datos limpios en formato Excel con una ruta de descarga local.

## Datos clave
- **Proyecto**: SenseNova Skills (flujo de trabajo de Excel).
- **Tecnologías**: Python, Pandas, PyArrow, Expresiones Regulares (Regex).
- **Decisiones**: Convertir a Parquet si el volumen de datos es grande para mejorar la eficiencia de lectura/escritura.
- **Pasos importantes**:
  1. Leer todas las hojas del Excel y concatenarlas en un DataFrame único.
  2. Guardar el resultado como archivo `.parquet` usando `engine='pyarrow'`.
  3. Aplicar una función Regex (`[一-鿿]`) para filtrar solo caracteres chinos en la columna objetivo.
  4. Exportar el DataFrame final a un nuevo archivo `.xlsx` y generar un enlace de descarga local (`file://`).

## Etiquetas
#limpieza-de-datos #python #pandas #excel #procesamiento-lingüístico

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-data-cleaning\invalid-data-cleaning\SKILL.md`
