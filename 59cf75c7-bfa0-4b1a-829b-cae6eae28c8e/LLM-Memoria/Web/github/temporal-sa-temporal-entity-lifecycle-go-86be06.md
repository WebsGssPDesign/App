---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/temporal-sa/temporal-entity-lifecycle-go"
tema: "Temporal Workflow Patterns"
tags: [web]
---
# temporal-sa/temporal-entity-lifecycle-go

## Resumen
Este proyecto demuestra el Patrón de Ciclo de Vida de Entidades utilizando la SDK para Go en Temporal, modelando un `UserAccount` como entidad persistente. El ejemplo ilustra cómo gestionar estados a través del tiempo mediante workflows que evolucionan o se reinician (`ContinueAsNew`) sin perder su identidad única.

## Datos clave
- **Conceptos**: Patrón de Ciclo de Vida de Entidades (Entity Lifecycle Pattern), Identidad vs Atributos, `ContinueAsNew`.
- **Casos de uso**: Gestión de infraestructura, campañas de marketing, aprobaciones humanas, programas de lealtad.
- **Comandos y variables**: `go run cmd/worker/worker.go`, `tcld namespace search-attributes add`, variables `TEMPORAL_CLIENT_KEY_PATH`, `TEMPORAL_CLIENT_HOSTPORT`.
- **Atributos de búsqueda**: `permissions` (KeywordList), `awaiting_approval` (KeywordList).
- **Pasos críticos**: Crear usuario, asignar permisos, solicitar aprobación, eliminar y restaurar entidad.
- **Mecanismo de determinismo**: Uso de versionado para pasar pruebas de reproducible history (`Test_Orchestration_ReplayHistory`).

## Etiquetas
#Temporal #EntityWorkflow #GoSDK #DistributedSystems #DomainDrivenDesign

Fuente: https://github.com/temporal-sa/temporal-entity-lifecycle-go
