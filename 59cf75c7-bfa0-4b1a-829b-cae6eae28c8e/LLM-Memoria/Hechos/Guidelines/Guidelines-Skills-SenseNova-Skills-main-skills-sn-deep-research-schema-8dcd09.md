---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-deep-research/schemas/supplement_plan.schema.md"
tags: [hecho]
---
# supplement_plan.schema.md

## Resumen
Este documento define el esquema JSON para `supplement_plan.json`, un archivo que registra las decisiones de investigación adicional por dimensión dentro del proyecto SenseNova. Sirve para estructurar tareas pendientes, justificar brechas en la evidencia y gestionar ítems diferidos antes de generar informes finales.

## Datos clave
- **Proyecto**: SenseNova (Skills/Deep Research).
- **Estructura principal**: Objeto raíz con `meta`, `dimension_id` y dos arrays: `supplement_items` (tareas activas) y `deferred_items` (tareas pospuestas).
- **Campos críticos en `supplement_items`**: `type` (coverage/claim_fix), `gap` (brecha identificada), `question` (pregunta para el agente de investigación), `rationale`, `suggested_sources` y `status`.
- **Estados de flujo**: El campo `status` inicia como `pending` y se actualiza a `resolved`, `partial`, `no_data` o `out_of_scope` tras la ejecución.
- **Manejo de vacíos**: Se requiere generar un plan JSON válido pero vacío si no es necesaria ninguna investigación adicional.

## Etiquetas
#SenseNova #Investigación #EsquemaJSON #GestiónDeDatos

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-deep-research\schemas\supplement_plan.schema.md`
