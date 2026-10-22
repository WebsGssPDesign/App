---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/mlops/inference/llama-cpp/references/troubleshooting.md"
tags: [hecho]
---
# troubleshooting.md

## Resumen
Esta guía técnica documenta soluciones para errores comunes al instalar, convertir y ejecutar modelos de lenguaje con llama-cpp. Proporciona comandos específicos para resolver problemas de compilación (CUDA/Metal), conversión de formatos GGUF, cuantización y rendimiento en inferencia.

## Datos clave
- **Proyecto**: llama.cpp / llama-cpp-python
- **Tecnologías**: CUDA, Metal, GGUF, Flash Attention
- **Comandos críticos**: `make`, `pip install` con argumentos `CMAKE_ARGS`, `./llama-quantize`, `./llama-cli -ngl`.
- **Pasos de solución**: Instalar dependencias (`cmake`, `scikit-build-core`), verificar tamaños de vocabulario, ajustar capas GPU (`n_gpu_layers`) y usar matrices de importancia (`imatrix`) para cuantización precisa.

## Etiquetas
#llama-cpp #GGUF #MLOps #Inference

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\mlops\inference\llama-cpp\references\troubleshooting.md`
