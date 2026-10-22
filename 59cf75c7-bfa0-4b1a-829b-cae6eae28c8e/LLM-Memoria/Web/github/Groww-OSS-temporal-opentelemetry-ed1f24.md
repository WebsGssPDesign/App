---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/Groww-OSS/temporal-opentelemetry"
tema: "Temporal Activity Execution"
tags: [web]
---
# Groww-OSS/temporal-opentelemetry

## Resumen
Este módulo ofrece interceptores para el SDK de Java de Temporal que habilitan la propagación del contexto de trazas de OpenTelemetry. Su objetivo es permitir rastrear tanto las ejecuciones de Workflows como las de Activities dentro del ecosistema temporal.

## Datos clave
- **Componentes principales**: `OpenTelemetryClientInterceptor` (lado cliente) y `OpenTelemetryWorkerInterceptor` (lado worker).
- **Funcionalidad**: Propagación de contexto de traza (Span Context).
- **Implementación**: Requiere configurar ambos interceptores mediante `.setInterceptors()` en el cliente y `.setWorkerInterceptors()` en el worker.

## Etiquetas
#temporal #opentelemetry #java-sdks #tracing #microservicios

Fuente: https://github.com/Groww-OSS/temporal-opentelemetry
