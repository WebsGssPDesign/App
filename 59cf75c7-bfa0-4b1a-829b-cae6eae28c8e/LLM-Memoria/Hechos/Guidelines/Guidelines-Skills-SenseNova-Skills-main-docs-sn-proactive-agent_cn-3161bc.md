---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/docs/sn-proactive-agent_cn.md"
tags: [hecho]
---
# sn-proactive-agent_cn.md

## Resumen
Este documento describe el agente proactivo SenseNova, diseñado para gestionar proyectos a largo plazo extrayendo progreso de diálogos y sugiriendo acciones auditables. Su función principal es mantener el estado del proyecto en un entorno local seguro y permitir que los usuarios acepten sugerencias que se ejecutan directamente en la sesión original de Hermes.

## Datos clave
- **Componentes**: Skill `sn-proactive-agent`, CLI, Core, Web 工作台 (port 8080) y Hermes Connector.
- **Requisitos**: Python 3.11+, Node.js 22+, `pipx`.
- **Ruta de datos**: `~/.sn-proactive-agent/` para proyectos, items y registros de ejecución (`runtime.jsonl`).
- **Comandos críticos**:
    - Descarga: `gh release download ... --pattern sn_proactive_agent-0.1.3-py3-none-any.whl`.
    - Instalación: `pipx install --python "$SNPA_PYTHON" "$SNPA_PACKAGE"`.
    - Configuración: `sn-proactive-agent setup --harness hermes --hermes-root "$SNPA_HERMES_ROOT"`.
    - Servicio: `sn-proactive-agent serve --web-only`.
- **Flujo de acción**: El usuario acepta una sugerencia en la Web UI, y el Connector ejecuta la acción en la sesión Hermes original devolviendo el resultado con `source_suggestion_id`.

## Etiquetas
#SenseNova #ProactiveAgent #Hermes #Automatización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\docs\sn-proactive-agent_cn.md`
