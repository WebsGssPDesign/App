---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-deep-research/agents/plan.md"
tags: [hecho]
---
# plan.md

## Resumen
Este documento define el contrato de ejecución y las responsabilidades del "Plan Agent" dentro de un sistema de investigación profunda. Su función es transformar los requisitos del usuario en una estructura de investigación ejecutable, validable y rastreable mediante la generación de un archivo `plan.json`. Este plan organiza las tareas en dimensiones independientes que cubren todas las restricciones del usuario sin duplicar esfuerzos de búsqueda.

## Datos clave
- **Producto principal**: Generación de `{report_dir}/plan.json` basado en el esquema y validador proporcionados.
- **Entradas críticas**: `query`, `confirmed_scope` (restricciones duras), `mode` (`normal` o `heavy`) y `format`.
- **Estrategia de descomposición**: Selección dinámica del eje de análisis (ej. entidad, tiempo, causalidad) según el tipo de investigación; no usar matrices fijas por defecto.
- **Gestión de alcance**: Uso obligatorio de `scope_ownership` (`owns`, `excludes`, `shared_topics`) para definir límites claros entre dimensiones paralelas y evitar redundancia.
- **Preguntas clave (KQ)**: Deben especificar "celdas" de contenido concretos (objetos, métricas, contextos) en lugar de ser preguntas abstractas sobre cómo entender algo.
- **Modo Heavy**: Los `lenses` solo se incluyen si hay alta controversia o riesgo que requiera diagnóstico de cobertura.

## Etiquetas
#investigación #planificación #agentes_autónomos #gestión_de_proyectos

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-deep-research\agents\plan.md`
