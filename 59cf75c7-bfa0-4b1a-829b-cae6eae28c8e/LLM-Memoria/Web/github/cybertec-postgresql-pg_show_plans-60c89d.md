---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/cybertec-postgresql/pg_show_plans"
tema: "PostgreSQL Query Planning"
tags: [web]
---
# cybertec-postgresql/pg_show_plans

## Resumen
pg_show_plans es una extensión de PostgreSQL diseñada para visualizar los planes de ejecución de todas las sentencias SQL en tiempo real. La herramienta almacena estos datos en una tabla hash dentro del espacio compartido, permitiendo su consulta mediante vistas y funciones específicas.

## Datos clave
- **Instalación**: Requiere compilar con `make` y añadirse a `shared_preload_libraries` en `postgresql.conf`.
- **Limitación crítica**: La tabla hash interna no es redimensionable; se llena y deja de aceptar nuevos planes.
- **Formatos de salida**: Soporta JSON, YAML, XML o texto (variable `pg_show_plans.plan_format`).
- **Vistas principales**:
  - `pg_show_plans`: Muestra ID del proceso (`pid`), nivel de anidación y plan.
  - `pg_show_plans_q`: Incluye la expresión SQL original correspondiente al plan.
- **Impacto en rendimiento**: Los benchmarks indican una penalización de aproximadamente el 14% en transacciones por segundo (TPS).
- **Control**: Se puede habilitar o deshabilitar mediante la variable GUC `pg_show_plans.is_enabled`.

#postgresql #optimización #monitorización #bases_de_datos

Fuente: https://github.com/cybertec-postgresql/pg_show_plans
