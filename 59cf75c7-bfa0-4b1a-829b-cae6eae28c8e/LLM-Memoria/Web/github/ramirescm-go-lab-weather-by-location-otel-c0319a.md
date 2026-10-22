---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/ramirescm/go-lab-weather-by-location-otel"
tema: "OpenTelemetry Attribute Propagation"
tags: [web]
---
# ramirescm/go-lab-weather-by-location-otel

## Resumen
Este proyecto es una extensión orientada a la observabilidad del sistema de clima Weather System, que implementa trazado distribuido completo mediante OpenTelemetry. Instrumenta servicios en Go para exportar spans al OTEL Collector y visualizar el ciclo de vida de las solicitudes en Zipkin. Incluye características como atributos personalizados, propagación de contexto entre goroutines y análisis de cuellos de botella.

## Datos clave
- **Comandos principales**: `docker-compose up -d` (ejecución completa), `docker compose up -d zipkin otel-collector` (solo infraestructura).
- **Endpoints útiles**: Zipkin (`http://localhost:9411`), zPages del Collector (`http://localhost:55679/debug/tracez`), BFF API (`http://localhost:8080`).
- **Configuración de depuración**: Ajustar `otel-collector-config.yaml` usando `endpoint: 0.0.0.0:4317` para recibir datos locales.
- **Servicios involucrados**: BFF, Orchestrator, OTEL Collector y Zipkin.
- **Pruebas de API**: Requieren una clave `x-api-key` válida (ej. OpenWeather) y un código postal válido (cep).

## Etiquetas
#observabilidad #OpenTelemetry #DistributedTracing #Go #Zipkin

Fuente: https://github.com/ramirescm/go-lab-weather-by-location-otel
