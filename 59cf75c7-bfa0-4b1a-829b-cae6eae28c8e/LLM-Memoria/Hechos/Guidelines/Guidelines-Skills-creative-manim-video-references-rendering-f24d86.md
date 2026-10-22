---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/manim-video/references/rendering.md"
tags: [hecho]
---
# rendering.md

## Resumen
Esta guía detalla el flujo de trabajo completo para renderizar videos educativos con Manim, desde la configuración inicial hasta la exportación final. Establece estándares de calidad para diferentes etapas (bocetos, previsualizaciones y producción) y ofrece métodos tanto manuales como automatizados mediante plugins para integrar voz en off y música.

## Datos clave
- **Presets de calidad**: `-ql` (854x480p, 15fps) para iteración rápida; `-qm` (720p, 30fps) para revisión de texto; `-qh` (1080p, 60fps) para producción final.
- **Comandos esenciales**: `manim -ql script.py SceneName`, `ffmpeg` para unir clips (`concat.txt`) y mezclar audio.
- **Configuración**: Uso de `manim.cfg` para definir rutas y colores por defecto sin repetir flags en el CLI.
- **Plugins recomendados**: `manim-voiceover` con servicios como ElevenLabs o Google TTS para sincronización automática de animaciones y generación de subtítulos.
- **Secciones**: Uso de `self.next_section()` y renderizado parcial (`--save_sections`) para optimizar la edición de videos largos.

## Etiquetas
#manim #rendering #video-production #ffmpeg #automation

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\manim-video\references\rendering.md`
