---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/manim-video/references/animations.md"
tags: [hecho]
---
# animations.md

## Resumen
Este documento es una guía de referencia para crear animaciones en Manim, explicando cómo definir objetos de animación que controlan estados visuales intermedios. Sirve como manual técnico para implementar movimientos, transformaciones y efectos de entrada/salida mediante la sintaxis `self.play()` y `.animate`.

## Datos clave
- **Concepto central**: Las animaciones son objetos pasados a `self.play()`, no funciones; siempre especificar `run_time` explícitamente.
- **Creación y eliminación**: Uso de `Create`, `Write`, `FadeIn` para entrada y `FadeOut`, `Uncreate`, `ShrinkToCenter` para salida.
- **Transformaciones críticas**: Diferencia entre `Transform` (modifica el objeto original) y `ReplacementTransform` (elimina el anterior y pone el nuevo). Se recomienda `ReplacementTransform` si se necesita manipular el nuevo objeto después.
- **Sintaxis `.animate`**: Permite animar propiedades dinámicas como color o posición (`circle.animate.set_color(RED)`).
- **Movimiento complejo**: Uso de `MoveAlongPath` con curvas arbitrarias y `Rotate` para rotaciones específicas.
- **Funciones de ritmo**: Control del flujo temporal mediante parámetros como `rate_func=smooth`, `linear` o `rush_into`.
- **Composición avanzada**: Agrupamiento simultáneo (`AnimationGroup`) o secuencial (`Succession`) con retrasos (`lag_ratio`).
- **Objetos reactivos**: Uso de `always_redraw()` para reconstruir mobjects en cada frame (ej. bridas que siguen a otros objetos) y `add_updater` para cambios más ligeros.
- **Rastreo de trayectorias**: Implementación de `TracedPath` para dibujar la ruta recorrida por un punto.

## Etiquetas
#manim #animaciones #documentación #python #visualización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\manim-video\references\animations.md`
