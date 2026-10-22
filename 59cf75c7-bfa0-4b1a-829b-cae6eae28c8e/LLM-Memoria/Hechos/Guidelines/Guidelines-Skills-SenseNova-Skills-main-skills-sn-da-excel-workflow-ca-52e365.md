---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-data-statistics/grouped-statistics/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento detalla un flujo de trabajo en Python para analizar archivos Excel con múltiples hojas, extrayendo estadísticas agrupadas por industria y valor industrial. El proceso incluye la limpieza de datos mediante fusión de tablas, identificación de los cinco principales valores y la generación de un informe final formateado visualmente.

## Datos clave
- **Tecnologías**: `pandas` para manipulación de datos y `openpyxl` para estilizado de hojas de cálculo.
- **Pasos críticos**: Extracción de dimensiones desde filas específicas (ej. fila 21), fusión interna (`inner join`) basada en índices, y filtrado de los top 5 resultados.
- **Estilización**: Aplicación de bordes finos, encabezados azules con texto blanco, alineación centrada y formato numérico para valores monetarios.
- **Salida**: Generación de un archivo `analysis_report.xlsx` con celdas críticas resaltadas en rojo y ancho de columnas ajustado.

## Etiquetas
#análisis-de-datos #excel-python #visualización #estadística

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-data-statistics\grouped-statistics\SKILL.md`
