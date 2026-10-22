---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/mlops/inference/llama-cpp/references/server.md"
tags: [hecho]
---
# server.md

## Resumen
Este documento describe la guía de despliegue en producción del servidor llama.cpp, configurado para ofrecer una API compatible con OpenAI. Proporciona instrucciones detalladas para iniciar el servicio localmente o mediante contenedores Docker, gestionar modelos desde Hugging Face y optimizar el rendimiento mediante técnicas como agrupación continua y caché de contexto.

## Datos clave
- **Proyecto**: Despliegue del servidor llama.cpp (inference).
- **Tecnologías**: llama-server, NVIDIA CUDA (-ngl), Docker, NGINX para balanceo de carga.
- **Decisiones**: Uso de modelos GGUF cuantizados; habilitación de aceleración GPU; implementación de API compatible con OpenAI.
- **Rutas importantes**: `/v1/chat/completions` (chat y streaming), `/metrics`, `/health`.
- **Comandos clave**: `llama-server -hf <repo>`, `docker run --gpus all`, configuración NGINX upstream, flags `-np` para paralelismo y `--cont-batching` para agrupación continua.

## Etiquetas
#mlops #llama-cpp #inference #deployment #gpu

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\mlops\inference\llama-cpp\references\server.md`
