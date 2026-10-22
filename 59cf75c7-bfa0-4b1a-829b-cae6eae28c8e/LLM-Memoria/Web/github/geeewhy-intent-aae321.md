---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/geeewhy/intent"
tema: "Temporal Workflow Patterns"
tags: [web]
---
# geeewhy/intent

## Resumen
Intent es una implementación de referencia en TypeScript para backends multi-inquilino basados en origen de eventos. Combina patrones CQRS y DDD con la ejecución de flujos duraderos proporcionada por Temporal, garantizando seguridad y recuperación ante fallos.

## Datos clave
- **Tecnología base:** TypeScript y Temporal (para workflows duraderos).
- **Patrones de arquitectura:** CQRS, DDD, Hexágono "ports-first".
- **Seguridad:** Aislamiento por inquilino mediante IDs propagados y políticas RLS nativas de PostgreSQL.
- **Garantías:** Procesamiento sin pérdida de datos (lossless), entrega exactamente una vez y recuperación automática ante fallos o reinicios.
- **Herramientas incluidas:** Scanner de deriva de esquemas, lint para seguridad, CLI interactivo para bootstrap y DevX-UI para visualización de flujos.
- **Gobernanza:** Soporte para evolución de esquemas mediante upcasting seguro de eventos inmutables.

## Etiquetas
#event-sourcing #CQRS #Temporal #multi-tenancy #TypeScript #DDD

Fuente: https://github.com/geeewhy/intent
