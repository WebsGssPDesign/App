---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/rknightion/tailscale2otel"
tema: "OpenTelemetry OTLP Exporters"
tags: [web]
---
# rknightion/tailscale2otel

## Resumen
tailscale2otel es un exportador escrito en Go que convierte datos de la flota de Tailscale (como registros de flujo y auditoría) en métricas y logs compatibles con OpenTelemetry y Prometheus. La herramienta permite monitorear el estado de la red, cambios de configuración y salud del nodo desde una única instancia binaria estática, integrándose fácilmente con Grafana Cloud.

## Datos clave
- **336 métricas** + 31 tipos de eventos de log recolectados a través de 17 colectores.
- Soporta múltiples vías de ingestión: polling de API, streams de logs (compatible Splunk-HEC), exportación desde S3 y webhooks verificados con HMAC.
- Incluye enriquecimiento offline de GeoIP y ASN usando bases de datos locales MaxMind (.mmdb).
- Ofrece controles de privacidad (PII) para redactar categorías sensibles como correos, IPs y hostnames.
- Funciona en modo multi-tailnet y soporta la implementación Headscale con un conjunto reducido de colectores.

## Etiquetas
#Tailscale #OpenTelemetry #Prometheus #Grafana #Observabilidad

Fuente: https://github.com/rknightion/tailscale2otel
