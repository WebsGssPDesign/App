---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/ascii-video/references/composition.md"
tags: [hecho]
---
# composition.md

## Resumen
Este documento define el sistema de composición visual del proyecto, detallando tres niveles clave: modos de mezcla a nivel de píxel, composición en cuadrículas múltiples y gestión adaptativa de brillo. Su función principal es proporcionar una guía técnica para combinar capas visuales con precisión, ofreciendo tanto métodos estándar como cálculos basados en luz lineal para resultados físicamente exactos.

## Datos clave
- **Funciones principales**: `blend_canvas()` (mezcla en espacio sRGB) y `blend_canvas_linear()` (mezcla en espacio de luz lineal).
- **Modos de mezcla**: 20 modos definidos, incluyendo aritméticos (`add`, `subtract`), contraste (`overlay`, `softlight`) y efectos de textura (`grain_extract`).
- **Recomendaciones críticas**: Usar `screen` o `add` para entradas oscuras; evitar `multiply` o `colorburn` en esos casos. Para efectos de brillo realistas (glow, bloom), convertir siempre a luz lineal antes de mezclar.
- **Orden de operaciones**: La secuencia importa en combinaciones complejas (ej: `difference(screen(A,B), C)` no es igual a `difference(A, screen(B,C))`).

## Etiquetas
#composición #modosmezcla #procesamientoimágenes #python

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\ascii-video\references\composition.md`
