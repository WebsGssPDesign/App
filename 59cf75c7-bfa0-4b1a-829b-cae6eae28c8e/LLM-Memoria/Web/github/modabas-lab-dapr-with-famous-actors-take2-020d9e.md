---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/modabas/lab-dapr-with-famous-actors-take2"
tema: "Dapr PubSub Patterns"
tags: [web]
---
# modabas/lab-dapr-with-famous-actors-take2

## Resumen
Este proyecto demuestra cómo integrar servicios de Microsoft Orleans con Dapr para crear una arquitectura distribuida escalable. Utiliza el patrón Outbox y la replicación lógica de PostgreSQL junto con RabbitMQ (vía Dapr pub/sub) para garantizar la consistencia de los eventos entre bases de datos y sistemas de mensajería.

## Datos clave
- **Tecnologías**: Microsoft Orleans, Dapr, .NET, PostgreSQL, RabbitMQ, OpenTelemetry, Elasticsearch.
- **Patrón Outbox**: Los eventos se escriben en una tabla `outbox` dentro de la misma transacción que los datos principales para asegurar integridad.
- **Replicación Lógica**: PostgreSQL Logical Replication notifica un listener cuando hay cambios en el outbox, publicándolos a Dapr.
- **Comandos de despliegue**:
  - Iniciar PostgreSQL: `docker run ... postgres:15.1 -c 'wal_level=logical'`
  - Iniciar RabbitMQ: `docker run ... rabbitmq:3-management`
- **Observabilidad**: Uso de OpenTelemetry para trazas y logs exportados a Elasticsearch vía un collector.
- **Herramienta de debug**: Dapr Sidekick for .Net facilita la configuración y depuración.

## Etiquetas
#MicrosoftOrleans #Dapr #PostgreSQL #RabbitMQ #OutboxPattern #EventSourcing #OpenTelemetry

Fuente: https://github.com/modabas/lab-dapr-with-famous-actors-take2
