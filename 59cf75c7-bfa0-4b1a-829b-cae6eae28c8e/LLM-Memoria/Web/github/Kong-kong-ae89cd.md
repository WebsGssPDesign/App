---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/Kong/kong"
tema: "Kubernetes Gateway API"
tags: [web]
---
# Kong/kong

## Resumen
Kong/kong es una puerta de entrada (gateway) nativa en la nube y agnóstica a plataformas diseñada para gestionar tráfico de APIs, inteligencia artificial (LLM) y Modelos de Control de Procesos (MCP). Ofrece alta performance y extensibilidad mediante plugins, actuando como capa central para orquestar microservicios y servicios de IA.

## Datos clave
- **Funcionalidades:** Proxying, enrutamiento, balanceo de carga, autenticación (JWT, OAuth) y gobernanza de tráfico MCP.
- **Soporte LLM:** Universal API para múltiples proveedores como OpenAI, Anthropic, AWS Bedrock y Azure AI.
- **Instalación:** Disponible nativamente en Kubernetes vía Ingress Controller o mediante Docker Compose (`KONG_DATABASE=postgres docker-compose --profile database up`).
- **Portes locales:** 8000 (tráfico), 8001 (API Admin/decK), 8002 (UI Kong Manager).
- **Licencia:** Apache 2.0.

## Etiquetas
#Kong #APIGateway #LLM #Kubernetes #DevOps

Fuente: https://github.com/Kong/kong
