---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-result-export/chart-embedded-export/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define una habilidad técnica para procesar datos estructurados en Excel, ejecutando un flujo que incluye limpieza, análisis estadístico y generación de visualizaciones. Su objetivo es producir informes completos con gráficos de alta resolución y enlaces de descarga automáticos, optimizado para grandes volúmenes de datos.

## Datos clave
- **Proyecto**: SenseNova Skills (flujo de trabajo Excel).
- **Tecnologías**: Python, Pandas (`ffill`, `value_counts`, `crosstab`), Matplotlib.
- **Decisiones técnicas**: Uso de expresiones regulares para limpiar texto y mapeo manual de categorías ('A类特征', 'B类特征').
- **Rutas de salida**: `analysis_result.xlsx` (datos) y `comprehensive_chart.png/.svg` (visualizaciones).
- **Comandos/Pasos críticos**: Configuración de fuentes (`SimHei`, `DejaVu Sans`) para soporte multilingüe, exportación a SVG/PNG con 300 DPI, y generación dinámica de enlaces de sandbox.

## Etiquetas
#Python #DataAnalysis #ExcelAutomation #Visualization

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-result-export\chart-embedded-export\SKILL.md`
