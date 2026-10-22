---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/pg2es/search-replica"
tema: "PostgreSQL Logical Decoding Replication"
tags: [web]
---
# pg2es/search-replica

## Resumen
pg2es/search-replica es una herramienta que replica datos de una base de datos PostgreSQL primaria a un índice de Elasticsearch o OpenSearch mediante el protocolo de replicación lógica nativo. Este enfoque garantiza sincronización casi en tiempo real sin depender de consultas adicionales ni colas externas, priorizando la velocidad y la eficiencia.

## Datos clave
- **Mecanismo**: Utiliza slots de replicación lógicos de PostgreSQL para consistencia y tolerancia a fallos.
- **Inicialización**: La carga inicial se realiza mediante el comando `COPY`.
- **Soporte de tipos**: Maneja campos JSON, tipos compuestos, arrays y enumeraciones (excepto arrays de tipos compuestos).
- **Configuración con comentarios**: Permite definir rutas (`routing`), `_id`, uniones padre/hijo e inlining directamente en los comentarios del esquema.
- **Variables de entorno principales**: `PG_SLOT`, `PG_PUBLICATION`, `SEARCH_HOST`, `SEARCH_BULK_SIZE`.
- **Limitaciones conocidas**: No soporta inlining 1:1; la eliminación de un documento borra todos sus datos embebidos (DELETE CASCADE) sin posibilidad de restauración.

#PostgreSQL #Elasticsearch #OpenSearch #ReplicaciónLógica #DevOps

Fuente: https://github.com/pg2es/search-replica
