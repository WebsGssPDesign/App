---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-deep-research/agents/supplement-planner.md"
tags: [hecho]
---
# supplement-planner.md

## Resumen
Este documento define las reglas operativas para el agente "Supplement Planner", encargado de analizar evidencias, revisiones y perspectivas dentro de un único dimensión de investigación. Su función es filtrar tareas pendientes mediante una decisión binaria: clasificarlas como ítems de investigación activa (`supplement_items`) que requieren datos nuevos, o como ítems diferidos (`deferred_items`) si ya están cubiertos o son solo contextuales.

## Datos clave
- **Entradas**: `plan.json`, `evidence.json`, `review.md` y archivos `perspectives/*.md` del dimensión objetivo.
- **Prohibido**: No realizar búsquedas web, no leer fuera del dimensión actual ni inventar nuevas fuentes en esta fase.
- **Lógica de decisión**: Solo se crea un ítem de suplemento si la evidencia actual es insuficiente para responder preguntas clave o validar afirmaciones críticas.
- **Salida**: Archivo `supplement_plan.json` con arrays estructurados (`supplement_items`, `deferred_items`) y metadatos.
- **Validación**: El esquema se define en `sn-deep-research/schemas/supplement_plan.schema.md`.

## Etiquetas
#investigación #planificación #evidencia #automatización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-deep-research\agents\supplement-planner.md`
