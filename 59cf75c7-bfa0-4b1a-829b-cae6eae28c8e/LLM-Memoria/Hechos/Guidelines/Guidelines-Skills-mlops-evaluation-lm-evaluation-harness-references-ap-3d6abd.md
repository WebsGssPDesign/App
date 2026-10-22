---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/mlops/evaluation/lm-evaluation-harness/references/api-evaluation.md"
tags: [hecho]
---
# api-evaluation.md

## Resumen
Esta guía detalla cómo utilizar la herramienta `lm-evaluation-harness` para evaluar modelos de lenguaje basados en APIs, como los de OpenAI y Anthropic, así como servidores locales compatibles. Permite comparar el rendimiento de modelos cerrados con otros, validar actualizaciones y gestionar costos mediante configuraciones específicas para tareas de generación o probabilidad logística.

## Datos clave
- **Tecnologías**: `lm-evaluation-harness`, interfaces `TemplateAPI`.
- **Modelos soportados**: OpenAI (GPT-4, GPT-3.5), Anthropic (Claude 3/2) y locales (vLLM, TGI, Ollama, llama.cpp).
- **Restricciones críticas**: Los modelos de chat no devuelven `logprobs`, limitando su uso a tareas de generación (`generate_until`) y excluyendo métricas como perplexidad.
- **Comandos clave**: Uso de `--model_args` para definir endpoints, concurrencia (`num_concurrent`) y reintentos; parámetros `--limit` y `--batch_size auto` para optimización.
- **Gestión de costos**: Estrategias de prueba inicial con modelos más baratos (ej. GPT-3.5 o Claude Haiku) antes de escalar a versiones premium, y cálculo manual de gastos por tokens.

## Etiquetas
#MLOps #EvaluaciónLLM #APIs #OpenAI #Anthropic

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\mlops\evaluation\lm-evaluation-harness\references\api-evaluation.md`
