---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/mlops/evaluation/weights-and-biases/references/artifacts.md"
tags: [hecho]
---
# artifacts.md

## Resumen
Esta guía explica cómo gestionar datos y modelos en MLOps utilizando W&B Artifacts para su versionado, trazabilidad y almacenamiento eficiente. Sirve como referencia técnica para crear, registrar y desplegar activos de machine learning con control de versiones automático y alias (como 'latest' o 'production').

## Datos clave
- **Conceptos**: Versionado automático (v0, v1...), trazabilidad de linaje, deduplicación de almacenamiento.
- **Tipos de Artifacts**: Conjuntos de datos (`type='dataset'`), modelos entrenados (`type='model'`) y datos preprocesados.
- **Comandos Python Clave**: `wandb.Artifact()`, `.add_file()`, `.add_dir()`, `run.log_artifact()` con parámetros `aliases`.
- **Gestión de Registros**: Creación de registros en la UI, enlace de modelos (`link_artifact`) y promoción entre etapas (staging/production).
- **Uso**: Descarga vía `use_artifact('nombre:versión')` o alias; acceso a metadatos como digest y fecha de creación.
- **Optimización**: Si el contenido es idéntico, no se crea una nueva versión, sino que referencia la existente.

## Etiquetas
#MLOps #WandB #ModelRegistry #VersionControl #DataScience

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\mlops\evaluation\weights-and-biases\references\artifacts.md`
