---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/autonomous-ai-agents/claude-code/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía detalla cómo delegar tareas de codificación autónomas al CLI de Claude Code a través del terminal Hermes. Explica dos modos de orquestación: el modo "Print" para automatización sin interacción y el modo interactivo vía tmux para sesiones iterativas complejas, incluyendo la gestión crítica de diálogos de confirmación.

## Datos clave
- **Instalación:** `npm install -g @anthropic-ai/claude-code`
- **Autenticación:** `claude auth login --console` (API key) o `--sso` (Enterprise).
- **Modo Print (Recomendado):** `claude -p "tarea" --allowedTools 'Read,Edit' --max-turns 10`. Ideal para CI/CD y tareas de un solo paso.
- **Modo Interactivo:** Requiere iniciar una sesión en tmux (`tmux new-session`) y enviar comandos con `send-keys`.
- **Gestión de Diálogos (Crítico):** En modo interactivo, se debe presionar `Enter` para aceptar la confianza del directorio y usar `Down` seguido de `Enter` para aceptar el aviso de permisos si se usa `--dangerously-skip-permissions`.
- **Comandos útiles:** `claude doctor` (salud), `claude update`, `claude mcp add <name> -- <cmd>` (servidores MCP).

## Etiquetas
#ClaudeCode #Automatización #DevOps #CLI #HermesAgent

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\autonomous-ai-agents\claude-code\SKILL.md`
