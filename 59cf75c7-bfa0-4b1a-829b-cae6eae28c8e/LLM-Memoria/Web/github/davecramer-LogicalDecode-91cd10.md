---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/davecramer/LogicalDecode"
tema: "PostgreSQL Logical Decoding"
tags: [web]
---
# davecramer/LogicalDecode

## Resumen
Este texto presenta una demostración de PostgreSQL Logical Decoding utilizando JDBC, explicando cómo acceder a cambios en la base de datos sin conexión directa. Se detallan los conceptos de "slots" para gestionar flujos de cambios y "plugins" para decodificar esos datos en formatos personalizados, además de mostrar ejemplos de código Java para crear y eliminar estos slots mediante consultas SQL.

## Datos clave
- **Logical Decoding**: Mecanismo que permite acceder a cambios en el heap sin conectarse a la base de datos, superando las limitaciones del formato binario inestable de los WAL (Write Ahead Logs).
- **Slot**: Flujo de cambios para una sola base de datos; gestiona transiciones y acknowledges. Se crea usando `pg_create_logical_replication_slot`.
- **Plugin**: Biblioteca que decodifica los cambios del slot en un formato definido por el usuario.
- **Comandos SQL clave**: `SELECT * FROM pg_create_logical_replication_slot`, `pg_terminate_backend`, `pg_drop_replication_slot`.
- **Clase Java**: `org.postgresql.replication.LogSequenceNumber` para manejar la posición LSN (Log Sequence Number) en el XLOG.

## Etiquetas
#PostgreSQL #LogicalDecoding #JDBC #Replicación

Fuente: https://github.com/davecramer/LogicalDecode
