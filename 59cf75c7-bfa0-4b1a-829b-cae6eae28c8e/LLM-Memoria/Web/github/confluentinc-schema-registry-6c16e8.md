---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/confluentinc/schema-registry"
tema: "Kafka Schema Registry"
tags: [web]
---
# confluentinc/schema-registry

## Resumen
El Confluent Schema Registry actúa como una capa de servicio para metadatos en Apache Kafka, permitiendo almacenar y recuperar versiones de esquemas Avro, JSON y Protobuf mediante una interfaz RESTful. Este sistema gestiona la evolución de los datos asegurando la compatibilidad entre diferentes versiones de esquemas registrados bajo nombres de sujetos específicos. Además, proporciona serializadores que integran directamente con clientes de Kafka para manejar el formato de mensajes automáticamente.

## Datos clave
- **Formatos soportados**: Avro®, JSON Schema y Protobuf.
- **Comandos principales**: `curl` para registrar (`POST /subjects/<name>/versions`), listar (`GET /subjects`), obtener versión específica (`GET /subjects/<name>/versions/<id>`) y verificar compatibilidad (`POST /compatibility`).
- **Configuración de compatibilidad**: Niveles globales o por sujeto (ej. `BACKWARD`, `NONE`) para controlar la evolución de esquemas.
- **Ejemplo de registro**: `curl -X POST ... --data '{"schema": "{\"type\": \"string\"}"}' http://localhost:8081/subjects/Kafka-key/versions`.

## Etiquetas
#ApacheKafka #SchemaRegistry #Avro #JSONSchema #Protobuf #DataIntegration

Fuente: https://github.com/confluentinc/schema-registry
