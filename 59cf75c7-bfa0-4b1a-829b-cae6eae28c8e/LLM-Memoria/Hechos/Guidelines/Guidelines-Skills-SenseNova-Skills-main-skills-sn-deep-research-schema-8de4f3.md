---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-deep-research/schemas/evidence.schema.md"
tags: [hecho]
---
# evidence.schema.md

## Resumen
Este documento define el contrato de datos para archivos `evidence.json` en investigaciones automatizadas, estableciendo reglas estrictas para estructurar hallazgos, afirmaciones y fuentes. Su función es garantizar la integridad referencial, la trazabilidad de las pruebas y la calidad de los datos en informes generados por IA sobre dimensiones específicas de un estudio.

## Datos clave
- **Estructura**: Jerarquía `key_findings` (conclusión) -> `claims` (afirmación verificable) -> `evidence` (prueba textual).
- **Tipos de afirmaciones**: `factual` (datos), `interpretive` (análisis), `projective` (predicciones).
- **Calidad de fuentes**: Clasificación en `primary`, `secondary` y `tertiary`.
- **Identificadores únicos**: IDs para dimensiones (`d1`), afirmaciones (`d1.c1`) y contexto de escritura (`d1.w1`).
- **Tipos de citas**: `direct` (texto exacto), `paraphrase` (resumen fiel) o `numeric` (datos con contexto).

## Etiquetas
#investigación #esquema_de_datos #verificación_de_hechos #IA

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-deep-research\schemas\evidence.schema.md`
