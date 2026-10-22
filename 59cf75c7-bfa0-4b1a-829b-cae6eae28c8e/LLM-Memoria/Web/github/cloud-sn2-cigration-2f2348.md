---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://github.com/cloud-sn2/cigration"
tema: "PostgreSQL Citus Sharding"
tags: [web]
---
# cloud-sn2/cigration

## Resumen
cigration es una extensión de PostgreSQL diseñada para facilitar la migración en línea de fragmentos (shards) en clústeres Citus, optimizando procesos de expansión y reducción del cluster. El sistema automatiza el movimiento de datos entre nodos Worker manteniendo la consistencia mediante sincronización lógica, minimizando el bloqueo a operaciones de negocio.

## Datos clave
- **Funciones principales**: `cigration_create_rebalance_job()` para generar tareas de migración automática; `cigration_cleanup_error_env()` para reiniciar tareas fallidas.
- **Requisitos técnicos**: PostgreSQL 10+, Citus 9.2+, nivel WAL lógico (`wal_level = 'logical'`) y acceso sin contraseña entre nodos.
- **Limitaciones**: Solo soporta tablas fragmentadas en hash con un solo copias; no funciona con tablas de referencia, múltiples copias o tablas `unlogged`.
- **Instalación**: Requiere compilar (`make install`) o copiar archivos de extensión a la carpeta de PostgreSQL.
- **Cambio crítico**: Tras instalar cigration, `create_distributed_table()` debe reemplazarse por `cigration.cigration_create_distributed_table()`.

## Etiquetas
#citus #postgresql #shard-migration #cloud-infrastructure #dba-tools

Fuente: https://github.com/cloud-sn2/cigration
