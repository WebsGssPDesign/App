---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/mlops/evaluation/lm-evaluation-harness/references/benchmark-guide.md"
tags: [hecho]
---
# benchmark-guide.md

## Resumen
Esta guía detalla más de 60 tareas de evaluación disponibles en lm-evaluation-harness, cubriendo áreas como comprensión lingüística, razonamiento matemático y generación de código. Su función principal es ayudar a los desarrolladores a medir el rendimiento de modelos de lenguaje grandes (LLMs) mediante benchmarks estandarizados e interpretar los resultados obtenidos.

## Datos clave
- **Tecnologías**: lm-evaluation-harness, Hugging Face (`hf`), modelos como Llama-2, CodeLlama y BERT.
- **Benchmarks principales**: MMLU (conocimiento general), GSM8K (matemáticas), HumanEval (código Python), BBH (razonamiento complejo), IFEval (seguimiento de instrucciones) y LongBench (contexto largo).
- **Comandos importantes**: `lm_eval --tasks list` para enumerar todas las tareas; uso de argumentos como `--model_args pretrained=...`, `--num_fewshot` y `--batch_size`.
- **Decisiones clave**: Selección del modelo adecuado según la tarea (ej. BERT para GLUE, CodeLlama para HumanEval) y ajuste de parámetros de few-shot learning.

## Etiquetas
#MLOps #EvaluaciónLLM #Benchmarks #Python #IA

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\mlops\evaluation\lm-evaluation-harness\references\benchmark-guide.md`
