---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/autonomous-ai-agents/codex/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento detalla cómo delegar tareas de desarrollo a OpenAI Codex mediante su CLI integrada en el terminal de Hermes. Sirve como guía operativa para ejecutar comandos, gestionar sesiones largas y realizar revisiones de PRs de forma autónoma o paralela, asegurando la seguridad con sandboxing y entornos Git temporales.

## Datos clave
- **Prerrequisitos**: Instalación global (`npm install -g @openai/codex`) y autenticación vía `OPENAI_API_KEY` o OAuth en `~/.codex/auth.json`.
- **Comandos esenciales**: Uso de `pty=true` para interactividad, `exec "prompt"` para tareas únicas y `--full-auto` para aprobaciones automáticas dentro del sandbox.
- **Modo fondo**: Iniciar con `background=true`, monitorear con `process(action="poll")` y enviar respuestas con `action="submit"`.
- **Seguridad en gateways**: Si falla el sandboxing (errores de `bubblewrap`), usar `--sandbox danger-full-access` y validar cambios manualmente.
- **Flujos avanzados**: Creación de worktrees (`git worktree add`) para arreglar múltiples issues en paralelo y revisión segura de PRs en directorios temporales.

## Etiquetas
#OpenAI #CodexCLI #AutomatizaciónDev #GitWorkflows #HermesAgent

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\autonomous-ai-agents\codex\SKILL.md`
