---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/manim-video/references/equations.md"
tags: [hecho]
---
# equations.md

## Resumen
Este documento es una guía de referencia para crear y animar ecuaciones matemáticas complejas en Manim utilizando LaTeX. Explica cómo estructurar fórmulas, aplicar transformaciones paso a paso y aislar subexpresiones para lograr animaciones precisas en videos educativos o científicos.

## Datos clave
- **Tecnología**: Manim (Python), LaTeX (`MathTex`).
- **Regla crítica**: Siempre usar cadenas crudas (`r""`) para evitar errores de escape.
- **Aislamiento**: Usar `substrings_to_isolate` en ecuaciones densas para permitir coloreo y transformación individual de términos.
- **Transformación**: Emplear `TransformMatchingTex` con parámetros `key_map`, `matched_keys` y `path_arc` para alinear correctamente partes ambiguas entre ecuaciones fuente y destino.
- **Entornos**: Soporte nativo para matrices (`bmatrix`, `pmatrix`) y funciones por casos (`cases`).
- **Coloreo**: Métodos como `set_color_by_tex` para asignar colores a substrings específicos sin dividir manualmente el objeto.

## Etiquetas
#Manim #LaTeX #AnimaciónMatemática #DocumentaciónTécnica

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\manim-video\references\equations.md`
