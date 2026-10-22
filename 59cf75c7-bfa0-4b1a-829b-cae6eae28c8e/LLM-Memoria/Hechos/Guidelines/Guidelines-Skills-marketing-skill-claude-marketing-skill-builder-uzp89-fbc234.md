---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/marketing-skill-claude-marketing-skill-builder-uzp891/skills/competitor-research/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía define un flujo de trabajo para generar informes estructurados de análisis competitivo, diseñados para equipos de marketing y ventas. Su objetivo es proporcionar evaluaciones neutrales y basadas en hechos sobre el posicionamiento, movimientos recientes y estrategias de rivales mediante investigación web verificada.

## Datos clave
- **Proyecto**: `competitor-research` (parte del conjunto de habilidades de marketing).
- **Herramientas permitidas**: Read, Grep, Glob, WebSearch, WebFetch, Write.
- **Configuración inicial**: Verifica la existencia de `${CLAUDE_PLUGIN_ROOT}/references/brand-voice.md`; si no existe o está desconfigurado, pausa para responder 4 preguntas de configuración antes de continuar.
- **Proceso de investigación**: Identificar nombre del competidor y ventana temporal (por defecto últimos 90 días); buscar noticias, lanzamientos de producto, cambios de precios y fusiones/adquisiciones.
- **Estructura de salida obligatoria**: Bottom Line, Company Overview, Recent Moves (con fechas y fuentes), Messaging & Positioning Analysis, tabla SWOT, Recommendations y Sources.
- **Reglas de veracidad**: Citar fuente para cada afirmación factual; usar "Not publicly available" en lugar de inventar datos; mantener tono neutral sin lenguaje hiperbólico.

## Etiquetas
#análisis-competitivo #marketing-strategy #investigación-web

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\marketing-skill-claude-marketing-skill-builder-uzp891\skills\competitor-research\SKILL.md`
