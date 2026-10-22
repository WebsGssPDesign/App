---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/mlops/inference/llama-cpp/references/hub-discovery.md"
tags: [hecho]
---
# hub-discovery.md

## Resumen
Este documento establece un flujo de trabajo basado exclusivamente en URLs para descubrir modelos compatibles con llama.cpp en Hugging Face sin depender de clientes de API. Su objetivo es guiar al usuario desde la búsqueda inicial hasta la construcción del comando exacto de ejecución, priorizando la información visible en la interfaz local-app y validando los archivos mediante la API del árbol de repositorio.

## Datos clave
- **Proyecto**: Integración de llama.cpp con Hugging Face Hub.
- **Tecnologías**: URLs de búsqueda (`apps=llama.cpp`), vista `local-app`, API `/api/models/<repo>/tree/main`.
- **Decisiones**: Priorizar la etiqueta de cuantización exacta del repositorio sobre abreviaturas genéricas; separar archivos `.gguf` principales de proyectores (`mmproj`) y shards BF16.
- **Comandos importantes**: `llama-server -hf <repo>:<QUANT>` para uso estándar o `--hf-file <filename.gguf>` cuando la cuantización no es estándar.
- **Pasos críticos**: 1) Buscar modelos con filtros de parámetros; 2) Extraer compatibilidad de hardware del snippet local-app; 3) Confirmar inventario y tamaños vía JSON API; 4) Generar comando final.

## Etiquetas
#llama-cpp #hugging-face #mlops #inference #gguf

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\mlops\inference\llama-cpp\references\hub-discovery.md`
