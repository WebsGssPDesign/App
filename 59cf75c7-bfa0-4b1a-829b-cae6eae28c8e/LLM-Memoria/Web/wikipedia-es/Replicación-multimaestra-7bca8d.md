---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://es.wikipedia.org/wiki/Replicaci%C3%B3n_multimaestra"
tema: "PostgreSQL Change Data Capture"
tags: [web]
---
# Replicación multimaestra

## Resumen
La replicación multimaestra es un esquema de bases de datos que permite a cualquier nodo del grupo modificar y actualizar los datos, distribuyendo estos cambios automáticamente al resto de la red. A diferencia del modelo maestra-esclava, este enfoque ofrece mayor disponibilidad y flexibilidad geográfica, aunque introduce desafíos significativos en cuanto a consistencia y resolución de conflictos.

## Datos clave
- **Definición**: Método donde múltiples nodos pueden escribir datos simultáneamente sin un único maestro exclusivo.
- **Ventajas principales**: Alta disponibilidad (si un nodo falla, otros continúan operando) y distribución física flexible.
- **Desventajas principales**: Posible inconsistencia de datos debido a la asincronía, complejidad en la resolución de conflictos y latencia en la comunicación.
- **Métodos de implementación**: Basado en Log (solo asíncrono) y Basado en Trigger (síncrono o asíncrono).
- **Herramientas mencionadas**: OpenLDAP (v2.4+), MySQL/MariaDB (Cluster v6.3+), PostgreSQL (con herramientas como Bucardo, PgPool-II), Ingres Replicator y SymmetricDS.

## Etiquetas
#bases_de_datos #replicación #multimaestra #disponibilidad #consistencia

Fuente: https://es.wikipedia.org/wiki/Replicaci%C3%B3n_multimaestra
