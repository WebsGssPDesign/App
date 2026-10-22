---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://github.com/2ndQuadrant/pglogical"
tema: "PostgreSQL Logical Replication"
tags: [web]
---
# 2ndQuadrant/pglogical

## Resumen
pglogical es una extensión para PostgreSQL que facilita la replicación lógica de datos mediante un modelo de publicación y suscripción, superando en velocidad a soluciones anteriores como Slony. Aunque el proyecto original sigue activo, EnterpriseDB ha centrado su desarrollo futuro en Postgres Distributed, una evolución con capacidades avanzadas como DDL replication. La herramienta permite replicar bases de datos completas o selectivamente entre nodos compatibles.

## Datos clave
- **Compatibilidad**: Funciona en PostgreSQL 9.4 y superiores; requiere extensiones idénticas en proveedor (Provider) y suscriptor (Subscriber).
- **Restricciones de esquema**: Las tablas deben tener nombres, esquemas, tipos de datos y claves primarias idénticos en ambos lados. Las restricciones del suscriptor pueden ser más permisivas que las del proveedor.
- **Instalación**: Disponible como paquetes RPM (RHEL/CentOS/Fedora) o DEB (Debian/Ubuntu), o desde el código fuente. Los comandos de instalación varían según la versión de PostgreSQL (ej: `yum install pglogical_17`).
- **Funcionalidades**: Soporta filtrado de filas, replicación cruzada de versiones mayores y resolución automática de conflictos en nodos múltiples.

## Etiquetas
#PostgreSQL #Replicación #pglogical #Infraestructura

Fuente: https://github.com/2ndQuadrant/pglogical
