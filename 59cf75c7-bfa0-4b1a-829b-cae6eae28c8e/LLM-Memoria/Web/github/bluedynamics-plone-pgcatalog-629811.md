---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/bluedynamics/plone-pgcatalog"
tema: "PostgreSQL JSONB Indexing"
tags: [web]
---
# bluedynamics/plone-pgcatalog

## Resumen
plone-pgcatalog es un catálogo para Plone que sustituye los índices BTrees de ZCatalog por consultas SQL sobre datos JSONB en PostgreSQL, mejorando el rendimiento y reduciendo la presión en la caché de ZODB. El sistema soporta todos los tipos de índice estándar, búsqueda completa con stemming multilingüe y ranking BM25 opcional sin necesidad de extensiones C complejas.

## Datos clave
- **Requisitos**: Python 3.12+, PostgreSQL 15+ (recomendado 17), `zodb-pgjsonb`, Plone 6.
- **Instalación**: Comando `pip install plone-pgcatalog` y configuración en `zope.conf` con el perfil `plone.pgcatalog:default`.
- **Características principales**: Soporte para índices de fecha recurrente, búsqueda full-text con 30 idiomas, ranking BM25 automático si se detectan extensiones `vchord_bm25` y `pg_tokenizer`.
- **Migración**: Requiere sitio previo en `zodb-pgjsonb`; implica reiniciar Zope, aplicar el perfil de migración y ejecutar `catalog.clearFindAndRebuild()`.
- **Rendimiento**: Escrituras transaccionales atómicas con el estado del objeto y cero presión de caché ZODB por objetos BTree.

## Etiquetas
#Plone #PostgreSQL #Catálogo #JSONB #Python

Fuente: https://github.com/bluedynamics/plone-pgcatalog
