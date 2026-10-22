---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/productivity/teams-meeting-pipeline/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe cómo operar el pipeline de resúmenes de reuniones de Microsoft Teams utilizando la CLI Hermes. Su función principal es gestionar suscripciones a Microsoft Graph para obtener transcripciones, inspeccionar el estado del sistema y reejecutar tareas fallidas sin intervención manual en el modelo.

## Datos clave
- **Prerrequisitos**: Variables de entorno `MSGRAPH_TENANT_ID`, `MSGRAPH_CLIENT_ID` y `MSGRAPH_CLIENT_SECRET`.
- **Comandos principales**: `hermes teams-pipeline validate` (validación inicial), `list --status failed` (diagnóstico), `run <job-id>` (reprocesamiento) y `maintain-subscriptions` (renovación automática).
- **Punto crítico**: Las suscripciones de webhook de Microsoft Graph expiran en 72 horas y no se renuevan automáticamente; es obligatorio configurar un cron o systemd timer para evitar interrupciones.
- **Flujo de trabajo**: Para problemas de entrega, verificar primero el estado del job (`show <job-id>`) y luego las suscripciones activas.

## Etiquetas
#MicrosoftTeams #PipelineAutomation #MicrosoftGraph #DevOps

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\productivity\teams-meeting-pipeline\SKILL.md`
