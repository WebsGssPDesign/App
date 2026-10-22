---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/TeamSpringbird/effect-temporal"
tema: "Temporal Workflow Signals"
tags: [web]
---
# TeamSpringbird/effect-temporal

## Resumen
Este proyecto permite definir y ejecutar flujos de trabajo duraderos en Temporal utilizando la librería Effect, garantizando tipado estricto para esquemas, errores y composición. Ofrece una única definición compartida entre el servidor y los clientes para evitar desincronizaciones y facilita pruebas unitarias sin necesidad del motor completo.

## Datos clave
- **Conceptos**: `Workflow.make`, `defineActivity`, `defineDeferred` (para señales), `workflowBundle`.
- **Características**: Idempotencia global basada en claves de digest, cancelación compuesta que interrumpe fibras, y determinismo mediante un programador de microtareas.
- **Tipado**: Esquemas para payloads, resultados y fallos en todas las transacciones (actividades, señales, actualizaciones).
- **Pruebas**: `makeTestWorkflowOps` para entornos in-memoria y `startWorkflowTestHarness` con salto de tiempo real.
- **Instalación**: `pnpm add @springbird/effect-temporal`.

## Etiquetas
#temporal #effect-ts #workflows #durabilidad #typescript

Fuente: https://github.com/TeamSpringbird/effect-temporal
