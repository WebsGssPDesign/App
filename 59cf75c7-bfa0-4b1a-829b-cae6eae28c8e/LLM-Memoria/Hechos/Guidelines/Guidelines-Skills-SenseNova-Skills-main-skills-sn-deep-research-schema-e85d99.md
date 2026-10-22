---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-deep-research/schemas/plan.schema.md"
tags: [hecho]
---
# plan.schema.md

## Resumen
Este documento define el contrato de datos para archivos JSON de planes de investigación en el sistema SenseNova. Establece las reglas estrictas para estructurar tareas de búsqueda en modos normales y profundos, asegurando que cada dimensión sea ejecutable de forma independiente antes de la síntesis final.

## Datos clave
- **Archivo**: `plan.json` ubicado en `{report_dir}/`.
- **Modos**: `normal` (sin lentes) y `heavy` (con análisis de perspectiva); el modo `quick` no genera este archivo.
- **Estrategia**: Debe definir dimensiones relevantes (`relevant_dimensions`) y una primaria, eligiendo entre ejes como `by_topic`, `by_entity`, `by_timeline`, etc.
- **Dimensiones**: Cada uno debe tener ID único (regex `^d[1-9]\d*$`), preguntas clave, fuentes categorizadas (ej. `official`, `academic`) y políticas de propiedad del alcance (`scope_ownership`).
- **Ejecución**: Los trabajos de descubrimiento inicial deben agruparse con la búsqueda posterior en el mismo dimensión; no crear dimensiones solo para consolidar evidencia existente.

## Etiquetas
#SenseNova #Investigación #Schema #Planificación

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-deep-research\schemas\plan.schema.md`
