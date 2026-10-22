---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/ssyhape-pixel/opencode-scale"
tema: "Temporal Workflow Observability"
tags: [web]
---
# ssyhape-pixel/opencode-scale

## Resumen
Este proyecto es una capa de orquestación industrial para instancias escalables del servidor OpenCode Server, capaz de manejar cientos o miles de sesiones de agentes concurrentes. Utiliza una arquitectura basada en Kubernetes y Temporal para gestionar entornos aislados (sandboxes) y flujos de trabajo complejos de codificación con total observabilidad.

## Datos clave
- **Arquitectura**: Kong Gateway -> Router (Go) -> Sandbox (K8s gVisor) / Temporal Server.
- **Componentes principales**: Router (afinidad de sesión), Controller (gestión de vida útil), Worker (5 actividades), Pool Manager (caché y GC).
- **Stack tecnológico**: Go 1.25, Kong 3.x, Temporal 1.24+, LiteLLM, OpenTelemetry + Prometheus + Grafana.
- **Configuración importante**: `POOL_MODE` (local/k8s), `POOL_MIN_READY`, `POOL_MAX_SIZE`, `API_KEYS`.
- **Comandos de despliegue**: `make compose-up`, `helm install opencode-scale ./charts/opencode-scale`, `make deploy-prod`.

## Etiquetas
#opencode #kubernetes #temporal #go #devops

Fuente: https://github.com/ssyhape-pixel/opencode-scale
