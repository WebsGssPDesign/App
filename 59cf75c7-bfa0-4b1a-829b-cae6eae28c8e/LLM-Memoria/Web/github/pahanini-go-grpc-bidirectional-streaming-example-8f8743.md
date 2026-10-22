---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/pahanini/go-grpc-bidirectional-streaming-example"
tema: "gRPC Bidirectional Streaming"
tags: [web]
---
# pahanini/go-grpc-bidirectional-streaming-example

## Resumen
Este repositorio presenta un ejemplo de streaming bidireccional gRPC en Go, donde el cliente envía números aleatorios y el servidor responde únicamente con los nuevos máximos recibidos. La implementación maneja errores de contexto para cerrar conexiones durante la transmisión.

## Datos clave
- **Requisitos**: Go 1.17.1, protoc instalado, soporte de protobuf en Go.
- **Comandos de instalación (MacOS)**: `brew install go`, `brew install protobuf`, `go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.1`.
- **Configuración PATH**: Agregar `export PATH="$PATH:$(go env GOPATH)/bin"` a `~/.bash_profile` y ejecutar `source ~/.bash_profile`.
- **Comando de compilación**: `make all`, generando los binarios `server` y `client`.
- **Uso**: Ejecutar `./server` en un terminal y `./client` en otro. El servidor envía el nuevo máximo (ej: "new max 6") cada vez que recibe un número mayor a los anteriores.

## Etiquetas
#gRPC #Go #StreamingBidireccional #Protobuf

Fuente: https://github.com/pahanini/go-grpc-bidirectional-streaming-example
