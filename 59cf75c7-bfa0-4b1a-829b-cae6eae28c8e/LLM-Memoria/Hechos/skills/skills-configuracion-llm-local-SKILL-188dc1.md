---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "skills/configuracion-llm-local/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía detalla cómo configurar modelos de lenguaje grandes (LLMs) para inferencia offline utilizando herramientas como llama.cpp, vLLM y Ollama. Su objetivo es permitir la ejecución privada de modelos en hardware local mediante cuantización GGUF y compatibilidad con APIs OpenAI.

## Datos clave
- **Proyecto**: Configuración de LLMs locales (offline).
- **Tecnologías**: llama.cpp, vLLM, Ollama, formato GGUF, librería `openai`.
- **Decisiones**: Seleccionar cuantizaciones según hardware; usar `'EMPTY'` o `'ollama'` como claves API.
- **Rutas y comandos**:
  - Búsqueda de modelos: `https://huggingface.co/models?num_parameters=min:0,max:24B&apps=llama.cpp&sort=trending`.
  - Iniciar Ollama: `ollama serve` (puerto 11434).
  - Instalar vLLM: `pip install vllm`.
  - Iniciar vLLM: `vllm serve meta-llama/Llama-3-8B-Instruct` (puerto 8000).
- **Pasos**: Descargar modelo, iniciar servidor y conectar cliente Python.

## Etiquetas
#llms #inferencia-local #privacy #gpu

Fuente: `F:\automatizaciones\homeLab\skills\configuracion-llm-local\SKILL.md`
