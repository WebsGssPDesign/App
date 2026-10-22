---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Materialized_view"
tema: "PostgreSQL Materialized Views"
tags: [web]
---
# Materialized view

## Resumen
Una vista materializada es un objeto de base de datos que almacena físicamente los resultados de una consulta, actuando como una forma de caché o precomputación. A diferencia de las vistas virtuales estándar, estas tablas concretas mejoran significativamente el rendimiento al evitar cálculos repetidos sobre datos subyacentes, aunque requieren espacio adicional y pueden quedar desactualizadas.

## Datos clave
- **Definición**: Objeto que contiene resultados de consultas (copias locales de datos remotos, subconjuntos o agregados).
- **Sinónimos**: Snapshots (terminología obsoleta en Oracle), Materialized Query Tables (IBM Db2).
- **Implementaciones específicas**:
    - **Oracle**: Implementado desde la versión 8i con función "Query rewrite".
    - **PostgreSQL**: Soporte nativo desde v9.3; requiere `REFRESH MATERIALIZED VIEW` manual o uso de `CONCURRENTLY`.
    - **SQL Server**: Se implementa mediante "Indexed Views", que se sincronizan automáticamente sin necesidad de refresco explícito si el mapeo es determinista.
- **Ventajas**: Acceso más eficiente, índices en cualquier columna (algo difícil en vistas normales).
- **Desventajas**: Consumo extra de almacenamiento y posible desactualización de datos.
- **Streaming**: Soportado por Apache Kafka, Spark, Flink, Materialize, RisingWave y otros frameworks modernos.

## Etiquetas
#bases_de_datos #optimizacion #caching #arquitectura

Fuente: https://en.wikipedia.org/wiki/Materialized_view
