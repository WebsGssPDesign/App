---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/docs/sn-proactive-agent.md"
tags: [hecho]
---
# sn-proactive-agent.md

## Resumen
Este documento describe el agente proactivo SenseNova, diseñado para gestionar proyectos a largo plazo, auditar estados y sugerir acciones dentro de un entorno web. Su función principal es capturar conversaciones, generar recomendaciones inteligentes y ejecutar tareas aceptadas directamente en la sesión original de Hermes sin perder contexto.

## Datos clave
- **Componentes**: Skill (lógica), Runtime package (CLI y Web workbench), Hermes Connector (integración).
- **Requisitos**: Python 3.11+, Node.js 22+, instalación vía `pipx` desde releases oficiales de GitHub.
- **Instalación**: Copia del directorio `skills/sn-proactive-agent/`, descarga verificada con SHA256SUMS y configuración mediante `sn-proactive-agent setup`.
- **Datos**: Almacenamiento por defecto en `~/.sn-proactive-agent/` (proyectos, items, eventos).
- **Comandos críticos**: `gh release download` para obtener el wheel verificado; `sn-proactive-agent serve --web-only` para iniciar la interfaz.
- **Flujo de validación**: Ejecución real de una conversación en Hermes (`hermes --tui`) para confirmar que las sugerencias se ejecutan y registran su ID fuente correctamente.

## Etiquetas
#SenseNova #ProactiveAgent #HermesIntegration #PythonAutomation

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\docs\sn-proactive-agent.md`
