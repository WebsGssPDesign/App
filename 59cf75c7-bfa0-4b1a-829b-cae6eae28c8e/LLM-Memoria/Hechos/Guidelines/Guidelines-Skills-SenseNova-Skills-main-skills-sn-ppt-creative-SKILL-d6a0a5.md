---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-ppt-creative/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía define el flujo de trabajo para la habilidad "sn-ppt-creative", diseñada para transformar un guion existente en una presentación visual basada en imágenes (formato 16:9) y empaquetarla como PPTX. Su función es traducir contenido textual a metáforas visuales sin alterar el mensaje central, respetando estrictamente la estructura del outline original y evitando realizar nuevas investigaciones o cambios de contenido.

## Datos clave
- **Proyecto**: SenseNova-Skills (Tier 1).
- **Entradas obligatorias**: `task_pack.json`, `info_pack.json` y `outline.md` dentro de `<DECK_DIR>`.
- **Jerarquía de generación**: Priorizar herramientas nativas del agente; usar `image_generate.py` solo si falla la herramienta nativa. Prohibido usar `model_client.py` o APIs externas adicionales.
- **Flujo de trabajo**:
  1. Generar `<DECK_DIR>/style_spec.md`.
  2. Crear prompts individuales por página y sanitizarlos con `sanitize_prompt.py`.
  3. Generar imágenes PNG (2752x1536) una por una.
  4. Empaquetar en PPTX usando `build_pptx.py`.
- **Recuperación**: El script `resume_scan.py` gestiona la reanudación basándose en qué archivos existen (prompts, PNGs o PPTX).
- **Restricciones**: No modificar, añadir ni eliminar páginas del outline; no inventar datos de investigación.

## Etiquetas
#presentaciones #generación-de-imágenes #automatización #sense-nova

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-ppt-creative\SKILL.md`
