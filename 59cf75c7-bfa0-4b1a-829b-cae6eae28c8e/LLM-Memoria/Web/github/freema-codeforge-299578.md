---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/freema/codeforge"
tema: "React Server Actions Streaming"
tags: [web]
---
# freema/codeforge

## Resumen
CodeForge es un orquestador de backend diseñado para ejecutar sesiones de trabajo impulsadas por IA sobre repositorios Git. Permite automatizar tareas como revisiones de código, creación de PRs y análisis de repositorios completos utilizando herramientas como Claude Code o Codex. El sistema opera en dos modos: como servidor con interfaz web o mediante acciones de CI/CD.

## Datos clave
- **Modos de operación**: Servidor (cola + workers + API) y Acción de GitHub/GitLab CI.
- **Tipos de sesiones**: Código, planificación, revisión completa del repositorio, revisión de PRs y sesiones de conocimiento.
- **Seguridad**: El CLI de IA corre en el mismo contenedor que el servidor pero con privilegios reducidos (usuario no root); las credenciales Git se gestionan mediante scripts efímeros.
- **Funcionalidades**: Flujo de trabajo en tiempo real, control humano antes de abrir PRs, plantillas reutilizables ("Blueprints") y seguimiento de costos.
- **Requisitos técnicos**: Go + React, despliegue vía Docker o GitHub Action, base de datos Redis para la cola.

## Etiquetas
#IA #DevOps #Automatización #Git #Seguridad

Fuente: https://github.com/freema/codeforge
