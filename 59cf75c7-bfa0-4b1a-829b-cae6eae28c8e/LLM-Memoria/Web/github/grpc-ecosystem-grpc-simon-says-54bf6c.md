---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/grpc-ecosystem/grpc-simon-says"
tema: "gRPC Bidirectional Streaming"
tags: [web]
---
# grpc-ecosystem/grpc-simon-says

## Resumen
Este proyecto demuestra la implementación de una versión multijugador del juego "Simon Says" utilizando gRPC para comunicación bidireccional y Kubernetes. Está diseñado como un ejemplo educativo que ilustra cómo construir juegos interactivos conectando múltiples clientes en diferentes plataformas con un servidor centralizado.

## Datos clave
- **Tecnologías principales**: gRPC (streaming bidireccional), Kubernetes, Redis.
- **Implementación del servidor**: Escrito en Go y alojado en la carpeta `/server/go`.
- **Clientes multilenguaje**: Disponibles versiones para Android (Java), línea de comandos (Java), Arduino (Node.js) y navegador web (Node.js).
- **Flujo de juego**: Los jugadores se unen, reciben notificaciones de turno, envían pulsaciones de botones y reciben indicaciones visuales de colores.
- **Estado del proyecto**: Proyecto de ejemplo no oficial de Google, presentado en conferencias como Ubiquity Dev Summit (2016).

## Etiquetas
#grpc #kubernetes #multijugador #simon-says #iot #android

Fuente: https://github.com/grpc-ecosystem/grpc-simon-says
