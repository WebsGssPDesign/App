---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/JSON-RPC"
tema: "gRPC Protocols"
tags: [web]
---
# JSON-RPC

## Resumen
JSON-RPC es un protocolo de red basado en JSON diseñado para realizar llamadas remotas a procedimientos (RPC). A diferencia de otros protocolos, permite notificaciones sin respuesta y opera independientemente del transporte subyacente. Define estructuras claras para solicitudes, respuestas y errores, aunque no incluye mecanismos nativos de autenticación.

## Datos clave
- **Componentes de solicitud**: `method` (nombre), `params` (parámetros opcionales), `id` (identificador opcional).
- **Componentes de respuesta**: `result` (datos devueltos) o `error` (código y mensaje si falla).
- **Notificaciones**: Solicitudes sin `id` que no requieren respuesta del servidor.
- **Transporte independiente**: Funciona sobre HTTP, TCP o descriptor de archivo.
- **Errores predefinidos**: Códigos como "Parse error", "Method not found" o "Internal error".
- **Versiones principales**: 1.0, 1.1 (borrador) y 2.0 (estándar).

## Etiquetas
#JSON-RPC #ProtocolosRed #RPC #DesarrolloWeb #API

Fuente: https://en.wikipedia.org/wiki/JSON-RPC
