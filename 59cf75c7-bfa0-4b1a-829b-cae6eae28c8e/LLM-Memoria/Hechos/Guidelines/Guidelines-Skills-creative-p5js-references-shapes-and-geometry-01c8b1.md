---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/p5js/references/shapes-and-geometry.md"
tags: [hecho]
---
# shapes-and-geometry.md

## Resumen
Este documento es una guía de referencia para crear formas geométricas y cálculos espaciales en p5.js. Sirve como manual técnico que detalla primitivas 2D, modos de dibujo, curvas paramétricas (Bézier, Catmull-Rom) y la implementación de campos de distancia firmados (SDF) para efectos visuales avanzados.

## Datos clave
- **Primitivas**: `point`, `line`, `rect` (con modos CORNER/CENTER), `ellipse`, `triangle`, `quad`.
- **Dibujo personalizado**: Uso de `beginShape()` con modos como `CLOSE`, `POINTS`, `TRIANGLE_FAN` y manejo de contornos (`beginContour`) para agujeros.
- **Curvas**: Funciones `bezier()`, `quadraticVertex()`, `curveVertex()` y cálculo de tangentes/interpolación.
- **Vectores**: Clase `p5.Vector` con métodos aritméticos (add, sub), normalización (`normalize`), magnitud y productos cruzados/puntos.
- **SDFs**: Funciones para calcular distancia a formas (círculos, cajas) y operaciones booleanas suaves (`opSmoothUnion`) para efectos de brillo.
- **Patrones**: Algoritmos para generar polígonos regulares y estrellas usando trigonometría básica.

## Etiquetas
#p5js #geometría #vectores #SDF #programaciónCreativa

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\p5js\references\shapes-and-geometry.md`
