---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Postgres-XL"
tema: "PostgreSQL Citus Sharding"
tags: [web]
---
# Postgres-XL

## Resumen
Postgres-XL fue un sistema de gestión de bases de datos relacionales distribuidas basado en PostgreSQL, diseñado para escalar horizontalmente mediante una arquitectura "shared-nothing". Aunque su desarrollo cesó en octubre de 2018, muchas de sus ideas sobre consultas paralelas y particionamiento fueron adoptadas posteriormente por la comunidad de PostgreSQL.

## Datos clave
- **Nombre**: eXtensible Lattice (XL).
- **Estado final**: Última versión en septiembre de 2018; desarrollo detenido y sitio web offline.
- **Arquitectura**: Requiere un nodo central Global Transaction Manager (GTM) para transacciones consistentes.
- **Requisitos de red**: Necesita una interconexión rápida entre nodos, por lo que no es apto para clusters geográficamente distribuidos.
- **Estrategias de datos**: Tablas totalmente replicadas (para tablas pequeñas) o sharding horizontal transparente (para escalabilidad en escritura).
- **Predecesor/Origen**: Basado en Postgres-XC; adquirido por TransLattice y abierto en 2014.

## Etiquetas
#PostgreSQL #BasesDeDatosDistribuidas #HistoriaTecnológica #BigData #TransLattice

Fuente: https://en.wikipedia.org/wiki/Postgres-XL
