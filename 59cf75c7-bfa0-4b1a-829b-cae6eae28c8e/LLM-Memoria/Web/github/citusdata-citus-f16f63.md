---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://github.com/citusdata/citus"
tema: "PostgreSQL Citus Sharding"
tags: [web]
---
# citusdata/citus

## Resumen
Citus es una extensión de código abierto para PostgreSQL que transforma la base de datos en un sistema distribuido capaz de escalar horizontalmente. Permite distribuir tablas entre nodos, replicar tablas de referencia y optimizar consultas analíticas mediante un motor de ejecución paralelo. Esta solución mantiene la compatibilidad con las herramientas nativas de Postgres mientras resuelve problemas de rendimiento al crecer el volumen de datos.

## Datos clave
- **Arquitectura**: Extensiones distribuidas (shards), tablas de referencia replicadas y almacenamiento columnar para compresión.
- **Escalabilidad**: Capacidad de agregar nodos trabajadores dinámicamente y redistribuir fragmentos de datos.
- **Casos de uso**: Aplicaciones multiinquilino, consultas analíticas rápidas, series temporales y datos IoT en tiempo real.
- **Integración**: Compatible con versiones recientes de PostgreSQL y herramientas estándar (PostGIS, índices avanzados).
- **Implementación**: Disponible como extensión local o servicio gestionado en Azure Database for PostgreSQL Flexible Server.

## Etiquetas
#Citus #PostgreSQL #BasesDeDatosDistribuidas #Escalabilidad #OpenSource

Fuente: https://github.com/citusdata/citus
