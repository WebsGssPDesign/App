---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/legrandlegrand/pg_stat_sql_plans"
tema: "PostgreSQL pg_stat_statements"
tags: [web]
---
# legrandlegrand/pg_stat_sql_plans

## Resumen
`pg_stat_sql_plans` es una extensión de PostgreSQL derivada de `pg_stat_statements` que añade la columna `planid`, calculada mediante un hash del texto normalizado del plan de ejecución. Esta herramienta permite rastrear y analizar el rendimiento de consultas con mayor granularidad, diferenciando entre tiempos de planificación, ejecución y actividades específicas de la extensión.

## Datos clave
- **Requisitos**: PostgreSQL >= 14; debe cargarse en `shared_preload_libraries`.
- **Columnas principales**: `queryid` (hash del SQL normalizado), `planid` (hash del plan), `qpid` (combinación de ambos).
- **Funciones útiles**: `pgssp_normalize_query(text)` para limpiar consultas, `pgssp_backend_qpid(pid)` para obtener el ID durante la ejecución activa.
- **Métricas temporales**: `plan_time`, `exec_time`, `extn_time` (tiempo en la extensión), `first_call`, `last_call`.
- **Configuración GUC**: `track_errors` (incluye fallos), `explain` (escribe planes en logs), `max` (límite de entradas).
- **Advertencia**: Versión Alpha, no usar en producción.

## Etiquetas
#PostgreSQL #Optimización #Rendimiento #ExtensiónSQL

Fuente: https://github.com/legrandlegrand/pg_stat_sql_plans
