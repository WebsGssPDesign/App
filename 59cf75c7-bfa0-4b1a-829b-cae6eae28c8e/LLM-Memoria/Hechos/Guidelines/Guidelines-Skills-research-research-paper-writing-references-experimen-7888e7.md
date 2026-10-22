---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/research/research-paper-writing/references/experiment-patterns.md"
tags: [hecho]
---
# experiment-patterns.md

## Resumen
Este documento establece patrones y mejores prácticas para diseñar experimentos de investigación a gran escala, enfocándose en la infraestructura, protocolos de evaluación y recuperación ante fallos. Su objetivo es garantizar la reproducibilidad, eficiencia y robustez al organizar scripts, gestionar configuraciones y analizar resultados de manera sistemática.

## Datos clave
- **Estructura de directorios**: Organización jerárquica separando ejecución (`experiments/`), resultados (`results/`), análisis (`analysis/`) y manuscritos (`paper/`).
- **Recuperación ante fallos**: Guardado incremental de resultados después de cada unidad de trabajo para permitir reinicios sin repetir tareas completadas.
- **Preservación de artefactos**: Almacenamiento de salidas intermedias (ej. `pass_01/`) para análisis posterior sin necesidad de re-ejecución.
- **Gestión de configuración**: Uso de archivos YAML para definir modelos, temperaturas y límites de tokens, cargados dinámicamente en scripts.
- **Separación de responsabilidades**: Scripts independientes para generación (`run_experiment.py`), evaluación ciega (`run_eval.py`) y visualización (`make_charts.py`).
- **Evaluación ciega**: Implementación de paneles de jueces con rotación aleatoria de etiquetas y conteo de Borda para tareas subjetivas.
- **Rutas importantes**: `workspace/experiments/run_main.py`, `config.yaml`, scripts de análisis estadístico en `analysis/`.

## Etiquetas
#experimentos #reproducibilidad #evaluacion #ciencia-de-datos

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\research\research-paper-writing\references\experiment-patterns.md`
