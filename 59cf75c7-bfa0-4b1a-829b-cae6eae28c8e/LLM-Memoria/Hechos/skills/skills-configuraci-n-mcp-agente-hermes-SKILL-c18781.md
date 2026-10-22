---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "skills/configuraci-n-mcp-agente-hermes/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe el procedimiento para configurar al agente Hermes con servidores MCP nativos y webhooks externos, permitiendo la automatización de flujos de trabajo mediante eventos de terceros como GitHub o Stripe. Su objetivo es integrar herramientas locales o remotas directamente en el agente sin necesidad de puentes CLI, facilitando la ejecución automática de tareas basadas en triggers específicos.

## Datos clave
- **Proyecto**: Configuración del agente Hermes para integración con herramientas externas vía Webhooks y MCP.
- **Tecnologías**: Servidores MCP (Model Context Protocol), Webhooks, GitHub, Stripe, IoT.
- **Decisiones**: Se requiere que la clave `mcp_servers` en `~/.hermes/config.yaml` no esté vacía antes de añadir nuevos servidores.
- **Comandos importantes**:
  - `hermes mcp add <NOMBRE> --url <URL>` o `--command <COMANDO_LOCAL>` para registrar servidores.
  - `hermes mcp test <NOMBRE>` y `hermes mcp list` para verificar la conectividad y descubrimiento de herramientas.
- **Pasos críticos**: Definir reglas de filtrado (headers, payloads) específicas del proveedor externo antes de activar los webhooks.

## Etiquetas
#HermesAgent #MCP #Webhooks #Automatización #IntegraciónAPI

Fuente: `F:\automatizaciones\homeLab\skills\configuraci-n-mcp-agente-hermes\SKILL.md`
