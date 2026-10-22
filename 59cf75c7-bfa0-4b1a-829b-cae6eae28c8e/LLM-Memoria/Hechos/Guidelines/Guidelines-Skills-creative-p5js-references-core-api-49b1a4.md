---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/p5js/references/core-api.md"
tags: [hecho]
---
# core-api.md

## Resumen
Este documento detalla la API central de p5.js para configurar el lienzo, gestionar sistemas de coordenadas (P2D vs WebGL), controlar bucles de animación y aplicar transformaciones geométricas. Su propósito es guiar a los desarrolladores en la creación eficiente de gráficos interactivos mediante patrones específicos como buffers fuera de pantalla y composiciones multicapa.

## Datos clave
- **Configuración inicial**: `createCanvas()` soporta modos 2D y WebGL; `pixelDensity(1)` debe llamarse antes del canvas para optimizar rendimiento en exportaciones.
- **Bucle de dibujo**: Estructura estándar con `preload()`, `setup()` (ejecución única) y `draw()` (60fps por defecto). Uso de `noLoop()` para piezas estáticas.
- **Transformaciones**: Funciones acumulativas (`translate`, `rotate`, `scale`) gestionadas con `push()`/`pop()` para aislar cambios; patrón recomendado para rotar alrededor del centro.
- **Buffers fuera de pantalla**: `createGraphics()` permite capas independientes esenciales para efectos de rastro (trails), máscaras y composición multicapa con modos de mezcla (`blendMode`).
- **Layouts**: Patrones iterativos para distribuir elementos en rejillas o radialmente usando trigonometría básica.

## Etiquetas
#p5js #programaciónCreativa #graficosWeb #apiCanvas

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\p5js\references\core-api.md`
