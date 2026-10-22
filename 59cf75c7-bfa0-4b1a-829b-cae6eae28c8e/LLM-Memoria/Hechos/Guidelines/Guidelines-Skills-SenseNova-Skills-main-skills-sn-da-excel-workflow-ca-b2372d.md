---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-data-statistics/percentage-calculation/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía detalla un flujo de trabajo en Python para analizar grandes archivos Excel, extrayendo métricas clave mediante búsqueda dinámica y calculando porcentajes. El proceso genera informes estructurados y gráficos visuales optimizados para presentar resultados estadísticos claros.

## Datos clave
- **Proyecto**: Dinámico porcentaje y análisis de archivos grandes (SenseNova).
- **Tecnologías**: Python, Pandas (`pd.DataFrame`, `iterrows`), OpenPyXL, Matplotlib.
- **Decisiones**: Búsqueda dinámica de columnas por palabras clave ('keyword1', 'keyword2') para evitar errores en nombres variables; uso de `SimHei` y `WenQuanYi Zen Hei` para soportar caracteres chinos sin corrupción en gráficos.
- **Rutas y archivos**: Entrada desde `df_analysis`; salida a `output_analysis_result.xlsx` (hoja '汇总结果') y `percentage_chart.png`.
- **Pasos importantes**: 1) Escaneo línea por línea para extraer valores numéricos positivos únicos; 2) Filtrado condicional basado en categorías específicas antes de calcular promedios; 3) Cálculo de porcentaje relativo entre dos indicadores clave.

## Etiquetas
#Python #AnálisisDeDatos #Excel #Visualización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-data-statistics\percentage-calculation\SKILL.md`
