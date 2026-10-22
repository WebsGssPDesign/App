---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/manim-video/references/decorations.md"
tags: [hecho]
---
# decorations.md

## Resumen
Este documento detalla técnicas en Manim para crear decoraciones visuales que polen animaciones matemáticas y científicas, transformando representaciones técnicas correctas en explicaciones claras y atractivas. Sirve como guía práctica para implementar elementos gráficos como recuadros, llaves, flechas y resaltados de color que guían la atención del espectador sobre conceptos clave.

## Datos clave
- **Proyecto**: Manim (animación matemática).
- **Tecnologías**: Python, `MathTex`, `Text`, `VMobject`.
- **Decisiones**: Se prioriza el uso de `set_stroke(background=True)` para etiquetas sobre gráficos y se evita dejar decoraciones en pantalla indefinidamente.
- **Rutas/Comandos**: `SurroundingRectangle`, `Brace`, `Angle`, `DashedLine`, `LabeledArrow`.
- **Pasos importantes**: Secuencia de animación (Aparecer -> Esperar -> Desaparecer) y métodos para colorear texto (`t2c`, `set_color_by_tex`, acceso por índice).

## Etiquetas
#manim #visualización #animación #documentación

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\manim-video\references\decorations.md`
