---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/p5js/references/animation.md"
tags: [hecho]
---
# animation.md

## Resumen
Esta guía técnica explica cómo crear animaciones fluidas y naturales en p5.js utilizando bucles de dibujo, funciones de suavizado (easing) y física de resortes. Sirve como referencia para implementar movimientos coherentes independientemente del rendimiento del navegador y gestionar secuencias complejas mediante máquinas de estados o líneas de tiempo.

## Datos clave
- **Bucle principal**: `draw()` se ejecuta ~60 veces/seg; usar `deltaTime` para movimiento independiente del framerate.
- **Tiempo normalizado**: Calcular progreso entre 0 y 1 usando `millis()`, útil para bucles o movimientos de ida y vuelta (ping-pong).
- **Funciones Easing**: Implementaciones manuales para curvas como `easeInQuad`, `easeOutCubic` y `smoothstep`; aplicar mediante la función auxiliar `easedValue`.
- **Física de resortes**: Clase `Spring` con parámetros de rigidez (`stiffness`) y amortiguación (`damping`) para movimientos orgánicos; versión 2D disponible.
- **Gestión de estados**: Uso de máquinas de estado (IDLE, ENTER, ACTIVE) para controlar fases de animación multi-etapa.
- **Secuenciación**: Clase `Timeline` para programar eventos temporales con duración específica y funciones asociadas.

## Etiquetas
#p5js #animación #javascript #física #desarrollo

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\p5js\references\animation.md`
