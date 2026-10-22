---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://github.com/oracle/oracle-db-appdev-monitoring"
tema: "OpenTelemetry Exporters"
tags: [web]
---
# oracle/oracle-db-appdev-monitoring

## Resumen
Este proyecto ofrece un exportador de métricas para Oracle AI Database que facilita la observabilidad al recopilar datos de rendimiento y diagnosticar problemas. Permite enviar métricas a Prometheus o a un backend de OpenTelemetry mediante OTLP/gRPC, funcionando en entornos locales, nube o Kubernetes con soporte para instancias autónomas. Incluye características avanzadas como autenticación segura, personalización de métricas y dashboards preconfigurados para Grafana.

## Datos clave
- **Formatos de exportación:** Métricas Prometheus (endpoint `/metrics`) y OpenTelemetry (OTLP/gRPC).
- **Soporte de entornos:** On-premises, nube pública/privada y Kubernetes (instancias únicas o en cluster).
- **Autenticación:** Soporta texto plano, TLS, Oracle Wallet y gestión segura con OCI Vault, Azure Vault o HashiCorp Vault.
- **Funcionalidades:** Recolección de alertas en formato JSON, imágenes precompiladas para AMD64/ARM64 y definición de métricas personalizadas vía YAML/TOML.
- **Integración:** Disponible como componente nativo para Grafana Alloy e incluye dashboards de ejemplo.

## Etiquetas
#OracleAI #Monitoring #Prometheus #OpenTelemetry #DevOps

Fuente: https://github.com/oracle/oracle-db-appdev-monitoring
