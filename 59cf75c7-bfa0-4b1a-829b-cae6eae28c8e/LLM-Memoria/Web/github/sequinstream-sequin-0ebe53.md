---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://github.com/sequinstream/sequin"
tema: "PostgreSQL Indexes"
tags: [web]
---
# sequinstream/sequin

## Resumen
Sequin es una plataforma de captura de cambios (CDC) para Postgres diseñada para ofrecer el mayor rendimiento del mercado, permitiendo sincronizar datos en tiempo real con sistemas como Kafka, Elasticsearch y colas. Funciona como un contenedor Docker independiente que se despliega junto a la base de datos para gestionar tanto el flujo continuo de nuevos eventos como la recuperación de datos históricos.

## Datos clave
- **Rendimiento:** Sustenta más de 50k operaciones por segundo con una latencia promedio de 55ms.
- **Funcionalidad principal:** Convierte cambios en Postgres a streams, colas y índices de búsqueda.
- **Capacidad de backfill:** Permite recuperar filas existentes además de transmitir cambios nuevos en tiempo real.
- **Despliegue:** Se instala como un contenedor Docker autónomo junto al motor de base de datos.
- **Destinos (Sinks):** Soporta Azure EventHubs, GCP Pub/Sub, Elasticsearch, Kafka, Kinesis, NATS, RabbitMQ, Redis Stream y HTTP endpoints.

## Etiquetas
#Postgres #CDC #Streaming #DevOps #DataEngineering

Fuente: https://github.com/sequinstream/sequin
