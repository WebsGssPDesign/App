---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/go-kratos/kratos"
tema: "gRPC Protobuf"
tags: [web]
---
# go-kratos/kratos

## Resumen
Kratos es un framework ligero en Go diseñado para construir microservicios nativos de la nube, priorizando el desarrollo orientado a APIs mediante Protobuf. Ofrece componentes modulares y explícitos para transporte, middleware, registro y configuración, permitiendo que los desarrolladores se enfoquen en la lógica de negocio.

## Datos clave
- **Requisitos:** Go 1.25 o posterior, `protoc` y `protoc-gen-go`.
- **Instalación del CLI:** `go install github.com/go-kratos/kratos/cmd/kratos/v3@latest`.
- **Comandos principales:** `kratos new <nombre>`, `kratos proto add <ruta>.proto`, `kratos run`.
- **Versiones:** La versión v3 reduce dependencias y hace explícitas las conductas implícitas de versiones anteriores.
- **Integraciones:** Soporte unificado para HTTP y gRPC con middleware como logging, validación y autenticación.

## Etiquetas
#Go #Microservicios #CloudNative #Protobuf

Fuente: https://github.com/go-kratos/kratos
