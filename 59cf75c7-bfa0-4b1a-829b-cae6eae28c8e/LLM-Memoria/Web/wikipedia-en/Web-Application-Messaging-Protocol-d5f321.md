---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Web_Application_Messaging_Protocol"
tema: "gRPC Bidirectional Streaming"
tags: [web]
---
# Web Application Messaging Protocol

## Resumen
WAMP es un subprotocolo WebSocket estandarizado que facilita el intercambio de mensajes en tiempo real mediante RPC y PubSub. Su diseño permite crear arquitecturas descentralizadas basadas en microservicios, actuando como un bus de servicios empresarial para aplicaciones web e IoT. El protocolo utiliza un router central para enrutar comunicaciones entre clientes iguales, ocultando la ubicación física de los procedimientos.

## Datos clave
- **Transporte:** WebSocket por defecto (requiere canal fiable, ordenado y full-duplex), aunque admite sockets crudos o HTTP long poll.
- **Serialización:** JSON es el formato estándar; MessagePack es una alternativa más rápida con dependencias adicionales.
- **Primitivas principales:** `register` (exponer procedimientos), `call` (invocar remotamente), `subscribe` (interesarse en un tema) y `publish`.
- **Seguridad:** Uso de TLS para cifrado, implementación de "realms" como dominios administrativos con permisos específicos y autenticación mediante certificados o tickets.
- **Arquitectura:** Los clientes son iguales (pueden ofrecer procedimientos), eliminando la distinción estricta entre cliente y servidor backend.
- **Implementaciones:** Requiere bibliotecas asíncronas/no bloqueantes; Crossbar.io es una implementación de router destacada.

## Etiquetas
#WAMP #WebSocket #Microservicios #IoT #RPC #PubSub

Fuente: https://en.wikipedia.org/wiki/Web_Application_Messaging_Protocol
