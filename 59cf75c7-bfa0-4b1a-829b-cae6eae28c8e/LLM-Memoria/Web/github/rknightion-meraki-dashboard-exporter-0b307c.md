---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/rknightion/meraki-dashboard-exporter"
tema: "OpenTelemetry OTLP Exporters"
tags: [web]
---
# rknightion/meraki-dashboard-exporter

## Resumen
Este proyecto es un exportador de métricas y un colector OpenTelemetry diseñado para extraer datos de la API del panel de control Cisco Meraki. Proporciona métricas listas para ser raspadas por Prometheus, exportación nativa OTLP e incluye tableros de Grafana preconfigurados para monitorizar dispositivos, redes y sensores MT.

## Datos clave
- **Funcionalidad**: Exporta métricas de dispositivos (MS, MR, MV, MT, MX, MG), uso de API, licencias y alertas de salud.
- **Endpoints**: `/metrics` para Prometheus, `/status`, `/health`, `/ready`.
- **Despliegue**: Soporte nativo para Docker (`docker compose up -d`) y Kubernetes (Helm charts en GHCR).
- **Configuración**: Requiere la variable de entorno `MERAKI_EXPORTER_MERAKI__API_KEY` con la clave de API del usuario.
- **Portabilidad**: Endpoint de API regional configurable; incluye caché compartido de inventario para optimizar consultas.
- **Limitaciones**: El soporte para tipos de dispositivos MX, MG y MV es "best-effort" ya que el autor no tiene acceso a hardware de esos modelos actualmente.

## Etiquetas
#CiscoMeraki #Prometheus #OpenTelemetry #DevOps #Monitorización

Fuente: https://github.com/rknightion/meraki-dashboard-exporter
