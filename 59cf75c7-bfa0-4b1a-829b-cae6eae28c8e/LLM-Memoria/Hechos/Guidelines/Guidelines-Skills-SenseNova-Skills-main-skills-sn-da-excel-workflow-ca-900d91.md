---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-data-visualization/scatter-plot-visualization/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento detalla un flujo de trabajo en Python para realizar análisis estadístico y visualización avanzada de datos en Excel, específicamente mediante gráficos de dispersión. Su objetivo es limpiar grandes conjuntos de datos, calcular métricas clave como la regresión lineal y exportar resultados visuales de alta resolución con soporte para caracteres chinos.

## Datos clave
- **Proyecto**: Flujo de trabajo de visualización estadística en Excel (Skills/SenseNova).
- **Tecnologías**: Python, Pandas (`groupby`, `pivot_table`), Matplotlib, SciPy (`linregress`).
- **Decisiones técnicas**: Uso de `ffill` para manejar celdas fusionadas; limpieza numérica con expresiones regulares.
- **Configuración de gráficos**: Fuente `SimHei` o `DejaVu Sans` para evitar problemas con caracteres chinos; uso de "jitter" (`np.random.normal`) en dispersión para evitar superposición de puntos.
- **Rutas y archivos**: Salida de imagen `'analysis_plot.png'`, datos limpios exportados a `'cleaned_analysis_data.csv'` (codificación `utf-8-sig`).
- **Métricas clave**: Cálculo de pendiente, intercepto, coeficiente de determinación ($R^2$) y valor p.

## Etiquetas
#Python #VisualizaciónDeDatos #AnálisisEstadístico #Matplotlib

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-data-visualization\scatter-plot-visualization\SKILL.md`
