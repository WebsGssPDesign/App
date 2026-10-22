---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://github.com/go-pg/pg"
tema: "PostgreSQL JSONB"
tags: [web]
---
# go-pg/pg

## Resumen
go-pg es una biblioteca de Golang diseñada como ORM y cliente para PostgreSQL, priorizando el rendimiento y las características nativas de la base de datos. Actualmente se encuentra en modo de mantenimiento crítico, mientras que el desarrollo activo ha migrado al repositorio "Bun" para soportar múltiples bases de datos.

## Datos clave
- **Estado**: Modo de mantenimiento (solo errores críticos); nuevo desarrollo en [Bun](https://bun.uptrace.dev).
- **Tipos de datos**: Soporta básicos, `sql.Null*`, `pg.NullTime`, arrays multidimensionales, hstore y tipos compuestos.
- **Operaciones ORM**: Transacciones, consultas preparadas, notificaciones (`LISTEN`/`NOTIFY`), carga masiva (bulk insert/update/delete) y relaciones (has one, belongs to).
- **Optimización**: Conexiones con *pooling* automático, soporte para *circuit breaker*, reintentos en errores de red y estimación de filas con `CountEstimate`.
- **Comandos SQL**: Uso de `COPY FROM/TO`, `INSERT ... ON CONFLICT DO UPDATE` y expresiones comunes (`WITH`).

## Etiquetas
#Go #PostgreSQL #ORM #Bun #Database

Fuente: https://github.com/go-pg/pg
