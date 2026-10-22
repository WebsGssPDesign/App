---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/mlops/inference/vllm/references/optimization.md"
tags: [hecho]
---
# optimization.md

## Resumen
Este documento detalla las técnicas de optimización para el motor de inferencia vLLM, enfocándose en la gestión eficiente de memoria y el aumento del throughput mediante estrategias como PagedAttention y batching continuo. Su objetivo principal es guiar a los ingenieros para configurar vLLM de manera que maximice el uso de GPUs (A100) y reduzca significativamente los tiempos de latencia y consumo de recursos comparado con implementaciones estándar.

## Datos clave
- **Tecnologías**: vLLM, PagedAttention, Continuous Batching, Speculative Decoding, Prefix Caching.
- **Decisiones**: Uso de bloques de memoria fragmentados para reducir el desperdicio de VRAM; mezcla dinámica de prefill y decode.
- **Comandos importantes**: `--block-size 16`, `--gpu-memory-utilization 0.9`, `--max-num-seqs 256`, `--enable-prefix-caching`.
- **Rutas de benchmarking**: Uso de `locust` para medir throughput y TTFT; métricas disponibles en `/metrics`.
- **Comparativas**: vLLM supera a HuggingFace Transformers (23x más throughput) y ofrece mayor flexibilidad que TensorRT-LLM.

## Etiquetas
#vllm #optimización #inferencia_llm #gpu_memory #performance_tuning

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\mlops\inference\vllm\references\optimization.md`
