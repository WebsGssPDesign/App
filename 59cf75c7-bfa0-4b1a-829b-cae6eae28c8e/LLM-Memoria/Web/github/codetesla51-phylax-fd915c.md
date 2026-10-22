---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/codetesla51/phylax"
tema: "PostgreSQL Logical Replication Slots"
tags: [web]
---
# codetesla51/phylax

## Resumen
Phylax es un cliente ligero en Go para replicación lógica de PostgreSQL que transmite cambios de datos en tiempo real. El software gestiona automáticamente la configuración del servidor, como las ranuras y publicaciones, permitiendo a los usuarios recibir actualizaciones mediante stdout, webhooks o una consola integrada con métricas en vivo.

## Datos clave
- **Idioma:** Go (binario único o librería embebida).
- **Funcionalidad principal:** Streaming de cambios (`insert`, `update`, `delete`, `truncate`) al momento del commit.
- **Gestión automática:** Provisiona ranuras (*slots*) y publicaciones; reconecta con retroceso (*backoff*) y reanuda desde la posición LSN guardada tras un reinicio.
- **Interfaz:** Consola en vivo accesible vía `/dashboard` con gráficos de retraso (*sparkline*) y KPIs.
- **Requisito del servidor:** `wal_level = logical` en PostgreSQL.
- **Instalación CLI:** `go install github.com/codetesla51/phylax/cmd/phylax@latest`.

## Etiquetas
#PostgreSQL #Go #CDC #ReplicaciónLógica #DevOps

Fuente: https://github.com/codetesla51/phylax
