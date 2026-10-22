---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/jhump/protoreflect"
tema: "gRPC Protobuf Reflection"
tags: [web]
---
# jhump/protoreflect

## Resumen
Este repositorio extiende las capacidades de reflexión del runtime de Protocol Buffers para Go, ofreciendo herramientas avanzadas para gestionar descripciones y tipos. Incluye utilidades para construir descripciones dinámicamente, resolver esquemas y recuperar información de código fuente perdida durante la generación. Además, facilita el trabajo con clientes RPC dinámicos mediante stubs genéricos.

## Datos clave
- **Paquetes principales**: `protoprint` (generación inversa a `.proto`), `protobuilder` (construcción programática de descripciones), `protoresolve` (unificación de interfaces de resolutores).
- **Información de código fuente**: El paquete `sourceinfo` permite recuperar datos como nombre de archivo, línea y comentarios originales mediante el plugin `protoc-gen-gosrcinfo`.
- **Dinamismo**: Uso del paquete `dynamicpb` para manejar mensajes sin generar structs específicos.
- **Versiones**: Disponible la versión v2 beta con cambios significativos respecto a la v1.

## Etiquetas
#ProtocolBuffers #Go #gRPC #Reflección #Descriptores

Fuente: https://github.com/jhump/protoreflect
