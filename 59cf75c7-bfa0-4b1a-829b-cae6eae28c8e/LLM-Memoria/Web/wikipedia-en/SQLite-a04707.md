---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/SQLite"
tema: "PostgreSQL JSONB Indexing"
tags: [web]
---
# SQLite

## Resumen
SQLite es un motor de base de datos relacional ligero y de código abierto escrito en C, diseñado para ser una librería integrada directamente en aplicaciones en lugar de funcionar como un servicio independiente. Aunque sigue gran parte del estándar SQL y garantiza la integridad ACID, carece de algunas características avanzadas como vistas materializadas y tiene un sistema de tipos dinámico que permite flexibilidad pero reduce la estricta validación de datos por defecto.

## Datos clave
- **Naturaleza**: Librería embebida (no es una aplicación standalone).
- **Lenguaje**: Escrito en C, con bindings para muchos lenguajes de programación.
- **Diseño**: Arquitectura sin servidor (serverless) que opera a nivel de archivo único.
- **Tipos de datos**: Sistema dinámico y débil por defecto (permite insertar cadenas en columnas enteras), aunque desde 2021 soporta tablas "STRICT".
- **Historia**: Diseñado por D. Richard Hipp en el año 2000 para sistemas de control de daños en buques.
- **Versión 3.7**: Introdujo la escritura anticipada (WAL) para permitir lecturas y escrituras concurrentes.
- **Almacenamiento**: Todo el esquema y los datos residen en un único archivo cross-platform.

## Etiquetas
#SQLite #BaseDeDatos #SQL #CódigoAbierto #DesarrolloSoftware

Fuente: https://en.wikipedia.org/wiki/SQLite
