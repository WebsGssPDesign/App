---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/mlops/evaluation/weights-and-biases/references/integrations.md"
tags: [hecho]
---
# integrations.md

## Resumen
Esta guía técnica detalla cómo integrar Weights & Biases (W&B) con frameworks de aprendizaje automático populares como HuggingFace, PyTorch Lightning y TensorFlow. Su objetivo es facilitar el seguimiento automático de métricas, la visualización de experimentos y el registro de modelos mediante artefactos durante el entrenamiento.

## Datos clave
- **Integraciones principales**: HuggingFace Transformers (automática y personalizada), PyTorch Lightning (básica y con barridos de hiperparámetros), Keras/TensorFlow, Fast.ai y XGBoost/LightGBM.
- **Funcionalidades críticas**: Uso de `report_to="wandb"` en argumentos de entrenamiento para HuggingFace; implementación de callbacks personalizados (`WandbCallback`) para métricas específicas.
- **Registro de modelos**: Creación de artefactos tipo 'model' usando `wandb.Artifact` y guardado de directorios finales con `trainer.save_model()`.
- **Barridos de hiperparámetros**: Configuración de exploración bayesiana en PyTorch Lightning definiendo rangos, distribuciones y objetivos de optimización.
- **Visualización avanzada**: Registro de imágenes (`wandb.Image`) y matrices de confusión (`wandb.plot.confusion_matrix`) dentro de los pasos de validación.

## Etiquetas
#mlops #weightsandbiases #pytorchlightning #huggingface #experimenttracking

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\mlops\evaluation\weights-and-biases\references\integrations.md`
