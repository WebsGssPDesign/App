---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/reorg/pg_repack"
tema: "PostgreSQL pg_repack"
tags: [web]
---
# reorg/pg_repack

## Resumen
pg_repack es una extensión de PostgreSQL diseñada para eliminar el "bloat" (datos redundantes) en tablas e índices y restaurar el orden físico de los índices agrupados. A diferencia de las herramientas nativas como CLUSTER o VACUUM FULL, opera en línea manteniendo la base de datos accesible sin bloqueos exclusivos durante la reorganización.

## Datos clave
- **Funcionalidad principal**: Elimina espacio desperdiciado y reordena físicamente los índices agrupados (clustered indexes).
- **Ventaja operativa**: Funciona en línea (online) sin adquirir bloqueos exclusivos, evitando tiempos de inactividad.
- **Eficiencia**: Su rendimiento es comparable al comando CLUSTER nativo, pero con mayor flexibilidad.
- **Relación histórica**: Es un fork del proyecto pg_reorg, actualizado para solucionar limitaciones y errores de versiones anteriores (como soporte para PostgreSQL 9.2).
- **Nuevas capacidades (v1.2)**: Soporte para construcción paralela de índices y la posibilidad de reconstruir solo índices específicos.

## Etiquetas
#PostgreSQL #OptimizaciónDeBaseDeDatos #pg_repack #Mantenimiento

Fuente: https://github.com/reorg/pg_repack
