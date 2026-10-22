---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/PhantomHunt/cdc_postgres_logical_replication"
tema: "PostgreSQL Logical Decoding Replication"
tags: [web]
---
# PhantomHunt/cdc_postgres_logical_replication

## Resumen
Este repositorio presenta una implementación de Captura de Cambios (CDC) en bases de datos PostgreSQL utilizando los plugins de salida `pgoutput` y `test_decoding`. El sistema extrae datos del WAL (Write-Ahead Log), los decodifica y transforma las operaciones de inserción, actualización, borrado o truncamiento en un formato JSON estructurado para facilitar su uso.

## Datos clave
- **Plugins utilizados**: `pgoutput` y `test_decoding`.
- **Formato de salida**: JSON que incluye nombres de columnas y valores (clave-valor).
- **Operaciones soportadas**: Insert ('I'), Update ('U'), Delete ('D'), Truncate ('T').
- **Estructura del flujo**: Base de datos -> WAL -> Decodificación -> Formateo a JSON.
- **Nota sobre nombres de columnas**: Solo aparecen en mensajes de relación ('R') al inicio o tras alteraciones, por lo que se requiere un formador para unirlos con los mensajes de operación.

## Etiquetas
#PostgreSQL #CDC #WAL #pgoutput #Python

Fuente: https://github.com/PhantomHunt/cdc_postgres_logical_replication
