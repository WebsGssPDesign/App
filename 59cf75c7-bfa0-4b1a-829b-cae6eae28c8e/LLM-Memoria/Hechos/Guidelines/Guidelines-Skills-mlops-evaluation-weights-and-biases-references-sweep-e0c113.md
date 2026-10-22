---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/mlops/evaluation/weights-and-biases/references/sweeps.md"
tags: [hecho]
---
# sweeps.md

## Resumen
Este documento es una guía completa para realizar optimización de hiperparámetros utilizando W&B Sweeps, detallando cómo configurar experimentos y seleccionar estrategias de búsqueda. Su objetivo principal es mejorar el rendimiento de modelos de machine learning automatizando la exploración del espacio de parámetros con eficiencia computacional.

## Datos clave
- **Tecnología**: Weights & Biases (W&B) para gestión de experimentos.
- **Estrategias de búsqueda**: Grid Search (exhaustivo), Random Search (muestreo aleatorio) y Bayesian Optimization (recomendada por eficiencia).
- **Tipos de parámetros**: Continuos (distribuciones log_uniform, uniform, normal), discretos (rangos enteros, cuantizados) y categóricos.
- **Configuración crítica**: Definición del `metric` a optimizar (ej. `val/accuracy`) y el método de búsqueda (`method`).
- **Optimización avanzada**: Uso de terminación temprana con algoritmo Hyperband para ahorrar recursos en ejecuciones costosas.
- **Comandos principales**: `wandb.sweep()` para iniciar configuraciones y `wandb.agent()` para ejecutar múltiples iteraciones.

## Etiquetas
#MLOps #HyperparameterTuning #WeightsAndBiases #MachineLearning

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\mlops\evaluation\weights-and-biases\references\sweeps.md`
