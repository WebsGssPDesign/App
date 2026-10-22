---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/adamw7/tools"
tema: "gRPC Protobuf Code Generation Tools"
tags: [web]
---
# adamw7/tools

## Resumen
Este repositorio ofrece una colección de herramientas para la ingeniería de contexto y generación de código seguro en tiempo de compilación. Incluye un plugin de Maven diseñado como "enforcer" que valida estrictamente la estructura y el contenido de los archivos necesarios para Claude Code, asegurando su consistencia antes de permitir la construcción del proyecto.

## Datos clave
- **Módulo `claude-code-enforcer`**: Conjunto de reglas personalizadas del plugin `maven-enforcer-plugin`.
- **Archivos críticos validados**: `CLAUDE.md`, `AGENTS.md`, `.claude/settings.json`, subagentes y habilidades (skills).
- **Reglas específicas**:
  - `claudeMdFormat` y `agentsMdFormat`: Verifican títulos, secciones obligatorias y referencias cruzadas.
  - `contextBudget`: Limita archivos por bytes, líneas o tokens para gestionar el presupuesto de contexto.
  - `memoryImports`: Asegura que las importaciones de rutas (`@path`) sean válidas en disco sin ciclos.
  - `settingsJsonValid` y `permissionsFormat`: Valida la sintaxis JSON y políticas de permisos de herramientas (ej. prohibir `Bash(*)`).
- **Generación de código**: Herramientas para generar código Java seguro de Protocol Buffers en tiempo de compilación.

## Etiquetas
#ingeniería_de_contexto #maven_enforcer #claude_code #calidad_del_código #protobuf

Fuente: https://github.com/adamw7/tools
