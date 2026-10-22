---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/sjqtentacles/sml-otel"
tema: "OpenTelemetry Attribute Propagation"
tags: [web]
---
# sjqtentacles/sml-otel

## Resumen
Este repositorio presenta `sml-otel`, una implementación de modelos de trazas y spans del estándar OpenTelemetry escrita en Standard ML. La biblioteca permite crear jerarquías de trazas compatibles con W3C, propagar contexto mediante cabeceras HTTP y exportar datos a formato JSON determinista para visualización o análisis posterior.

## Datos clave
- **Funciones principales**: `Otel.newTrace` (iniciar traza), `Otel.childSpan` (crear span hijo), `Otel.inject/extract` (propagación W3C traceparent), `Otel.toJson/spansToJson` (exporto JSON).
- **Tipos de datos**: `span`, `traceId` (32 hex), `spanId` (16 hex), `status` (Ok/Error/Unset), `kind` (Server, Client, etc.).
- **Limitaciones**: Funciona solo en memoria sin exportador de red; los IDs se generan determinísticamente (no criptográficos); no soporta cabeceras `tracestate` ni `baggage`.
- **Instalación**: Se instala vía `smlpkg add github.com/sjqtentacles/sml-otel`.

## Etiquetas
#OpenTelemetry #StandardML #Trazabilidad #DistributedTracing #W3CTraceparent

Fuente: https://github.com/sjqtentacles/sml-otel
