---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/touchdesigner-mcp/references/external-data.md"
tags: [hecho]
---
# external-data.md

## Resumen
Este documento sirve como referencia técnica para conectar TouchDesigner con datos externos mediante protocolos de red y dispositivos físicos. Explica cómo implementar clientes HTTP, servidores web, conexiones WebSocket, MQTT e interfaces serie para automatización y control en tiempo real.

## Datos clave
- **Protocolos soportados**: HTTP (GET/POST), WebSockets, MQTT, Serial, TCP/IP, UDP.
- **Nodos principales**: `webDAT`, `webclientDAT` (recomendado), `webserverDAT`, `websocketDAT`, `mqttClientDAT`, `serialDAT`.
- **Patrones de uso**: Polling con `timerCHOP` y `chopExecuteDAT`; manejo de JSON en respuestas; autenticación vía cabeceras.
- **Seguridad**: Los servidores web no tienen autenticación por defecto; se recomienda vincularlos solo a localhost o implementar tokens.
- **Comandos clave**: `par.fetch.pulse()` para disparar solicitudes, `dat.sendText()` para enviar mensajes WebSocket/Serial.

## Etiquetas
#TouchDesigner #APIExterna #IoT #Redes #Automatización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\touchdesigner-mcp\references\external-data.md`
