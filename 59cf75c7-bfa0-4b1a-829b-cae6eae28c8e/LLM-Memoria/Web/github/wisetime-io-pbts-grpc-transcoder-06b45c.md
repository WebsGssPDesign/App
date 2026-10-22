---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/wisetime-io/pbts-grpc-transcoder"
tema: "gRPC Protobuf JSON Transcoding"
tags: [web]
---
# wisetime-io/pbts-grpc-transcoder

## Resumen
pbts-grpc-transcoder es una librería en TypeScript que permite transcodificar llamadas gRPC (HTTP/2 binario) a HTTP/1 y JSON, facilitando la interoperabilidad con clientes REST. El proyecto mantiene el fuerte tipado de Protocol Buffers al ejecutar solicitudes asíncronas contra un servidor gRPC mediante un proxy transparente.

## Datos clave
- **Instalación:** `npm i pbts-grpc-transcoder`
- **Herramientas de generación:** `pbjs` y `pbts` (disponibles en `node_modules/.bin`).
- **Pasos de configuración:** Generar descriptor JSON con `-t json`, librería JS estática con `-t static-module` y tipos TypeScript.
- **Funcionalidad principal:** Ejecutor HTTP para `protobuf.js` que soporta políticas automáticas de reintentos (`RetryPolicy`) basadas en códigos de estado (ej. 401).
- **Flujo:** El cliente llama a la API como si fuera gRPC; el transcodificador convierte la petición a JSON/HTTP/1 y envía al proxy, que la traduce nuevamente a gRPC para el servidor backend.

## Etiquetas
#TypeScript #gRPC #Protobuf #Transcoding #RESTAPI

Fuente: https://github.com/wisetime-io/pbts-grpc-transcoder
