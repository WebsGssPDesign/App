---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-image-imitate/README_CN.md"
tags: [hecho]
---
# README_CN.md

## Resumen
Este documento describe la habilidad `sn-image-imitate`, diseñada para generar imágenes que imitan el estilo y la composición de una referencia mientras cambian su contenido semántico. El sistema automatiza un flujo de trabajo que incluye análisis visual, reescritura de prompts mediante LLMs y generación iterativa con revisión automática de la consistencia del diseño.

## Datos clave
- **Proyecto**: `sn-image-imitate` (Tier 1), dependiente de `sn-image-base`.
- **Tecnologías**: Python 3.9+, VLM para análisis y revisión, LLM para reescritura de descripciones.
- **Variables críticas**: `SN_BASE_URL`, `SN_API_KEY`, `SN_TEXT_*`, `SN_VISION_*`.
- **Rutas de instalación**: Copia a `~/.openclaw/skills/` o `~/.hermes/skills/openclaw-imports/`.
- **Comandos de uso**: `/skill sn-image-imitate "参考图：ruta, 目标内容：descripción"`.
- **Parámetros principales**: `reference_image`, `target_content`, `max_attempts`, `layout_threshold`.

## Etiquetas
#IA #GeneraciónDeImágenes #SenseNova #OpenClaw

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-image-imitate\README_CN.md`
