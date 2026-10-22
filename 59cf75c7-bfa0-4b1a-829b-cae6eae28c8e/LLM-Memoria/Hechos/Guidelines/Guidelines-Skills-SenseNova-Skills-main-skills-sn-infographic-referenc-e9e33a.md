---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-infographic/references/layout-style-selection.md"
tags: [hecho]
---
# layout-style-selection.md

## Resumen
Este documento establece las reglas para seleccionar automáticamente diseños de diagramas y estilos visuales basándose en el tipo de datos y el tono del prompt del usuario. El sistema utiliza una lógica de puntuación ponderada que asigna un candidato principal (puntuación 1.0) y alternativas (puntuación 0.7) sin necesidad de comparar el contenido interno de los archivos de definición, ya que la elección es aleatoria entre las opciones válidas.

## Datos clave
- **Proyecto**: SenseNova-Skills (agente trabajador).
- **Tecnologías/Conceptos**: Lógica de puntuación ponderada (`match_score`), selección aleatoria, manipulación de nombres.
- **Decisiones principales**: Nunca abrir archivos de definición para elegir; operar solo con nombres de layouts y styles.
- **Rutas relevantes**: `references/layouts/*.md`, `references/styles/*.md`.
- **Pasos importantes**:
  1. Analizar `user_prompt` para determinar `data_type` y mapear a candidatos de layout (ej: timeline -> `linear-progression`).
  2. Analizar tono/dominio para mapear a candidatos de style (ej: Tech -> `technical-schematic`).
  3. Realizar un sorteo ponderado final; solo leer los archivos seleccionados en el paso 2.3 del SKILL.md.

## Etiquetas
#diseño #automatización #guias #sensenova

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-infographic\references\layout-style-selection.md`
