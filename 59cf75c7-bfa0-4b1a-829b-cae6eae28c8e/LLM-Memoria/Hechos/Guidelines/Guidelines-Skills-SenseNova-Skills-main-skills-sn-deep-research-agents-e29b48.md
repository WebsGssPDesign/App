---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-deep-research/agents/report-stitcher.md"
tags: [hecho]
---
# report-stitcher.md

## Resumen
Este documento define al agente "Report Stitcher", encargado de ensamblar unidades de contenido generadas por investigación profunda en un informe final coherente. Su función es calibrar la estructura, terminología y resúmenes sin alterar los hechos, datos o evidencia originales de las fuentes.

## Datos clave
- **Entrada**: `outline.json`, archivos `.md` de unidades de contenido, y parámetros del payload (idioma, formato).
- **Límites de edición**: Permite ajustar títulos H1, resúmenes L0, conectores breves y consistencia Markdown. Prohíbe modificar hechos, números, citas, tablas o la estructura interna de las unidades.
- **Control de calidad (Step 1)**: Valida el contrato de renderizado (prosa, tablas, listas, Mermaid, etc.) antes de escribir. Si falla, retorna un error específico sin generar salida.
- **Estructura de salida**: Genera `stitched.md` respetando decisiones organizacionales sobre TOC y numeración de encabezados.
- **Respuestas de fallo/completado**: Devuelve reportes estructurados (`Stitch Failed` o `Stitch Complete`) con métricas de cambios y veredictos.

## Etiquetas
#agentes #redacción_técnica #control_de_calidad #markdown #investigación

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-deep-research\agents\report-stitcher.md`
