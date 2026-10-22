---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Leakage_%28machine_learning%29"
tema: "Temporal Workflow Isolation"
tags: [web]
---
# Leakage (machine learning)

## Resumen
La fuga de datos (data leakage) en aprendizaje automático ocurre cuando un modelo utiliza información durante el entrenamiento que no estaría disponible al momento de la predicción real. Esto genera estimaciones de rendimiento excesivamente optimistas y puede llevar a seleccionar modelos subóptimos frente a alternativas libres de fugas.

## Datos clave
- **Fuga por características**: Incluir columnas que son duplicados, proxies o versiones anticipadas del objetivo (ej. "Salario Mensual" para predecir "Salario Anual").
- **Fuga por ejemplos de entrenamiento**: Compartir información incorrectamente entre filas mediante duplicación, muestreo bootstrap antes de dividir datos, o divisiones aleatorias en series temporales.
- **Fuga grupal**: No asegurar que todos los registros de un mismo grupo (ej. imágenes de un paciente) estén en el mismo conjunto de datos.
- **Impacto**: Un estudio de 2023 identificó la fuga como una falla extendida en al menos 294 publicaciones académicas, provocando una crisis de reproducibilidad.
- **Detección**: Buscar discrepancias entre entrenamiento y prueba, examinar la importancia de las características y usar conjuntos de retención (hold-out) separados para validación final.

## Etiquetas
#aprendizaje_automático #fuga_de_datos #reproducibilidad #modelado_estadístico

Fuente: https://en.wikipedia.org/wiki/Leakage_%28machine_learning%29
