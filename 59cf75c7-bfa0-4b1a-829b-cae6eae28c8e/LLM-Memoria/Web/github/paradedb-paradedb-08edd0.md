---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://github.com/paradedb/paradedb"
tema: "PostgreSQL Vector Search"
tags: [web]
---
# paradedb/paradedb

## Resumen
ParadeDB es una extensión de PostgreSQL que integra capacidades avanzadas de búsqueda (texto completo y vectores), análisis OLAP y agregaciones directamente en la base de datos. Al utilizar bibliotecas en Rust como Tantivy y Apache DataFusion, permite ejecutar consultas complejas con ACID sin necesidad de sistemas externos.

## Datos clave
- **Funcionalidades principales**: Búsqueda de texto completo (BM25), búsqueda vectorial, búsqueda híbrida, filtrado, facetas y agregaciones.
- **Tecnología base**: Construida sobre la extensión `pgrx` para conectar Rust con PostgreSQL.
- **Instalación local**: Se ejecuta mediante un script de Docker (`curl -fsSL https://paradedb.com/install.sh | sh`).
- **Integraciones**: Soporte nativo para ORMs como Drizzle, Django y SQLAlchemy, además de plugins para agentes de IA.
- **Almacenamiento**: Utiliza almacenamiento columnar para optimizar el rendimiento en análisis.

## Etiquetas
#PostgreSQL #VectorSearch #FullTextSearch #Rust #OLAP

Fuente: https://github.com/paradedb/paradedb
