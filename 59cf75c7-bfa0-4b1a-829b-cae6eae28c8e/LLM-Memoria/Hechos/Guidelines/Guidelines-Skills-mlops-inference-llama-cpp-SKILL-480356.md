---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/mlops/inference/llama-cpp/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía técnica define el flujo de trabajo para ejecutar inferencias locales con modelos LLM utilizando llama.cpp y archivos GGUF. Su propósito es ayudar a los usuarios a descubrir repositorios en Hugging Face, seleccionar cuantizaciones óptimas según sus recursos hardware (CPU, GPU, Apple Silicon) y generar comandos precisos para servidores o scripts de Python.

## Datos clave
- **Tecnologías**: llama-cpp-python, GGUF, Hugging Face Hub API, CUDA, Metal, ROCm.
- **Flujo de descubrimiento**: Buscar repositorios con filtros de parámetros -> Verificar compatibilidad en la vista `?local-app=llama.cpp` -> Confirmar archivos `.gguf` mediante el endpoint del Tree API (`/api/models/<repo>/tree`).
- **Comandos principales**: `llama-server -hf <repo>:<quant>`, `llama-cli`, instalación vía `brew install llama.cpp`.
- **Selección de cuantización**: Preferir etiquetas exactas del repositorio (ej. `UD-Q4_K_M`); usar `Q4_K_M` para chat general y `Q5/Q6` para tareas técnicas si hay memoria disponible.
- **Python bindings**: Uso de `Llama.from_pretrained` para cargar modelos directamente desde el Hub con filtros de archivo.

## Etiquetas
#llama-cpp #GGUF #InferenciaLocal #MLOps #HuggingFace

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\mlops\inference\llama-cpp\SKILL.md`
