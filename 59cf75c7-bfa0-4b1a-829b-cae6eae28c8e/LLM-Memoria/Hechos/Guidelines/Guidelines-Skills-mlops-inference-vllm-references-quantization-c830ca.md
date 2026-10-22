---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/mlops/inference/vllm/references/quantization.md"
tags: [hecho]
---
# quantization.md

## Resumen
Esta guía técnica detalla métodos de cuantización para optimizar modelos de lenguaje en vLLM, equilibrando velocidad, memoria y precisión. Sirve como referencia práctica para seleccionar entre técnicas como AWQ, GPTQ o FP8 según el hardware disponible y los requisitos del despliegue productivo.

## Datos clave
- **Comparativa**: AWQ (4-bit) es ideal para modelos de 70B en GPUs estándar; FP8 ofrece mayor velocidad exclusiva para H100/H800; GPTQ garantiza máxima compatibilidad.
- **Comandos vLLM**: Uso de `--quantization awq`, `gptq` o `fp8`; ejemplo de lanzamiento: `vllm serve TheBloke/Llama-2-70B-AWQ --tensor-parallel-size 1`.
- **Optimización memoria**: Cuantización AWQ reduce VRAM de 140GB a 35GB para Llama 2 70B.
- **Requisitos FP8**: GPU Hopper (H100), CUDA 12.3+, sin necesidad de pre-cuantizar el modelo.
- **Cálculo propio**: Uso de `AutoAWQForCausalLM` y `BaseQuantizeConfig`; requiere datos de calibración (128-512 ejemplos) para GPTQ.

## Etiquetas
#mlops #vllm #cuantización #optimización_modelos #inferencia

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\mlops\inference\vllm\references\quantization.md`
