---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/grpc-ecosystem/go-grpc-middleware"
tema: "gRPC Interceptors"
tags: [web]
---
# grpc-ecosystem/go-grpc-middleware

## Resumen
Este repositorio proporciona middleware para gRPC en Go, facilitando la implementación de patrones comunes como autenticación, logging y recuperación ante pánicos. Permite encadenar múltiples interceptores tanto en el servidor como en el cliente para crear microservicios robustos y observables. Ofrece herramientas listas para usar y ejemplos que integran métricas, trazabilidad y seguridad.

## Datos clave
- **Interceptores**: Funciones ejecutadas antes o alrededor de las llamadas gRPC (unary/stream).
- **Autenticación**: Middleware configurable vía `AuthFunc` y políticas RBAC externas.
- **Observabilidad**: Soporte para Prometheus, OpenTelemetry y logging con adaptadores externos (logrus, zap, etc.).
- **Encadenamiento**: Uso de `grpc.ChainUnaryInterceptor` y `grpc.ChainStreamInterceptor`.
- **Recuperación**: Interceptores para manejar pánicos (`recovery.UnaryServerInterceptor`).
- **Licencia**: Apache 2.0.

## Etiquetas
#go #gRPC #middleware #microservicios #observabilidad

Fuente: https://github.com/grpc-ecosystem/go-grpc-middleware
