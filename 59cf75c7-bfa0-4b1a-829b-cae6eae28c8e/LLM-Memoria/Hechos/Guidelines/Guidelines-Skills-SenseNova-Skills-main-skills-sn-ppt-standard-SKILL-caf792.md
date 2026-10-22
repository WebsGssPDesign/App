---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-ppt-standard/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento actúa como una hoja de ruta técnica para el Skill `sn-ppt-standard`, definiendo estrictamente los roles del Orchestrator, Slide y Review, así como las reglas de diseño visual y generación de activos. Su función es orquestar la creación de presentaciones (HTML/PPTX) basándose exclusivamente en inputs preexistentes (`outline.md`, `task_pack.json`), garantizando que los productos finales sean técnicamente válidos y visualmente coherentes sin inventar contenido ni alterar el orden establecido.

## Datos clave
- **Roles**: Orchestrator (planificación/aceptación), Slide (creación de páginas), Review (diagnóstico y reparación).
- **Entradas obligatorias**: `DECK_DIR`, `task_pack.json`, `info_pack.json` y `outline.md`.
- **Herramientas Hermes**: Mapeo específico para reemplazar comandos Box-Agent (`bash` → `terminal`, `inspect_images` → `vision_analyze`).
- **Restricciones de diseño**: Máximo 3 familias tipográficas; prohibido usar fuentes monoespaciadas para texto chino; priorizar imágenes reales o generadas sobre SVGs para visuales principales.
- **Entregables críticos**: `present.html` (siempre obligatorio) y `<DECK_ID>.pptx` (solo si `static_postprocess` incluye PPTX).
- **Flujo de trabajo**: Fase 0 (validación de inputs) → Fase 1 (Grounding gate para verificar reportes de investigación antes de proceder).

## Etiquetas
#sn-ppt-standard #guías-de-diseño #automatización-de-presentaciones #orquestación

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-ppt-standard\SKILL.md`
