---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://es.wikipedia.org/wiki/Protocolo_Agent2Agent"
tema: "gRPC Protocols"
tags: [web]
---
# Protocolo Agent2Agent

## Resumen
El Protocolo Agent2Agent (A2A) es un estándar abierto diseñado por Google y adoptado por la Linux Foundation para permitir la interoperabilidad entre agentes de inteligencia artificial de diferentes proveedores. Su objetivo principal es facilitar el descubrimiento, la comunicación segura y la coordinación de tareas sin exponer los datos privados o internos de los agentes involucrados.

## Datos clave
- **Anuncio inicial:** 9 de abril de 2025 por Google con más de 50 socios tecnológicos.
- **Gobernanza:** Proyecto alojado en la Linux Foundation desde junio de 2025 con apoyo de más de 100 compañías.
- **Versiones:** v1.0.0 publicada el 12 de marzo de 2026 y v1.0.1 el 26 de mayo de 2026.
- **Componente central:** "Agent Card" (tarjeta de agente en JSON) que describe identidad, capacidades y seguridad; accesible vía `/.well-known/agent-card.json`.
- **Modelo de datos:** Se basa en objetos como tareas, mensajes, partes y artefactos.
- **Transportes:** Soporta JSON-RPC, gRPC y HTTP+JSON/REST.
- **Seguridad:** Implementa OAuth, OpenID Connect, TLS mutuo, firmas JWS y cabeceras de versión (`A2A-Version`).
- **Relación con MCP:** Complementario; MCP conecta agentes con herramientas/recursos externos, mientras que A2A coordina la comunicación entre agentes independientes.

## Etiquetas
#InteligenciaArtificial #AgentesIA #ProtocolosAbiertos #Interoperabilidad #LinuxFoundation #GoogleCloud

Fuente: https://es.wikipedia.org/wiki/Protocolo_Agent2Agent
