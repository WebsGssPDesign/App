---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "skills/agente-research-academico/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define un flujo autónomo para investigación académica que integra búsqueda en Semantic Scholar, síntesis de artículos y redacción de informes estructurados. Su objetivo es permitir una recolección profunda de evidencia validada antes de generar reportes finales con citas automáticas, evitando dependencias de APIs comerciales costosas.

## Datos clave
- **Entrada unificada**: `/skill sn-deep-research "Tema" --language es --format {report,paper,table,memo}`.
- **Modos operativos**: `quick` (ejecución en una pasada), `normal` (planificación y síntesis paralela) y `heavy` (revisión exhaustiva con múltiples perspectivas).
- **Fuentes autorizadas**: Exclusivamente Semantic Scholar API para datos de citas; Google Scholar está prohibido por falta de API oficial y riesgos legales.
- **Restricciones**: No crear archivos auxiliares como `format.json`; no generar propuestas previas antes de la investigación.

## Etiquetas
#investigación-académica #semantic-scholar #automatización

Fuente: `F:\automatizaciones\homeLab\skills\agente-research-academico\SKILL.md`
