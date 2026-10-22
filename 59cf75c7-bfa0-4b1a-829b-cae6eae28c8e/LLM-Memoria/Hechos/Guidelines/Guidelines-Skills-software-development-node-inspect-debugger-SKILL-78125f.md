---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/software-development/node-inspect-debugger/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía explica cómo depurar aplicaciones de Node.js utilizando el inspector nativo V8 (`--inspect`) y la interfaz remota del protocolo Chrome (CDP) para obtener control granular sobre el flujo de ejecución. Sirve como referencia técnica para configurar puntos de interrupción, inspeccionar variables en tiempo real y automatizar diagnósticos complejos sin depender de `console.log`.

## Datos clave
- **Herramientas principales**: `node inspect` (CLI rápida) y `chrome-remote-interface` (automatización/scripting).
- **Comandos esenciales**: `sb()` para establecer puntos de interrupción, `bt` para trazas de llamada, `watch()` para monitoreo continuo.
- **Flujo de trabajo Hermes/ui-tui**: Usar `tsx` directamente con `--inspect-brk` en lugar del script `npm run dev` para depurar componentes Ink/React.
- **Instalación segura**: Instalar `chrome-remote-interface` en directorios temporales (`/tmp`) para evitar ensuciar el árbol de dependencias del proyecto principal.
- **Ataque a procesos activos**: Enviar `SIGUSR1` al PID para habilitar el inspector y luego unirse con `node inspect -p <pid>`.

## Etiquetas
#debugging #nodejs #cdp #hermes

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\software-development\node-inspect-debugger\SKILL.md`
