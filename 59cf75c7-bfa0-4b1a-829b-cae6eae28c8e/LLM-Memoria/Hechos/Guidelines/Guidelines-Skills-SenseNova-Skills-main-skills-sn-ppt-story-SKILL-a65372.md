---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-ppt-story/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía define la habilidad `sn-ppt-story` como un paso obligatorio en el flujo de trabajo de presentaciones de SenseNova, encargado de sintetizar consultas, materiales del usuario y reportes de investigación en un único archivo `outline.md`. Su función es estructurar una narrativa coherente para las etapas finales (standard/dazzle/creative), asegurando que la lógica argumental se base estrictamente en evidencias verificadas sin generar contenido visual ni realizar nuevas búsquedas.

## Datos clave
- **Proyecto**: SenseNova-Skills (Tier 1, categoría scene).
- **Entrada**: Directorio `DECK_DIR` con archivos `task_pack.json`, `info_pack.json` y reportes de investigación previos (`sn-deep-research`).
- **Salida**: Archivo único `<DECK_DIR>/outline.md` que define título, flujo narrativo y contenido por página.
- **Proceso crítico**: Lectura completa de fuentes, definición del "Story" global antes de la paginación, y tres rondas de autocrítica (evidencia, lógica, demostración).
- **Restricciones**: No ejecutar búsquedas web ni generar PPTX/HTML; si faltan datos, detenerse y devolver control a `sn-ppt-entry`.
- **Formato**: Markdown estricto con secciones "Esta página debe explicar" y "Relaciones previas/siguientes".

## Etiquetas
#SenseNova #Storytelling #PPTOutline #GuíaTécnica

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-ppt-story\SKILL.md`
