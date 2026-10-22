---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://github.com/shayonj/pg_easy_replicate"
tema: "PostgreSQL Logical Replication"
tags: [web]
---
# shayonj/pg_easy_replicate

## Resumen
pg_easy_replicate es una herramienta de línea de comandos diseñada para simplificar la configuración de replicación lógica entre dos servidores PostgreSQL y facilitar el cambio (switchover) con un tiempo de inactividad mínimo. El software asegura que no haya pérdida de datos al poner la base de datos fuente en modo solo lectura y sincronizar todo hacia la nueva antes del corte final, siendo útil para actualizaciones mayores o pruebas de carga.

## Datos clave
- **Requisitos**: PostgreSQL 10+, Ruby 3.0+ o contenedor Docker.
- **Variables de entorno**: `SOURCE_DB_URL` (origen) y `TARGET_DB_URL` (destino).
- **Comandos principales**: `bootstrap`, `start_sync`, `stop_sync`, `cleanup`, `config_check`.
- **Limitaciones**: Aplica las restricciones estándar de replicación lógica de PostgreSQL.
- **Tiempo de inactividad**: Menor a 1 minuto dependiendo del caso de uso.

## Etiquetas
#PostgreSQL #Replicación #DevOps #BaseDeDatos #Switchover

Fuente: https://github.com/shayonj/pg_easy_replicate
