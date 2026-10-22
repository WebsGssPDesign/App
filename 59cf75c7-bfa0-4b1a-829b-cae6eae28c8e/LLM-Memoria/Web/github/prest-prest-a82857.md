---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/prest/prest"
tema: "PostgreSQL TimescaleDB"
tags: [web]
---
# prest/prest

## Resumen
pREST es una API de bajo código que expone interfaces REST y MCP directamente sobre bases de datos PostgreSQL o MySQL existentes. Permite realizar operaciones CRUD, definir rutas SQL personalizadas y gestionar autenticación sin necesidad de programar un backend desde cero. Ofrece alto rendimiento y soporte nativo para múltiples motores de base de datos.

## Datos clave
- **Soporte de bases de datos**: PostgreSQL 9.5+ (por defecto) y MySQL 8.0.19+.
- **Configuración del motor**: Se selecciona mediante la variable `engine = "mysql"` o `PREST_ENGINE=mysql`.
- **Endpoints principales**: `GET /{database}/{schema}/{table}` para acceso directo a datos.
- **Modos de múltiples bases de datos**:
  - *Registro*: Define alias y URLs en `prest.toml` o variables `DATABASE_ALIAS_<n>`.
  - *Sin registro*: Usa `pg.database` y `pg.allowed_databases` (o equivalentes para MySQL).
- **Variables de entorno críticas**: `PREST_PG_URL`, `DATABASE_URL`, `PREST_DB_DATABASE`.

## Etiquetas
#pREST #PostgreSQL #MySQL #API #MCP #LowCode

Fuente: https://github.com/prest/prest
