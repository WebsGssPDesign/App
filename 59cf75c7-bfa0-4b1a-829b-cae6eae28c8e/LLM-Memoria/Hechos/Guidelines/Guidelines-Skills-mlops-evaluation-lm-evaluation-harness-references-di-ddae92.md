---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/mlops/evaluation/lm-evaluation-harness/references/distributed-eval.md"
tags: [hecho]
---
# distributed-eval.md

## Resumen
Esta guía explica cómo acelerar la evaluación de modelos de lenguaje distribuyendo tareas entre múltiples GPUs mediante paralelismo de datos o tensores. Permite evaluar modelos grandes que no caben en una sola tarjeta gráfica y optimiza el rendimiento para benchmarks como MMLU o GSM8K usando frameworks como HuggingFace, vLLM o NeMo.

## Datos clave
- **Paralelismos**: Data Parallelism (copias completas del modelo), Tensor Parallelism (pesos divididos) y Pipeline Parallelism (capas divididas).
- **HuggingFace (`hf`)**: Usa `accelerate launch` para multi-GPU; requiere memoria total del modelo en cada GPU. Para modelos grandes, usa `parallelize=True`.
- **vLLM**: Soporta Tensor Parallelism nativo y Data Parallelism con múltiples réplicas; para multi-nodo se requiere Ray.
- **NVIDIA NeMo (`nemo_lm`)**: Usa `torchrun`; combina TP y PP donde `devices = TP × PP`. No soporta multi-nodo actualmente.
- **SGLang**: Prefiere Tensor Parallelism; el Data Parallelism está siendo deprecado.
- **Comandos clave**: `accelerate launch`, `lm_eval --model hf/vllm/nemo_lm/sglang`, `torchrun`.

## Etiquetas
#MLOps #DistributedComputing #LLMEvaluation #GPUParallelism

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\mlops\evaluation\lm-evaluation-harness\references\distributed-eval.md`
