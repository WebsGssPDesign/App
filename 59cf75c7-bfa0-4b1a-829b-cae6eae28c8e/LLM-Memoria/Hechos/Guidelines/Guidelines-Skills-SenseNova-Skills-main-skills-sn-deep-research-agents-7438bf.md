---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-deep-research/agents/report-planner.md"
tags: [hecho]
---
# report-planner.md

## Resumen
Este documento define el flujo de trabajo del Agente Planificador de Informes para el modo "heavy" de investigación profunda. Su función es organizar la evidencia recopilada en un esquema estructurado (outline) que respeta los límites de las pruebas y se alinea con las tareas específicas del lector, evitando estructuras genéricas.

## Datos clave
- **Proyecto**: `SenseNova-Skills` / `sn-deep-research`.
- **Tecnologías**: JSON para el esquema (`outline.json`, `.evidence_subset.json`), Python para validación (`validate_outline.py`).
- **Decisiones de diseño**: El tipo de unidad se deriva de la tarea del lector y la forma de la evidencia, no del paradigma principal. Las matrices y líneas de tiempo son unidades principales, no solo visuales auxiliares.
- **Límites estrictos**: Máximo 10 referencias de evidencia por elemento y 30 claims únicos por unidad.
- **Rutas de archivos**: `{report_dir}/outline.json`, `{report_dir}/content_units/{unit_id}.evidence_subset.json`.
- **Comandos críticos**: Ejecución del script `validate_outline.py` con rutas absolutas expandidas para verificar la integridad antes de finalizar.

## Etiquetas
#SenseNova #DeepResearch #AgentePlanificador #GestiónDeEvidencia

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-deep-research\agents\report-planner.md`
