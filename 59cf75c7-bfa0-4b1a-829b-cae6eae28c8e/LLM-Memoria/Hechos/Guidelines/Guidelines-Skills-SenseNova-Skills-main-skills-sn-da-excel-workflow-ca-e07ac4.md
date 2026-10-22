---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-result-export/report-generation-export/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define una habilidad técnica para analizar datos de Excel, generando informes con estadísticas cruzadas y gráficos visuales. Su función es extraer métricas clave, identificar valores que superan límites predefinidos mediante búsqueda inversa y exportar los resultados junto a enlaces de descarga seguros.

## Datos clave
- **Proyecto**: SenseNova-Skills (flujo de trabajo Excel).
- **Tecnologías**: Python, pandas, matplotlib, regular expressions (`re`).
- **Pasos principales**:
  1. Clasificación de datos basada en palabras clave y generación de tablas con totales y porcentajes.
  2. Detección de filas donde el valor objetivo excede un límite encontrado mediante búsqueda inversa (hasta 15 líneas atrás).
  3. Creación de gráficos circulares de alta resolución (dpi=150) y exportación a Excel con enlaces sandbox.
- **Configuraciones**: Uso de fuentes 'SimHei' para caracteres chinos en gráficos; lógica de severidad ('Alto' si la diferencia > 10).

## Etiquetas
#Python #AnalisisDeDatos #Excel #Visualizacion

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-result-export\report-generation-export\SKILL.md`
