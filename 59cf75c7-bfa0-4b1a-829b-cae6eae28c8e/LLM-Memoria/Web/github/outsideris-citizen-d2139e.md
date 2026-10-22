---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/outsideris/citizen"
tema: "Terraform Provider Registry"
tags: [web]
---
# outsideris/citizen

## Resumen
Citizen es un registro privado y autoalojable para módulos y proveedores de Terraform que permite a los usuarios gestionar su propio repositorio sin depender de GitHub. El sistema soporta múltiples bases de datos (MySQL, MongoDB, SQLite) y sistemas de almacenamiento como S3 o Google Cloud Storage. Incluye herramientas específicas para publicar módulos y proveedores con firmas GPG automáticas.

## Datos clave
- **Comandos principales**: `citizen server` (inicia el servidor), `citizen module <namespace> <name> <provider> <version>` (publica módulos), `citizen provider <namespace> <type> <version>` (publica proveedores).
- **Variables de entorno críticas**: `CITIZEN_ADDR` (dirección del registro), `CITIZEN_DATABASE_TYPE`, `CITIZEN_STORAGE`.
- **Requisitos técnicos**: HTTPS obligatorio para la comunicación con Terraform CLI.
- **Almacenamiento soportado**: Archivos locales (`file`), AWS S3, Google Cloud Storage (`gcs`).
- **Base de datos**: Prisma ORM utilizado para gestionar migraciones y metadatos.

## Etiquetas
#Terraform #DevOps #InfraestructuraComoCodigo #CloudStorage

Fuente: https://github.com/outsideris/citizen
