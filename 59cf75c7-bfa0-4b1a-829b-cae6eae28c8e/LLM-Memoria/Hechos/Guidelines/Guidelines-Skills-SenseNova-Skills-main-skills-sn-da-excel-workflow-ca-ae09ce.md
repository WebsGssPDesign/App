---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-data-visualization/pie-chart-visualization/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento detalla un flujo de trabajo automatizado en Python para analizar datos de Excel o CSV, identificando automáticamente columnas de categorías y valores. El sistema genera informes que incluyen estadísticas resumidas y gráficos de pastel visualmente mejorados, listos para descarga directa.

## Datos clave
- **Tecnologías**: pandas, matplotlib, openpyxl, re (expresiones regulares).
- **Lógica de detección**: Identifica columnas numéricas buscando palabras clave como '金额' o '数量'; detecta categorías usando patrones regex para términos chinos o etiquetas específicas.
- **Procesamiento**: Limpia datos mediante `ffill` para celdas fusionadas, convierte tipos y calcula porcentajes relativos al total.
- **Visualización**: Crea gráficos de pastel con efecto anillo (donut), resaltando el segmento más grande y configurando fuentes SimHei/DejaVu Sans para compatibilidad con caracteres chinos.
- **Exportación**: Genera un archivo Excel único que integra una hoja de resumen y la imagen del gráfico incrustada, proporcionando un enlace de descarga en formato Base64.

## Etiquetas
#análisis-de-datos #visualización-python #automatización-excel

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-data-visualization\pie-chart-visualization\SKILL.md`
