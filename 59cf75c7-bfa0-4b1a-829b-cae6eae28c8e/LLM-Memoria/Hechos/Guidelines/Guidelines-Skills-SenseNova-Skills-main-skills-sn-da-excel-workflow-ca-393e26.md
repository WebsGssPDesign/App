---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-data-cleaning/outlier-detection/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe un flujo de trabajo en Python para la detección y evaluación de calidad de datos utilizando el método del rango intercuartílico (IQR). Sirve como guía técnica para identificar valores atípicos, visualizar distribuciones mediante gráficos de caja y analizar características estadísticas como asimetría y curtosis antes de aplicar métodos de limpieza.

## Datos clave
- **Proyecto**: sn-da-excel-workflow (SenseNova Skills)
- **Tecnologías**: Python, Pandas, Matplotlib, Seaborn, NumPy
- **Método principal**: IQR (Q1 - 1.5*IQR, Q3 + 1.5*IQR) para identificar outliers
- **Análisis estadístico**: Cálculo de asimetría (skewness) y curtosis (kurtosis) para evaluar la forma de la distribución
- **Visualización**: Gráficos de caja multi-dimensionales con anotaciones de estadísticas descriptivas
- **Pasos críticos**:
  1. Configuración de fuentes para visualización en chino/inglés
  2. Filtrado automático de columnas numéricas y eliminación de NaNs
  3. Generación de informe `outlier_analysis_report.png` (dpi=300)
- **Función de limpieza**: `handle_outliers` soporta métodos 'cap' (clipping) o 'drop' (eliminación)

## Etiquetas
#limpieza-de-datos #python #excel #análisis-estadístico #outlier-detection

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-data-cleaning\outlier-detection\SKILL.md`
