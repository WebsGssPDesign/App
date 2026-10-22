---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://github.com/The-Vibe-Company/quivr"
tema: "PostgreSQL Vector Search"
tags: [web]
---
# The-Vibe-Company/quivr

## Resumen
Quivr V2 es un motor de código abierto que convierte flujos continuos de contenido en sistemas de búsqueda y monitoreo duraderos. Su arquitectura prioriza la integridad de los datos mediante almacenamiento canónico antes que la velocidad, permitiendo una recuperación de índices fiable y búsquedas híbridas. El núcleo del sistema está diseñado para ser genérico, delegando formatos específicos e inteligencia artificial a plugins extensibles.

## Datos clave
- **Estado:** Etapa de evaluación (API v0), no apto para producción aún.
- **Principios:** Ingesta duradera ("durable before fast"), idempotencia total y búsqueda honesta con rehidratación de datos.
- **Tecnologías:** Go (monolito modular), PostgreSQL 17 (catálogo), S3/SeaweedFS (artifacts), Temporal (orquestación), Weaviate (índices).
- **Embeddings:** Modelo local TEI (`multilingual-e5-small`, 384 dimensiones) por defecto.
- **Comandos principales:** `make dev` (iniciar entorno), `make verify` (testes end-to-end), `make demo` (interfaz web).

## Etiquetas
#QuivrV2 #BúsquedaHíbrida #OpenSource #GoLang #IngestaDuradera

Fuente: https://github.com/The-Vibe-Company/quivr
