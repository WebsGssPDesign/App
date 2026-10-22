---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/timescale/timescaledb"
tema: "PostgreSQL TimescaleDB"
tags: [web]
---
# timescale/timescaledb

## Resumen
TimescaleDB es una extensión de PostgreSQL diseñada para análisis en tiempo real de datos series temporales y eventos. El texto presenta una guía rápida para instalarla localmente mediante Docker o un script automático, crear hipertablas con compresión nativa (columnstore) e insertar grandes volúmenes de datos simulando sensores IoT.

## Datos clave
- **Instalación recomendada:** `curl -sL https://tsdb.co/start-local | sh` (solo desarrollo).
- **Puerto de conexión:** 6543 (para evitar conflictos con PostgreSQL estándar en 5432).
- **Comando Docker:** `docker run -d --name timescaledb -p 6543:5432 ... timescale/timescaledb-ha:pg18`.
- **Creación de hipertabla:** Uso del comando `WITH (tsdb.hypertable)` al crear la tabla.
- **Compresión automática:** Activar con `SET timescaledb.enable_direct_compress_insert = on` durante la inserción.
- **Optimización post-inserción:** Llamada a `convert_to_columnstore(ch, recompress := true)` para cada chunk.
- **Rendimiento:** Generación de ~7.8 millones de lecturas en 90 días con consultas analíticas instantáneas.

## Etiquetas
#basesdedatos #tiemporeal #postgreSQL #series-temporales #IoT

Fuente: https://github.com/timescale/timescaledb
