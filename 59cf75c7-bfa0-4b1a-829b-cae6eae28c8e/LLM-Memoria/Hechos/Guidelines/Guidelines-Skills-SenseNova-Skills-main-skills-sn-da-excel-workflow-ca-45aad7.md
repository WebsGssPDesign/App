---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-data-visualization/stacked-chart-visualization/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento detalla un flujo de trabajo en Python para visualizar datos de composición porcentual utilizando gráficos de barras apiladas. Su objetivo es procesar cadenas con formato de porcentaje, calcular automáticamente las categorías faltantes basándose en la suma total del 100% y generar una imagen clara que muestre tendencias multidimensionales.

## Datos clave
- **Tecnologías**: Python, Pandas (para manipulación de datos), Matplotlib y Seaborn (para visualización).
- **Proceso principal**: Limpieza de datos mediante conversión de cadenas a flotantes, cálculo del residuo para completar el 100% y renderizado gráfico.
- **Lógica crítica**: Uso del parámetro `bottom` en la función `plt.bar()` para apilar las barras correctamente según los niveles anteriores.
- **Configuración**: Se configuran fuentes de caracteres chinos ('SimHei') y se ajustan márgenes (`bbox_inches='tight'`) al guardar el archivo PNG a 300 dpi.

## Etiquetas
#visualización #python #pandas #graficos_apilados

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-data-visualization\stacked-chart-visualization\SKILL.md`
