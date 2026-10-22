---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/krzko/otelgen"
tema: "OpenTelemetry Synthetic Monitoring"
tags: [web]
---
# krzko/otelgen

## Resumen
`otelgen` es una herramienta diseñada para generar datos sintéticos de trazas, métricas y registros que cumplen con la especificación OpenTelemetry. Su objetivo principal es facilitar la validación rápida de configuraciones complejas en colectores OpenTelemetry mediante el envío de datos a través del protocolo OTLP (soportando tanto gRPC como HTTP).

## Datos clave
- **Señales soportadas**: Trazas (patrones single y multi), Métricas (histogramas, gauges, sumas) y Registros.
- **Instalación**: Disponible vía Homebrew (`brew install krzko/tap/otelgen`), descarga de binarios o contenedor Docker.
- **Comandos principales**: `logs`, `metrics`, `traces`.
- **Opciones globales**: `--duration` (duración en segundos), `--rate` (velocidad), `--insecure` (habilitar transporte sin seguridad para localhost).
- **Protocolos**: OTLP/gRPC y OTLP/HTTP.

## Etiquetas
#OpenTelemetry #DevOps #Testing #SyntheticData #OTLP

Fuente: https://github.com/krzko/otelgen
