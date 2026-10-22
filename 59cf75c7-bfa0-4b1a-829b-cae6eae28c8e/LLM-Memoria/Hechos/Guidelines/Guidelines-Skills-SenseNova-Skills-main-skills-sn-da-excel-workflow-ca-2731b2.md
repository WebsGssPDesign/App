---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-data-visualization/bar-chart-visualization/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía describe una habilidad técnica para automatizar el análisis de datos en Excel mediante Python. El proceso incluye la limpieza y fusión de múltiples hojas de cálculo, la ejecución de estadísticas cruzadas y la generación de gráficos de barras horizontales estéticos con soporte para caracteres chinos.

## Datos clave
- **Proyecto**: Flujo de trabajo de Excel (SenseNova).
- **Tecnologías**: Python, Pandas (`pd.concat`, `groupby`), Matplotlib.
- **Decisiones técnicas**: Uso de `ffill()` para rellenar celdas fusionadas y mapeo manual de fragmentos de texto a categorías estándar.
- **Configuración crítica**: Configuración de fuentes en Matplotlib (`SimHei`, `DejaVu Sans`) para garantizar la visualización correcta de caracteres chinos y símbolos matemáticos.
- **Salida**: Generación de un archivo Excel con totales y una URL de descarga temporal.

## Etiquetas
#Python #VisualizaciónDeDatos #Excel #Automatización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-data-visualization\bar-chart-visualization\SKILL.md`
