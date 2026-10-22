---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/mlops/evaluation/lm-evaluation-harness/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe `lm-evaluation-harness`, una herramienta estándar de la industria para evaluar modelos de lenguaje grandes (LLMs) en más de 60 benchmarks académicos como MMLU, GSM8K y HumanEval. Sirve para medir la calidad del modelo, comparar diferentes versiones y monitorear el progreso durante el entrenamiento mediante métricas estandarizadas.

## Datos clave
- **Proyecto**: lm-evaluation-harness (lm-eval).
- **Tecnologías**: Python, HuggingFace Transformers, vLLM, PyTorch Lightning.
- **Decisiones de diseño**: Soporte nativo para modelos cuantizados (4-bit/8-bit) y ejecución en GPU (`cuda:0`).
- **Comandos principales**: `pip install lm-eval`, `lm_eval --model hf --tasks mmlu,gsm8k`.
- **Pasos críticos**: Selección de suite de benchmarks, configuración del modelo (checkpoint o API), ejecución con parámetros como `--num_fewshot` y análisis de resultados JSON.
- **Flujos de trabajo**: Evaluación estándar, monitoreo periódico durante el entrenamiento (cada N pasos) y comparación entre múltiples modelos.

## Etiquetas
#MLOps #LLMEvaluation #Benchmarking #HuggingFace #Python

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\mlops\evaluation\lm-evaluation-harness\SKILL.md`
