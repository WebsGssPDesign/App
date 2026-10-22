---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/autonomous-ai-agents/hermes-agent/references/native-mcp.md"
tags: [hecho]
---
# native-mcp.md

## Resumen
Este documento describe la implementación de un cliente nativo para el protocolo MCP dentro del agente Hermes, permitiendo conectar servidores externos (locales o remotos) y hacer sus herramientas disponibles automáticamente. Su función es integrar capacidades adicionales como acceso a archivos, GitHub o bases de datos sin necesidad de puentes CLI externos, registrando las herramientas con un prefijo específico en todas las plataformas del agente.

## Datos clave
- **Prerrequisitos**: Paquete `mcp` (pip/uv), Node.js para servidores stdio (`npx`) y uv para servidores Python (`uvx`).
- **Configuración**: Se define en `~/.hermes/config.yaml` bajo la clave `mcp_servers`.
- **Tipos de transporte**: 
  - **Stdio**: Usa comandos ejecutables con argumentos (ej. `npx`, `uvx`) y variables de entorno filtradas.
  - **HTTP/StreamableHTTP**: Conecta a URLs remotas, soportando encabezados personalizados como tokens de autenticación.
- **Nomenclatura**: Las herramientas se registran con el patrón `mcp_{servidor}_{herramienta}` (ej. `mcp_github_list_issues`).
- **Gestión de conexiones**: Los servidores corren en bucles de eventos de fondo con reintentos exponenciales ante fallos y cierre suave al detener el agente.

## Etiquetas
#MCP #HermesAgent #IntegraciónAPI #Automatización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\autonomous-ai-agents\hermes-agent\references\native-mcp.md`
