---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/ttys3/axum-otel-metrics"
tema: "OpenTelemetry Metrics Exporters"
tags: [web]
---
# ttys3/axum-otel-metrics

## Resumen
Este proyecto es middleware para el framework web Rust Axum que facilita la recolección y exportación de métricas mediante OpenTelemetry. Actualmente, solo soporta el exportador OTLP (gRPC o HTTP), habiendo eliminado el soporte para Prometheus debido a vulnerabilidades de seguridad en sus dependencias.

## Datos clave
- **Exportadores activos:** Solo OTLP (`opentelemetry_otlp`); se recomienda usarlo con Prometheus nativo.
- **Variables de entorno:** `OTEL_EXPORTER_OTLP_ENDPOINT` (gRPC: 4317, HTTP: 4318) y `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT`.
- **Métricas exportadas (Semantic Conventions):** `http.server.active_requests`, `http.server.request.duration`, `http.server.request.body.size`, `http.server.response.body.size`.
- **Limitación:** El exportador Prometheus fue eliminado en la versión 0.29 final por problemas de seguridad y falta de mantenimiento.

## Etiquetas
#axum #opentelemetry #rust #metrics #otlp

Fuente: https://github.com/ttys3/axum-otel-metrics
