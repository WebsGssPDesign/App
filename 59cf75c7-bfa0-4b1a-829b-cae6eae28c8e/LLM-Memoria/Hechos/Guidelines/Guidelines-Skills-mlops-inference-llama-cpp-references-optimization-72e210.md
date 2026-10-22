---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/mlops/inference/llama-cpp/references/optimization.md"
tags: [hecho]
---
# optimization.md

## Resumen
Esta guía detalla estrategias para optimizar la velocidad y eficiencia de inferencia en modelos Llama utilizando llama.cpp, cubiendo ajustes de CPU, offloading a GPU y gestión de memoria. Su objetivo es ayudar a los usuarios a configurar parámetros como hilos, capas en GPU y tamaño de lote para maximizar el rendimiento según su hardware específico.

## Datos clave
- **CPU**: Usar `-t` igual al número de núcleos físicos (evitar hyperthreading) y compilar con `LLAMA_OPENBLAS=1` para aceleración de matrices 2-3x.
- **GPU Offloading**: Parámetro `-ngl` para mover capas a GPU; iniciar en 999 y reducir si hay OOM. Ejemplo: `-ngl 35`.
- **Batching**: Aumentar tamaño de lote con `-b` (ej. 512) y usar `--ubatch` para procesamiento físico en GPU.
- **Contexto**: Controlar memoria con `-c`; reducir de 4K a 2K si es necesario.
- **Rendimiento**: RTX 4090 alcanza 120 tok/s offloading todo (35 capas) vs 30 tok/s solo CPU. Apple M3 Max llega a 50 tok/s con Metal.

## Etiquetas
#llama-cpp #optimización #inferenciaGPU #MLOps

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\mlops\inference\llama-cpp\references\optimization.md`
