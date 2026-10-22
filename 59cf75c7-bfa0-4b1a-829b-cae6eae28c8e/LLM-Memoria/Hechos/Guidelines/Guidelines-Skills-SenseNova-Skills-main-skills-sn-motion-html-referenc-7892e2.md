---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-motion-html/references/schemas.md"
tags: [hecho]
---
# schemas.md

## Resumen
Este documento define los esquemas JSON para estructurar narrativas visuales y generar videos mediante IA, especificando cómo organizar capítulos, prompts de generación y conectores entre escenas. Sirve como guía técnica para asegurar la consistencia en el estilo artístico, la duración y la integración de recursos multimedia dentro del proyecto SenseNova.

## Datos clave
- **Proyecto**: SenseNova (Skills/sn-motion-html).
- **Archivos principales**: `content/story.json` (estructura narrativa) y `prompts/video-manifest.json` (instrucciones de generación).
- **Modelo de IA**: `doubao-seedance-2-5-260628`.
- **Modos de condicionamiento**: `reference_images` (para composición multimodal) o `first_last` (para anclaje exacto de bordes usando caché en `assets/video/frames`).
- **Métricas de tiempo**: El atributo `span` se mide en alturas de viewport, no en segundos.
- **Conectores**: Deben existir `chapters.length - 1` para tomas continuas; usar `null` solo si hay cortes visibles aceptados por el usuario.

## Etiquetas
#SenseNova #GeneraciónDeVideo #JSONSchema #IA

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-motion-html\references\schemas.md`
