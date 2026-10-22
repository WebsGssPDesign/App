---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/ascii-video/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define una guía técnica y creativa para producir videos de arte ASCII que convierten audio o video en animaciones de texto coloreado. Su objetivo es establecer un estándar cinematográfico donde la estética visual y el concepto creativo priman sobre la implementación literal, garantizando resultados impactantes desde el primer renderizado sin necesidad de GPUs.

## Datos clave
- **Proyecto**: Pipeline de producción de ASCII Video (MP4/GIF).
- **Tecnologías**: Python 3.10+, NumPy, SciPy, Pillow, ffmpeg, ElevenLabs API (opcional), OpenCV.
- **Arquitectura**: Script único autocontenido con un pipeline de 6 etapas: INPUT → ANALYZE → SCENE_FN → TONEMAP → SHADE → ENCODE.
- **Modos de operación**: Video-to-ASCII, Audio-reactive, Generative, Hybrid, Lyrics/text y TTS narration.
- **Decisiones creativas**: Uso obligatorio de paletas densas y variadas; prohibido el fondo negro plano; se requiere composición multi-grid por escena.
- **Recursos de referencia**: `references/inputs.md`, `references/effects.md`, `architecture.md`.

## Etiquetas
#ascii-art #video-production #python #creative-coding #ffmpeg

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\ascii-video\SKILL.md`
