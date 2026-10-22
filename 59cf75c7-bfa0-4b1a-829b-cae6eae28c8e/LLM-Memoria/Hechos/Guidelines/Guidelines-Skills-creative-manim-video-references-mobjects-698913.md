---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/manim-video/references/mobjects.md"
tags: [hecho]
---
# mobjects.md

## Resumen
Este documento es una referencia técnica para la librería Manim, detallando cómo crear y manipular objetos visuales (Mobjects) en videos educativos. Explica la sintaxis para generar texto, formas geométricas, gráficos matemáticos e imágenes, además de reglas clave para agrupar elementos y animarlos correctamente.

## Datos clave
- **Concepto central**: Todo elemento visible es un Mobject con posición, color y opacidad.
- **Regla crítica**: Usar `Group` si hay texto (`Text`) mezclado; usar `VGroup` solo para formas vectoriales (VMobjects).
- **Tipos de objetos**: Text, MathTex, Circle, Polygon, Arc, Sector, Annulus, SVGMobject, ImageMobject.
- **Comandos de estilo**: `.set_color()`, `.set_fill()`, `.set_stroke()`, `.move_to()`, `.to_edge()`.
- **Matrices**: `IntegerMatrix`, `DecimalMatrix` y `MobjectMatrix` para álgebra lineal.
- **Constantes**: Direcciones (`UP`, `LEFT`) y colores predefinidos (ej. `RED`, `BLUE`).
- **Animación**: Las imágenes raster no usan `.animate`; usar `FadeIn` o `shift`.

## Etiquetas
#manim #animación #python #documentación

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\manim-video\references\mobjects.md`
