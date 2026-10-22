---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/mlops/inference/llama-cpp/references/advanced-usage.md"
tags: [hecho]
---
# advanced-usage.md

## Resumen
Esta guía técnica detalla estrategias avanzadas para optimizar la inferencia de modelos LLM en formato GGUF, enfocándose en técnicas como decodificación especulativa, cuantización mixta y gestión eficiente de memoria. Su objetivo es mejorar el rendimiento, reducir el consumo de recursos y permitir un despliegue escalable mediante servidores con agrupamiento de solicitudes (batching).

## Datos clave
- **Decodificación**: Uso de `llama-speculative` para generación rápida con modelos "draft" o decodificación auto-especulativa con cachés estáticos/dinámicos.
- **Servidores y Batching**: Configuración de `llama-server` con flags `--parallel`, `--cont-batching` y `-ngl` para offload de GPU.
- **Cuantización**: Herramienta `llama-quantize` soporta tipos mixtos (`Q4_K_M`), embeddings de alta precisión (`--token-embedding-type f16`) y cuantización consciente del impacto (IQ2_XXS, IQ3_S).
- **Optimización de Memoria**: Uso de mapeo de memoria (`use_mmap=True`) y cálculo dinámico de capas para GPU basado en `nvidia-smi`.
- **Gestión de Contexto**: Implementación de "context shifting" en Python para mantener historiales cortos y uso de `--save-session`/`--load-session` para continuidad.
- **Conversión**: Scripts personalizados para modificar vocabularios (tokens especiales) y conversión específica por arquitectura (Mistral, Qwen, Phi).
- **Generación Restrita**: Uso de gramáticas BNF (`LlamaGrammar`) para forzar salidas JSON válidas.

## Etiquetas
#LLaMA-cpp #GGUF #InferenciaOptimizada #CuantizaciónIA #DespliegueMLOps

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\mlops\inference\llama-cpp\references\advanced-usage.md`
