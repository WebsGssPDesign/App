---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/xstevens/decoderbufs"
tema: "PostgreSQL Logical Decoding"
tags: [web]
---
# xstevens/decoderbufs

## Resumen
decoderbufs es un plugin de salida para el decodificador lógico de PostgreSQL diseñado para entregar datos en formato Protocol Buffers. El proyecto se encuentra inactivo y su autor recomienda utilizar la versión mantenida activamente de Debezium para nuevos desarrollos.

## Datos clave
- **Estado**: Inactivo (PoC de hace 4 años); alternativa activa: [Debezium's fork](https://github.com/debezium/postgres-decoderbufs).
- **Compatibilidad**: PostgreSQL 9.4+, Protocol Buffers 3.x, protobuf-c 1.2.x, PostGIS 2.1.x.
- **Configuración necesaria**: `shared_preload_libraries = 'decoderbufs'`, `wal_level = logical`.
- **Permisos**: Requiere configuración en `pg_hba.conf` para el usuario de replicación (`replication`).
- **Uso SQL**: Crear ranura con `pg_create_logical_replication_slot('nombre', 'decoderbufs')`.
- **Consumo**: Consultas como `pg_logical_slot_peek_changes` o `pg_logical_slot_get_changes`.
- **Tipos mapeados**: Booleans, enteros (int32/int64), flotantes, cadenas y geometrías PostGIS se convierten a campos específicos de Protocol Buffers.

## Etiquetas
#PostgreSQL #ProtocolBuffers #ReplicaciónLógica #Debezium #OpenSource

Fuente: https://github.com/xstevens/decoderbufs
