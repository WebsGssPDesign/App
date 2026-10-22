---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/Telefonica/prometheus-kafka-adapter"
tema: "Prometheus Remote Write"
tags: [web]
---
# Telefonica/prometheus-kafka-adapter

## Resumen
El proyecto `prometheus-kafka-adapter` de Telefónica es un servicio diseñado para actuar como almacenamiento remoto de métricas, recibiendo datos desde Prometheus mediante el protocolo `remote_write` y transformándolos en mensajes JSON o Avro para enviarlos a un tema de Kafka. La herramienta facilita la integración entre ambos sistemas permitiendo una configuración flexible sobre serialización, filtrado de métricas y autenticación segura.

## Datos clave
- **Función principal**: Recibe métricas Prometheus vía `remote_write` y las escribe en Kafka.
- **Formatos de salida**: JSON o Avro-JSON (configurable con `SERIALIZATION_FORMAT`).
- **Variables críticas de configuración**:
  - `KAFKA_TOPIC`: Define el tema destino (soporta plantillas Go para temas dinámicos).
  - `MATCH`: Filtra métricas y etiquetas específicas antes del envío.
  - `KAFKA_BROKER_LIST`, `KAFKA_COMPRESSION`, `PORT`.
- **Seguridad**: Soporte para autenticación básica, SSL/TLS y SASL/SCRAM mediante variables de entorno.
- **Despliegue**: Imagen Docker disponible (`telefonica/prometheus-kafka-adapter`) y despliegue en Kubernetes vía Helm.

## Etiquetas
#monitorización #prometheus #kafka #ingesta-de-métricas #telefonica

Fuente: https://github.com/Telefonica/prometheus-kafka-adapter
