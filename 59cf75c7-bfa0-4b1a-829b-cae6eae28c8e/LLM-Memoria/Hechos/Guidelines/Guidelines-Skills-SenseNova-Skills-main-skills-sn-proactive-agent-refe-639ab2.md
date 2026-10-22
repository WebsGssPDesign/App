---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-proactive-agent/references/connectors/hermes.md"
tags: [hecho]
---
# hermes.md

## Resumen
Este documento detalla la integración del componente de Hermes para el agente proactivo, cubriendo la instalación del conector web, la configuración de rutas y los pasos de verificación. Su función es permitir que el sistema capture diálogos en tiempo real, genere sugerencias en la interfaz web y ejecute acciones aprobadas dentro de la sesión original sin modificar el flujo nativo de Hermes.

## Datos clave
- **Proyecto**: Integración del conector `sn-proactive-agent` para Hermes (versión base `b03c94db...`).
- **Tecnologías**: Node.js 22+, Python, TUI (Terminal User Interface), Web-only bridge.
- **Variables críticas**: `$SNPA_HERMES_ROOT`, `$HERMES_HOME`, `$SN_PROACTIVE_AGENT_SERVICE_URL`, `$SNPA_SESSION_ID`.
- **Comandos principales**:
    - `sn-proactive-agent setup --harness hermes --web-only` (Instalación).
    - `hermes --tui --accept-hooks` (Reinicio del entorno de diálogo).
    - `sn-proactive-agent doctor --harness hermes ... --json` (Diagnóstico y verificación de estado).
- **Flujo de aceptación**: Captura de turnos (`turn.started`/`completed`) -> Sugerencia en Web -> Ejecución visible tras aprobación del usuario.

## Etiquetas
#Hermes #Integración #Automatización #AgentesIA #Desarrollo

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-proactive-agent\references\connectors\hermes.md`
