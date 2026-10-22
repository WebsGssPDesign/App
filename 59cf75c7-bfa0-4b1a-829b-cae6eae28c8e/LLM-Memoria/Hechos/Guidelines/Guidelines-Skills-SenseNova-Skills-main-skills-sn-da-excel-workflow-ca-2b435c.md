---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-reading/multi-file-reading/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento detalla un flujo de trabajo técnico para analizar múltiples archivos Excel, evaluando su escala y optimizando el manejo de datos grandes mediante conversión a Parquet. El proceso incluye la generación de informes estadísticos detallados y visualizaciones gráficas (como diagramas de pastel) para facilitar la interpretación de los resultados.

## Datos clave
- **Proyecto**: `SenseNova-Skills` - Habilidad de análisis multi-fichero Excel.
- **Tecnologías**: Python, Pandas (`pd.read_excel`, `read_parquet`), Matplotlib, OpenPyXL (implícito en Excel).
- **Pasos críticos**:
  1. Lectura eficiente: Usar `usecols=[0]` para contar filas sin cargar todo el archivo en memoria.
  2. Optimización: Conversión de datos grandes a formato Parquet antes del análisis profundo.
  3. Estadística: Cálculo de conteos y porcentajes por categoría (ej. columna '剪裁结果').
  4. Visualización: Configuración de fuentes (`SimHei`) para evitar problemas con caracteres chinos en gráficos.
- **Salidas**: Gráfico `analysis_pie_chart.png` y tabla resumen `analysis_report.xlsx`.

## Etiquetas
#Python #AnálisisDeDatos #Excel #Pandas #Visualización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-reading\multi-file-reading\SKILL.md`
