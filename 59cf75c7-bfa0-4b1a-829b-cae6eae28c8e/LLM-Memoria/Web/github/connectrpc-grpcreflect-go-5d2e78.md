---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/connectrpc/grpcreflect-go"
tema: "gRPC Protobuf Reflection"
tags: [web]
---
# connectrpc/grpcreflect-go

## Resumen
Este módulo añade soporte para la API de reflexión de servidores gRPC a aplicaciones construidas con el framework Connect. Permite que herramientas de depuración ad-hoc inspeccionen respuestas sin necesidad de tener una copia del esquema local, manteniendo compatibilidad con implementaciones estándar de Google.

## Datos clave
- **Funcionalidad principal**: Habilita la API de reflexión de gRPC para servidores `net/http` usando Connect.
- **Compatibilidad**: Funciona con herramientas como `grpcurl`, `grpcui` y versiones recientes del protocolo (v1 y v1alpha).
- **Requisitos técnicos**: La API de reflexión requiere streaming bidireccional, por lo que solo se sirve sobre HTTP/2.
- **Instalación**: Se usa importando `connectrpc.com/grpcreflect/v2` y llamando a `grpcreflect.Register(server)`.
- **Estabilidad**: El módulo v2 es estable y sigue semantic versioning sin cambios rompedores en la serie 2.x.

## Etiquetas
#gRPC #Go #ReflectAPI #ConnectRPC #DevTools

Fuente: https://github.com/connectrpc/grpcreflect-go
