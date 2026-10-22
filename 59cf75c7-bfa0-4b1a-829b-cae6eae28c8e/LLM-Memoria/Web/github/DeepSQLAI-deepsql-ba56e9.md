---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/DeepSQLAI/deepsql"
tema: "PostgreSQL pgvector Indexes"
tags: [web]
---
# DeepSQLAI/deepsql

## Resumen
DeepSQL es un agente autónomo para bases de datos PostgreSQL y MySQL que permite realizar consultas, analizar rendimiento y generar recomendaciones en lenguaje natural. Funciona como una solución auto-alojada (self-hosted) donde el usuario gestiona completamente la infraestructura y los modelos de IA, garantizando privacidad y aislamiento de red sin depender de proveedores externos.

## Datos clave
- **Requisitos técnicos:** Docker Engine con Compose v2 y buildx (versión ≥0.17.0), Git, curl, openssl y 4 GB de RAM disponibles para el backend JVM.
- **Instalación rápida:** `curl -fsSL https://deepsql.ai/install.sh | bash` o uso del script `bootstrap-server.sh`.
- **Configuración de modelos:** Variables `.env` (`DEEPSQL_CHAT_PROVIDER`, `API_KEY`, `ENDPOINT`, `MODEL`) compatibles con OpenAI, Azure, Anthropic y modelos locales (Ollama, vLLM).
- **Funcionalidades principales:** Exploración de esquemas, generación de consultas SQL, análisis de consultas lentas, recomendaciones de índices y dashboards.
- **Seguridad:** Credenciales encriptadas localmente; no salen datos del entorno salvo los prompts enviados al endpoint elegido.

## Etiquetas
#DeepSQL #IAparaBD #PostgreSQL #MySQL #AutoAlojado

Fuente: https://github.com/DeepSQLAI/deepsql
