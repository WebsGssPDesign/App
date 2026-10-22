---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/p5js/references/visual-effects.md"
tags: [hecho]
---
# visual-effects.md

## Resumen
Este documento técnico detalla técnicas avanzadas de efectos visuales generativos utilizando la librería p5.js. Sirve como referencia para implementar ruido (Perlin, fBM), campos de flujo y sistemas de partículas con física realista, permitiendo crear texturas orgánicas y simulaciones complejas.

## Datos clave
- **Técnicas principales**: Ruido Perlin (1D/2D/3D), Movimiento Browniano Fractal (fBM) para texturas naturales, y deformación de dominio (Domain Warping).
- **Cálculo de Curl Noise**: Implementado mediante diferencias finitas parciales para generar campos vectoriales divergencia-libre ideales para fluidos.
- **Clase FlowField**: Genera una cuadrícula de vectores basada en ruido temporal que dirige el movimiento de partículas.
- **Sistemas de partículas**: Incluye clases `Particle` con física básica, `Attractor` para fuerzas magnéticas y lógica de enjambre (Boids) con alineación, cohesión y separación.
- **Parámetros críticos**: El factor de escala del ruido (`0.005`, `0.01`) define el nivel de detalle; la lacunaridad y ganancia controlan las octavas en fBM.

## Etiquetas
#p5js #generativeArt #visualEffects #particles #noise

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\p5js\references\visual-effects.md`
