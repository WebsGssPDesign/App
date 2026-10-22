---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/uniquejava/icm-tracing"
tema: "Temporal Activity Heartbeat"
tags: [web]
---
# uniquejava/icm-tracing

## Resumen
Este repositorio ofrece demostraciones prácticas que exploran las limitaciones de la trazabilidad en sistemas basados en Temporal y OpenTelemetry. A través de varias ramas, el proyecto ilustra cómo manejar casos complejos como reintentos de actividades, intervención humana (HITL) y mantenimientos de latencia larga mediante latidos (heartbeats).

## Datos clave
- **Tecnologías**: Java 25, Maven 3.9.x, Temporal CLI, Docker/Docker Compose.
- **Objetivo principal**: Detectar problemas en trazas cuando se combinan reintentos con enlaces de traza (Span Links) o intervenciones humanas.
- **Ramas destacadas**: `retry` (reintentos), `hitl` (intervención humana), `heartbeat_retry` (latidos para evitar fragmentación de trazas).
- **Configuración**: Requiere claves de API de New Relic y Datadog en un archivo `.env`.
- **Comandos principales**: `./scripts/startup.sh` (infraestructura), `mvn clean spring-boot:run` (aplicación), `./scripts/01normal.sh` (disparar flujo).

## Etiquetas
#temporal #opentelemetry #tracing #java #devops

Fuente: https://github.com/uniquejava/icm-tracing
