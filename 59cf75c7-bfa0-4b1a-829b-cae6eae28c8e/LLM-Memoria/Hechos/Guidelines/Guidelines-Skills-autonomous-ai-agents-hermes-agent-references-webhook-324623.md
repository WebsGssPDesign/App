---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/autonomous-ai-agents/hermes-agent/references/webhooks.md"
tags: [hecho]
---
# webhooks.md

## Resumen
Este documento describe cómo configurar y gestionar suscripciones de webhooks en el agente Hermes para permitir que servicios externos (como GitHub, Stripe o sensores IoT) desencadenen ejecuciones automáticas. Sirve como guía práctica para habilitar la plataforma, crear reglas de filtrado de eventos y definir plantillas de prompts personalizadas para diversas integraciones.

## Datos clave
- **Configuración inicial**: Habilitar la plataforma con `hermes gateway setup` o editando `~/.hermes/config.yaml` (usando variables de entorno como alternativa). Verificar con `curl http://localhost:8644/health`.
- **Comandos principales**: Crear suscripciones (`hermes webhook subscribe`), listarlas, eliminarlas y probarlas (`hermes webhook test`).
- **Filtrado de payloads**: Uso de filtros declarativos en `config.yaml` o scripts personalizados (`.sh`/`.py`) para procesar la entrada JSON antes de enviarla al agente.
- **Plantillas de prompts**: Acceso a campos anidados del payload mediante notación punto (ej: `{issue.title}`) y envío directo sin LLM usando `--deliver-only`.
- **Ejemplos de uso**: Integraciones específicas para GitHub (issues/PRs), Stripe, CI/CD y alertas genéricas.

## Etiquetas
#hermes-agent #webhooks #automatización #integración-sistemas

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\autonomous-ai-agents\hermes-agent\references\webhooks.md`
