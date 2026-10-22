---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/KnigguKniggu-droid/14-agentic-workflow-orchestrator"
tema: "Temporal Workflow State Machines"
tags: [web]
---
# KnigguKniggu-droid/14-agentic-workflow-orchestrator

## Resumen
Este repositorio es un espacio de trabajo de ingeniería de IA que contiene 15 plantillas especializadas diseñadas para producción. Cada proyecto sigue una arquitectura estandarizada con contratos tipificados, capas de configuración y orquestación de servicios mediante Docker. El enfoque centraliza la robustez técnica en sistemas como detección de regresión de modelos, optimización de costos y gestión de flujos agénticos multiagente.

## Datos clave
- **Arquitectura estandarizada**: Uso obligatorio de Pydantic para contratos tipados, YAML/TOML para configuración y Dockerfile para despliegue.
- **Infraestructura compartida**: Orquestación centralizada de Redis, PostgreSQL y ClickHouse vía `docker-compose.infra.yml`.
- **Flujo de trabajo agéntico (Proyecto 14)**: Gestiona flujos multiagente con máquinas de estado, puntos de control humanos y transacciones de compensación.
- **Tecnologías destacadas**: FastAPI como capa de servicio, GitHub Actions para CI/CD, y herramientas específicas como LangGraph o ChromaDB según el caso de uso.
- **Seguridad y calidad**: Implementación de guardrails para SQL, pruebas unitarias con pytest y análisis estadístico para A/B testing de prompts.

## Etiquetas
#IngenieríaDeIA #OrquestaciónAgéntica #DevOpsAI #ArquitecturaSistemas

Fuente: https://github.com/KnigguKniggu-droid/14-agentic-workflow-orchestrator
