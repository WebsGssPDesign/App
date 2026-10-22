---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://github.com/cloudnative-pg/cloudnative-pg"
tema: "Kubernetes Operators"
tags: [web]
---
# cloudnative-pg/cloudnative-pg

## Resumen
CloudNativePG es una plataforma de código abierto y el operador más popular para gestionar bases de datos PostgreSQL en entornos Kubernetes. Diseñado por expertos, automatiza el ciclo completo operativo mediante integración directa con la API de Kubernetes, eliminando la necesidad de herramientas externas de alta disponibilidad.

## Datos clave
- **Funcionalidades principales:** Gestión automática de failover (elección de nuevo primario), escalado de réplicas de lectura y actualizaciones rolling controladas.
- **Recursos gestionados:** Cluster, Backup, Database, Pooler, Publication, Subscription, entre otros.
- **Principios de diseño:** Enfoque nativo en Kubernetes, contenedores inmutables y reconciliación automática del estado deseado.
- **Limitaciones:** Exclusivo para PostgreSQL estándar (sin soporte a forks ni otras bases de datos como MariaDB) y requiere Kubernetes vanilla.

## Etiquetas
#PostgreSQL #Kubernetes #CloudNativePG #BasesDeDatos

Fuente: https://github.com/cloudnative-pg/cloudnative-pg
