---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://github.com/HypoPG/hypopg"
tema: "PostgreSQL Indexes"
tags: [web]
---
# HypoPG/hypopg

## Resumen
HypoPG es una extensión para PostgreSQL que permite crear índices hipotéticos o virtuales, los cuales no consumen recursos de CPU ni disco. Esta herramienta facilita la evaluación del rendimiento de consultas específicas al simular el uso de índices sin necesidad de crearlos físicamente en la base de datos.

## Datos clave
- **Funciones principales**: `hypopg_create_index` (crea índice virtual), `hypopg_list_indexes` (lista índices disponibles), `hypopg_drop_index`, `hypopg_hide_index` y `hypopg_unhide_index`.
- **Compatibilidad**: Funciona con PostgreSQL 9.2 y versiones superiores.
- **Instalación**: Requiere descomprimir el archivo, ejecutar `sudo make install` y activar la extensión con `CREATE EXTENSION hypopg;` en cada base de datos.
- **Limitaciones**: Los índices son locales al backend (conexión) y solo afectan a consultas de `EXPLAIN` sin la opción `ANALYZE`. Para actualizar la extensión, es necesario eliminarla y volver a crearla.

## Etiquetas
#PostgreSQL #OptimizaciónDeConsultas #HypoPG #BaseDeDatos

Fuente: https://github.com/HypoPG/hypopg
