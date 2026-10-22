---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-deep-research/schemas/perspective_feedback.schema.md"
tags: [hecho]
---
# perspective_feedback.schema.md

## Resumen
Este documento define el contrato de formato para archivos Markdown que registran la revisión de perspectivas en un proceso de investigación profunda. Su función es diagnosticar brechas de cobertura, proponer preguntas de investigación adicionales y delimitar el contexto de escritura sin generar afirmaciones factuales finales.

## Datos clave
- **Ubicación**: `{report_dir}/sub_reports/d{N}.perspectives/{lens.axis}_{lens.value}.md`
- **Estructura obligatoria**: Secciones para "Lens 定位", "写作补充边界", "需要补研后才能使用", "探索性搜索线索" y "维度内补研需求".
- **Flujo de trabajo**: Los hallazgos aquí no son evidencia formal; deben ser verificados por el rol `research` antes de escribirse en `d{N}.evidence.json`.
- **Consumo**: El agente `supplement-planner` lee este archivo junto con `review.md` y `evidence.json`, pero los agentes del reporte final no deben usarlo como evidencia directa.

## Etiquetas
#investigación #esquema #metadatos

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-deep-research\schemas\perspective_feedback.schema.md`
