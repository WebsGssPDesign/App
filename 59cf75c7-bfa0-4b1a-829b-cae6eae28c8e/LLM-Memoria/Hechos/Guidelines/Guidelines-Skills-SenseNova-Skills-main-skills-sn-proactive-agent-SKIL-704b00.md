---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-proactive-agent/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define las directrices para instalar, configurar y operar el agente Proactive Agent de SenseNova. Su función principal es monitorear conversaciones multi-turno, identificar tareas pendientes y sugerir acciones en la interfaz web, ejecutándose como un servicio independiente que no modifica archivos del proyecto directamente.

## Datos clave
- **Proyecto**: sn-proactive-agent (versión 0.1.3).
- **Tecnologías**: Python (`pipx`), Hermes Connector, Web-only mode.
- **Rutas de instalación**: `install/overview.md`, `install/macos.md`, `install/windows.md`.
- **Comandos y flags**: `serve --web-only`, `doctor --session-id`, `--data-root`.
- **Estructura de datos**: Directorio `.sn-proactive-agent/` con archivos `project.md`, `item.md`, `events.md` y `runtime.jsonl`.
- **Restricciones críticas**: No editar archivos del proyecto manualmente, no leer credenciales (API Keys), evitar ejecución duplicada de acciones.

## Etiquetas
#SenseNova #ProactiveAgent #Automatización #Python #Documentación

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-proactive-agent\SKILL.md`
