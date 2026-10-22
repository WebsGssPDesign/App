---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Presto_%28SQL_query_engine%29"
tema: "PostgreSQL Query Planning"
tags: [web]
---
# Presto (SQL query engine)

## Resumen
Presto es un motor de consultas distribuido y de código abierto que permite ejecutar análisis SQL rápidos sobre grandes volúmenes de datos almacenados en diversas fuentes. A diferencia de sistemas basados en MapReduce, Presto procesa los datos directamente en memoria sin escribir resultados intermedios en disco, lo que mejora significativamente la velocidad. El proyecto ha experimentado una evolución compleja con múltiples bifurcaciones y cambios de marca, resultando hoy principalmente en Trino (mantenido por la fundación) y PrestoDB.

## Datos clave
- **Funcionamiento**: Arquitectura cliente-servidor donde un coordinador asigna tareas a trabajadores que procesan datos en memoria sin usar disco intermedio.
- **Compatibilidad**: Conectores para Hadoop, AWS S3, Kafka, Cassandra, MySQL, MongoDB y muchos otros; funciona con cualquier variante de Hadoop o sin él.
- **Historia y nombres**: Desarrollado inicialmente por Facebook (Meta) en 2012. En 2019 se fundó la Presto Software Foundation. En 2020, PrestoSQL se renombró a Trino debido a una marca registrada de Facebook, mientras que el fork original mantenido por Meta se llama PrestoDB.
- **Lenguaje**: Escrito en Java.

## Etiquetas
#Presto #Trino #BigData #SQL #OpenSource

Fuente: https://en.wikipedia.org/wiki/Presto_%28SQL_query_engine%29
