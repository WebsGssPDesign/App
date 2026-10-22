---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-reading/range-reading/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define una habilidad técnica para analizar archivos Excel con múltiples hojas, optimizando el procesamiento de grandes volúmenes de datos mediante conversión a Parquet. Permite extraer rangos específicos, realizar estadísticas y generar gráficos de regresión lineal con visualización en chino.

## Datos clave
- **Proyecto**: SenseNova-Skills (flujo de trabajo Excel).
- **Tecnologías**: Python, Pandas, NumPy, Matplotlib, Parquet (pyarrow).
- **Decisiones**: Limpieza dinámica de nombres de columnas con espacios; uso de bloques o conversión a Parquet para archivos grandes.
- **Pasos importantes**: 
  1. Lectura y limpieza de `Sheet2` calculando tasas de nulos.
  2. Extracción de pares numéricos en filas 40-50 y conversión a DataFrame.
  3. Ajuste de polinomio lineal (`np.polyfit`) y generación de gráfico con fuente `SimHei`.
- **Rutas**: Directorio `output_results` para guardar `.parquet`, `.png` y `.csv`.

## Etiquetas
#Python #AnálisisDeDatos #Excel #Visualización #Optimización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-reading\range-reading\SKILL.md`
