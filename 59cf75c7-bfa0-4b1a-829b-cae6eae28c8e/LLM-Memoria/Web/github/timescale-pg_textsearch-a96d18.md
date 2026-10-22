---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/timescale/pg_textsearch"
tema: "PostgreSQL Full-Text Search"
tags: [web]
---
# timescale/pg_textsearch

## Resumen
pg_textsearch es una extensión para PostgreSQL que implementa búsqueda de texto completo con ranking BM25, permitiendo consultas rápidas y ordenadas mediante un operador sintáctico simple. Soporta versiones 17 y 18 del motor de base de datos y ofrece opciones configurables para la normalización de longitud y frecuencia de términos.

## Datos clave
- **Operador principal**: `content <@> 'query'` devuelve documentos ordenados por relevancia (BM25).
- **Configuración BM25**: Parámetros ajustables `k1` (frecuencia, default 1.2) y `b` (normalización de longitud, default 0.75).
- **Instalación**: Se añade a `shared_preload_libraries` en `postgresql.conf`.
- **Creación de índice**: `CREATE INDEX ... USING bm25(column)` con opción `text_config`.
- **Filtrado booleano**: Uso del operador `@@` y sintaxis `to_tsquery` para filtrar antes o después del ranking.
- **Compatibilidad**: PostgreSQL 17, 18 (y beta de 19).

## Etiquetas
#PostgreSQL #BM25 #BusquedaTexto #ExtensionesSQL #Timescale

Fuente: https://github.com/timescale/pg_textsearch
