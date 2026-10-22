---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/cloudwego/kitex"
tema: "gRPC Protobuf Streaming"
tags: [web]
---
# cloudwego/kitex

## Resumen
Kitex es un framework de RPC para Go diseñado para construir microservicios priorizando el alto rendimiento y la extensibilidad. Integra la biblioteca de red Netpoll para superar las limitaciones del estándar `go net` y soporta múltiples protocolos como Thrift, Protobuf personalizado y gRPC. El sistema incluye módulos nativos de gobernanza de servicios, generación de código y una arquitectura modular que permite inyección de middleware.

## Datos clave
- **Rendimiento**: Basado en Netpoll para mayor eficiencia que `go net`.
- **Protocolos soportados**: Thrift, Kitex Protobuf (formato similar a Thrift), gRPC.
- **Tipos de mensajes**: PingPong, One-way, Bidirectional Streaming.
- **Transportes**: TTHeader y HTTP2.
- **Gobernanza**: Registro de servicios, descubrimiento, balanceo de carga, circuit breaker, rate limiting, trazabilidad y logging.
- **Herramientas**: Generador de código para Thrift, Protobuf y andamiaje.
- **Extensibilidad**: Soporte para middleware, suites personalizadas e inyección en módulos como Codec y Transport.

## Etiquetas
#Go #RPC #Microservicios #DevOps #Netpoll

Fuente: https://github.com/cloudwego/kitex
