---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/Trendyol/go-pq-cdc"
tema: "PostgreSQL Change Data Capture"
tags: [web]
---
# Trendyol/go-pq-cdc

## Resumen
go-pq-cdc es un sistema ligero y eficiente de captura de datos en cambios (CDC) para bases de datos PostgreSQL, escrito completamente en Golang. Utiliza la replicación lógica nativa de PostgreSQL para sincronizar datos históricos mediante snapshots y transmitir cambios en tiempo real a sistemas downstream como Kafka o Elasticsearch.

## Datos clave
- **Tecnología**: Sistema CDC ligero en Golang que aprovecha `pg_export_snapshot()` para consistencia punto en el tiempo.
- **Funcionalidad principal**: Captura de datos existentes (snapshot) + streaming de cambios (INSERT, DELETE, UPDATE, TRUNCATE).
- **Procesamiento**: Manejo chunk-based para eficiencia de memoria y soporte para particionamiento automático.
- **Protocolos**: Soporte para versiones `pgoutput` 1 y 2.
- **Instalación**: `go get github.com/Trendyol/go-pq-cdc`.
- **Configuración clave**: Definición de `Publication`, `Slot`, operaciones permitidas (Insert, Delete, Update) y tabla específica (ej: "users").
- **Recuperación**: Soporte para recuperación automática tras fallos y manejo seguro de transacciones abortadas.

## Etiquetas
#PostgreSQL #CDC #Golang #DataSync #RealTime

Fuente: https://github.com/Trendyol/go-pq-cdc
