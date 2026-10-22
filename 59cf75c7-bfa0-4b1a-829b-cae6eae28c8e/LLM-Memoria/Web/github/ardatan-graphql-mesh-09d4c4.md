---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/ardatan/graphql-mesh"
tema: "GraphQL Federation"
tags: [web]
---
# ardatan/graphql-mesh

## Resumen
GraphQL Mesh es un framework de federación y gateway diseñado para permitir el acceso a datos mediante GraphQL desde servicios remotos que no lo utilizan nativamente, como REST, gRPC o bases de datos. Actúa como una capa intermedia que transforma automáticamente las especificaciones de estas APIs en esquemas GraphQL funcionales.

## Datos clave
- **Funcionalidad principal**: Convierte servicios heterogéneos (REST, OpenAPI, SOAP, gRPC, MongoDB, MySQL, PostgreSQL) en fuentes de datos accesibles vía GraphQL.
- **Mecanismo de trabajo**: Recopila especificaciones de esquemas API, crea instancias de SDK tipadas y convierte dichas especificaciones en un esquema GraphQL que puede actuar como subgrafo o supergrafo federado.
- **Capacidades adicionales**: Permite modificar el esquema de salida, vincular tipos entre diferentes esquemas, fusionar tipos y añadir resolutores personalizados para adaptar los datos a las necesidades específicas del desarrollador.

## Etiquetas
#GraphQL #Federation #APIGateway #Microservicios

Fuente: https://github.com/ardatan/graphql-mesh
