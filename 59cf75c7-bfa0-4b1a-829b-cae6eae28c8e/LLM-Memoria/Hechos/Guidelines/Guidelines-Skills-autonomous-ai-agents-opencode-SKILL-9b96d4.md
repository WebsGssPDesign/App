---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/autonomous-ai-agents/opencode/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define la habilidad de delegar tareas de programación al agente autónomo OpenCode, orquestado a través de herramientas del terminal Hermes. Sirve como guía operativa para ejecutar sesiones interactivas o tareas puntuales, gestionar revisiones de PR y optimizar costos mediante el control de sesiones.

## Datos clave
- **Proyecto**: OpenCode CLI (versión 1.2.0).
- **Tecnologías**: Node.js (`npm`), Homebrew, interfaces TUI/CLI, modelos de IA (ej. Claude Sonnet 4).
- **Decisiones críticas**: Evitar el comando `/exit` para cerrar sesiones; usar `Ctrl+C` o `process(action="kill")`.
- **Comandos principales**:
  - Instalación: `npm i -g opencode-ai@latest`.
  - Tareas puntuales: `opencode run 'prompt'`.
  - Sesiones interactivas: `opencode ... background=true, pty=true`.
  - Revisión de PR: `opencode pr <número>`.
- **Gestión**: Uso de directorios de trabajo aislados (`workdir`) para tareas paralelas y verificación de binarios con `which -a opencode`.

## Etiquetas
#OpenCode #AgentesAutónomos #DevOps #CLI #Hermes

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\autonomous-ai-agents\opencode\SKILL.md`
