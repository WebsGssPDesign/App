---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-image-imitate/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía define la habilidad `sn-image-imitate` de SenseNova-Skills, diseñada para generar imágenes que imitan el estilo visual de una referencia mientras incorporan nuevo contenido solicitado por el usuario. El sistema opera mediante un flujo de tres etapas: reconocimiento de imagen, optimización del texto y generación final, garantizando consistencia en la composición a través de restricciones estrictas de diseño.

## Datos clave
- **Proyecto**: SenseNova-Skills (Tier 1).
- **Herramientas dependientes**: `sn-image-base` (Tier 0), que incluye `sn-image-recognize`, `sn-text-optimize` y `sn-image-generate`.
- **Arquitectura**: Agente principal (gestiona la interfaz) + Agente trabajador (ejecuta el pipeline de 3 pasos).
- **Parámetros críticos**: `reference_image`, `target_content`, `layout_threshold` (0.75), `max_attempts` (3).
- **Variables de entorno**: Configuración vía `$SN_BASE_URL`, `$SN_API_KEY` y claves específicas para visión/generación (`SN_VISION_API_KEY`, etc.).
- **Limitaciones**: No soporta edición local, inpainting, video ni transferencia de estilo puro sin cambio de contenido.

## Etiquetas
#SenseNova #GeneraciónDeImágenes #IAVisual #GuíaTécnica

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-image-imitate\SKILL.md`
