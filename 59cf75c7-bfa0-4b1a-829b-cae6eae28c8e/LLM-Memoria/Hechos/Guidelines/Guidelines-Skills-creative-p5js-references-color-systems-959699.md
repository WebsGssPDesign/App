---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/p5js/references/color-systems.md"
tags: [hecho]
---
# color-systems.md

## Resumen
Esta guía técnica documenta el sistema de colores en p5.js, recomendando el modo HSB para arte generativo por su facilidad en la manipulación matricial. Proporciona funciones y algoritmos para generar paletas procedimentales, interpolar gradientes complejos y aplicar modos de mezcla avanzados.

## Datos clave
- **Modos de color**: `colorMode(HSB)` es preferido; HSL para tintes/sombras; RGB por defecto.
- **Manipulación**: Uso de objetos `color()` con extractores (`hue`, `saturation`) y setters (`setAlpha`).
- **Interpolación**: Funciones `lerpColor` (dos colores) y `paletteLerp` (múltiples colores en p5.js 1.11+).
- **Gradientes**: Implementaciones manuales para lineales, radiales y basados en ruido (`noiseGradient`).
- **Generación de paletas**: Funciones para complementarias, análogas, triádicas, split-complementary, tetradic y monocromáticas.
- **Biblioteca curada**: Colección de constantes hexadecimales organizadas por temperatura (Warm, Cool), neutralidad y tonos tierra.

## Etiquetas
#p5js #colorSystems #generativeArt #palettes

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\p5js\references\color-systems.md`
