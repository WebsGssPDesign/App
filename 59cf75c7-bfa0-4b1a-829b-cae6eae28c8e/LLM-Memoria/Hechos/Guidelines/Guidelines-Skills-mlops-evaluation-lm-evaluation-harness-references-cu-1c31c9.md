---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/mlops/evaluation/lm-evaluation-harness/references/custom-tasks.md"
tags: [hecho]
---
# custom-tasks.md

## Resumen
Esta guía explica cómo crear tareas de evaluación personalizadas en lm-evaluation-harness para datos propietarios o dominios específicos. Permite definir conjuntos de datos, plantillas de prompts y métricas a medida mediante archivos YAML y funciones Python.

## Datos clave
- **Tecnología**: lm-evaluation-harness (lm_eval).
- **Formatos de datos**: JSONL local, datasets de HuggingFace, CSV.
- **Tipos de salida**: `generate_until` (generación libre), `loglikelihood`, `multiple_choice`.
- **Configuración YAML**: Campos esenciales incluyen `task`, `dataset_path`, `doc_to_text`, `metric_list` y `generation_kwargs`.
- **Lógica personalizada**: Uso de Jinja2 para plantillas condicionales e integración con funciones Python (`!function`) para preprocesamiento y métricas complejas.
- **Comando principal**: `lm_eval --model hf --tasks <nombre_tarea> --include_path <ruta>`.

## Etiquetas
#mlops #evaluación_llm #custom_tasks #python

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\mlops\evaluation\lm-evaluation-harness\references\custom-tasks.md`
