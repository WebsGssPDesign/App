---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-reading/structured-header-reading/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía describe un flujo de trabajo en Python para procesar archivos Excel grandes, enfocándose en la limpieza de datos y el análisis estadístico. Su objetivo es extraer caracteres chinos de campos de texto mediante expresiones regulares, contar ocurrencias específicas en columnas dinámicas y exportar los resultados a un archivo limpio con métricas de tamaño.

## Datos clave
- **Proyecto**: `SenseNova-Skills` (sub-habilidad de lectura de Excel).
- **Tecnologías**: Python, Pandas (`pd`, `df`), expresiones regulares (`re`).
- **Pasos principales**:
  1. Limpieza de texto: Extracción de caracteres chinos usando el rango Unicode `[一 -龥]`.
  2. Análisis dinámico: Búsqueda flexible de columnas por palabra clave (ej. 'type') y conteo de valores específicos ('varchar').
  3. Exportación: Guardado en `/mnt/data/cleaned_data_output.xlsx` con cálculo de tamaño en bytes y generación de enlace `sandbox`.

## Etiquetas
#Python #Excel #LimpiezaDeDatos #Procesamiento

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-reading\structured-header-reading\SKILL.md`
