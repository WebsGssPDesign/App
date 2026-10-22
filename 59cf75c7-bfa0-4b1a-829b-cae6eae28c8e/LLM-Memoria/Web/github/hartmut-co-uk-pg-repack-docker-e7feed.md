---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/hartmut-co-uk/pg-repack-docker"
tema: "PostgreSQL pg_repack"
tags: [web]
---
# hartmut-co-uk/pg-repack-docker

## Resumen
Esta imagen de Docker proporciona la extensión `pg_repack` para PostgreSQL, permitiendo ejecutar operaciones de reempaquetado de tablas desde el lado del cliente sin modificar la base de datos original. El contenedor se basa en las imágenes oficiales de PostgreSQL y soporta múltiples versiones compatibles entre sí. Ofrece modos nativos o remotos para gestionar mantenimiento de índices y tablas grandes mediante comandos `psql` o ejecutables directos.

## Datos clave
- **Compatibilidad**: Soporta PostgreSQL 10 a 18 con versiones específicas de pg_repack (ej. PG 18 usa v1.5.3).
- **Uso nativo**: Iniciar como base de datos estándar (`docker run -e POSTGRES_PASSWORD=...`).
- **Ejecución remota**: Usar `--network host` y pasar credenciales vía variable de entorno `PGPASSWORD`.
- **Comando principal**: `pg_repack -h localhost -U usuario --dbname=db --table=t1 --dry-run`.

## Etiquetas
#PostgreSQL #Docker #Mantenimiento #pg_repack

Fuente: https://github.com/hartmut-co-uk/pg-repack-docker
