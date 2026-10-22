---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-data-cleaning/missing-value-handling/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento detalla un flujo de trabajo en Python para la limpieza inteligente, validación cruzada y análisis visual de archivos Excel con múltiples hojas. Su objetivo es automatizar tareas como el manejo de valores faltantes, la normalización de texto y la generación de reportes estéticos con soporte para caracteres chinos.

## Datos clave
- **Proyecto**: `sn-da-excel-workflow` (módulo de limpieza de datos).
- **Tecnologías**: Python, Pandas (`ffill`, `crosstab`, `groupby`), Matplotlib, OpenPyXL.
- **Pasos críticos**:
  1. Limpieza: Rellenar celdas fusionadas con `ffill`, aplicar expresiones regulares para sanitizar texto y filtrar valores basados en componentes RGB (Rojo, Verde, Azul).
  2. Validación: Comparar sumas de columnas entre diferentes hojas (`Sheet1` vs `Sheet2`) y calcular tablas dinámicas de porcentajes.
  3. Visualización: Configurar fuentes para caracteres chinos en gráficos de barras y exportar resultados a Excel con estilos condicionales (texto rojo/grueso para anomalías).

## Etiquetas
#Python #LimpiezaDeDatos #ExcelAutomation #Análisis

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-data-cleaning\missing-value-handling\SKILL.md`
