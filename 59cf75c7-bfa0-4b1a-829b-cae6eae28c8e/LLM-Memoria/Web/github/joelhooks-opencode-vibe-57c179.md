---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/joelhooks/opencode-vibe"
tema: "React Server Components Streaming"
tags: [web]
---
# joelhooks/opencode-vibe

## Resumen
Este proyecto es una aplicación web moderna construida con Next.js 16 y Bun que sirve como interfaz de chat en tiempo real para la herramienta OpenCode. Utiliza componentes del lado del servidor, arquitectura reactiva de flujos mundiales y sincronización vía eventos enviados por el servidor (SSE) para conectar la UI con múltiples procesos de OpenCode ejecutándose localmente.

## Datos clave
- **Tecnologías principales**: Next.js 16 (canary), Bun v1.3+, TypeScript 5+, Tailwind CSS, Turbopack.
- **Características destacadas**: Descubrimiento automático de procesos OpenCode vía `lsof`, chat en tiempo real con streaming, comandos por barra (`/fix`, `/refactor`) y búsqueda de archivos (`@`).
- **Comandos esenciales**: `bun install`, `opencode` (para iniciar el CLI), `bun dev` (puerto 8423).
- **Estructura**: Monorepo con apps web, CLI de swarm, paquetes core/react y documentación ADR.
- **Tema**: Catppuccin (Latte/Mocha) con resaltado de sintaxis.

## Etiquetas
#NextJS16 #Bun #OpenCode #ReactServerComponents #RealTimeChat

Fuente: https://github.com/joelhooks/opencode-vibe
