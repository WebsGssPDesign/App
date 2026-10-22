---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-data-visualization/histogram-visualization/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe un flujo de trabajo en Python para analizar la distribución estadística y detectar valores atípicos en datos numéricos extraídos de hojas de cálculo. Su objetivo es generar informes visuales detallados, como gráficos de caja y histogramas de errores, junto con métricas cuantitativas para evaluar la calidad de los datos.

## Datos clave
- **Proyecto**: sn-da-excel-workflow (análisis de visualización de datos en Excel).
- **Tecnologías**: Python, pandas, matplotlib, seaborn, numpy, re.
- **Pasos importantes**:
  - Preprocesamiento: carga de `input_data.xlsx`, manejo de celdas fusionadas con `ffill` y renombrado dinámico de columnas.
  - Visualización: generación de gráficos de caja por columna con estadísticas (media, mediana) y exportación a PNG de alta resolución (300 dpi).
  - Detección de anomalías: cálculo del rango intercuartílico (IQR) para identificar valores fuera de los límites inferior y superior.
  - Extracción de errores: uso de expresiones regulares (`±(\d+\.?\d*)`) para extraer magnitudes de error de texto y crear un histograma de distribución con líneas de referencia.
  - Salida: exportación de resultados a `analysis_summary.csv` y generación de enlaces de descarga.

## Etiquetas
#análisis-de-datos #python #visualización-estadística #detección-anomalías

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-data-visualization\histogram-visualization\SKILL.md`
