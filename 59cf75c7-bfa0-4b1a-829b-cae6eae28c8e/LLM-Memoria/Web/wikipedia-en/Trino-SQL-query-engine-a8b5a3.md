---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Trino_%28SQL_query_engine%29"
tema: "PostgreSQL Federated Queries"
tags: [web]
---
# Trino (SQL query engine)

## Resumen
Trino es un motor de consultas SQL distribuido y de código abierto diseñado para analizar grandes conjuntos de datos almacenados en fuentes heterogéneas. Su arquitectura separa el cómputo del almacenamiento, permitiendo ejecutar consultas federadas sobre múltiples sistemas como data lakes, bases de datos relacionales y NoSQL sin mover los datos.

## Datos clave
- **Origen**: Fork del proyecto Presto creado en 2019; renombrado a Trino en diciembre de 2020.
- **Licencia**: Apache License.
- **Arquitectura**: Escrita en Java con nodos coordinadores (planificación) y trabajadores (ejecución).
- **Compatibilidad**: Soporta estándares ANSI SQL desde 1992 hasta 2023.
- **Almacenamiento**: Consulta formatos como CSV, JSON, ORC y Parquet en HDFS, AWS S3, GCS o Azure Blob Storage.
- **Fuentes federadas**: MySQL, PostgreSQL, Cassandra, Kafka, MongoDB, Elasticsearch.
- **Despliegue**: Soporta entornos on-premises y nube (ejemplos: Amazon Athena, Starburst Galaxy).

## Etiquetas
#Trino #BigData #SQL #OpenSource #DistributedComputing

Fuente: https://en.wikipedia.org/wiki/Trino_%28SQL_query_engine%29
