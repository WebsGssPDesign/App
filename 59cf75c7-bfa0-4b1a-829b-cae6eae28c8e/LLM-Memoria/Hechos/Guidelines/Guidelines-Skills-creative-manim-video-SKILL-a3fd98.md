---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/manim-video/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento establece las directrices para producir videos educativos animados con estilo de 3Blue1Brown utilizando Manim Community Edition. Su objetivo es transformar conceptos matemáticos y algorítmicos complejos en explicaciones visuales claras, asegurando que cada frame tenga un propósito pedagógico y una estética cohesiva sin necesidad de revisiones posteriores.

## Datos clave
- **Proyecto**: Pipeline de producción de videos educativos (Manim CE).
- **Tecnologías**: Python 3.10+, Manim Community Edition v0.20+, LaTeX, ffmpeg.
- **Decisiones creativas**: Priorizar geometría sobre álgebra; usar capas de opacidad para dirigir la atención; incluir tiempos de espera (`self.wait()`) tras cada animación clave.
- **Rutas y comandos**: `scripts/setup.sh` para dependencias; renderizado con `manim -ql script.py Scene1 ...` (draft) o `-qh` (producción); ensamblaje final con ffmpeg.
- **Estructura de archivos**: Un único archivo `script.py` por proyecto, acompañado de un `plan.md` y `concat.txt`.
- **Paletas de color**: Definidas para estilos como "Classic 3B1B", "Warm academic" y "Neon tech".

## Etiquetas
#manim #animación #educación #python #visualización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\manim-video\SKILL.md`
