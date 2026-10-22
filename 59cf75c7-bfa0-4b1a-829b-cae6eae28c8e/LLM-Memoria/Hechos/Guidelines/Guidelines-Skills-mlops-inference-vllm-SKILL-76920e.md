---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/mlops/inference/vllm/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento es una guía técnica para implementar vLLM, un sistema de alto rendimiento para servir modelos de lenguaje grandes (LLMs) en producción. Su objetivo principal es optimizar la latencia y el throughput mediante técnicas como PagedAttention, batching continuo y cuantización, ofreciendo endpoints compatibles con la API de OpenAI.

## Datos clave
- **Tecnologías**: vLLM, PyTorch, Transformers, Docker, Prometheus (monitoreo), Locust (pruebas de carga).
- **Decisiones técnicas**: Uso de PagedAttention para gestión eficiente del caché KV; soporte para cuantización (AWQ, GPTQ, FP8) y paralelismo tensorial.
- **Comandos y pasos críticos**:
  - Instalación: `pip install vllm`.
  - Servidor básico: `vllm serve <modelo> --gpu-memory-utilization 0.9`.
  - Paralelismo tensorial (ej. modelos grandes): `--tensor-parallel-size 4 --quantization awq`.
  - Habilitar métricas: `--enable-metrics --metrics-port 9090`.
  - Despliegue en Docker: `docker run --gpus all ... vllm/vllm-openai:latest`.
- **Métricas de rendimiento**: Tiempo al primer token (TTFT) < 500ms y throughput > 100 req/sec.

## Etiquetas
#vLLM #InferenceServing #LLMOps #HighThroughput #ProductionReady

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\mlops\inference\vllm\SKILL.md`
