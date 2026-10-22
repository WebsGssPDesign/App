---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/ascii-video/README.md"
tags: [hecho]
---
# README.md

## Resumen
Este documento describe una habilidad técnica para crear videos en ASCII coloreados que convierten audio, video o matemáticas en secuencias MP4/GIF sin usar GPU. Sirve como guía completa para agentes de código que construyen renderizadores Python desde cero, gestionando todo el pipeline desde la análisis de entrada hasta la codificación final con ffmpeg.

## Datos clave
- **Proyecto**: Hermes Agent (Hermes Agent).
- **Tecnologías**: Python, ffmpeg, OKLAB/OKLCH color system, FFT para audio.
- **Pipeline**: 6 etapas: INPUT --> ANALYZE --> SCENE_FN --> TONEMAP --> SHADE --> ENCODE.
- **Modos de operación**: Video-to-ASCII, Audio-reactive, Generative, Hybrid, Lyrics/text, TTS narration.
- **Sistema de rejilla (Grid)**: 6 tamaños (xs a xxl) para capas de profundidad; uso típico de 2-3 densidades superpuestas.
- **Paletas**: 24 familias de caracteres validadas (Braille, Katakana, Runes, etc.) y 10 paletas RGB discretas.
- **Generadores de valor**: 21 campos (trigonometría, ruido, espirales) para mapear brillo en la rejilla.
- **Comandos clave**: Uso de `ShaderChain` con 38 shaders compuestos y `FeedbackBuffer` para recursión temporal.

## Etiquetas
#ascii-video #python-rendering #creative-coding #hermes-agent #ffmpeg

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\ascii-video\README.md`
