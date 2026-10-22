---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/pretext/references/patterns.md"
tags: [hecho]
---
# patterns.md

## Resumen
Este documento ofrece fragmentos de código reutilizables para crear demostraciones visuales con la librería Pretext, permitiendo que el texto fluya dinámicamente alrededor de obstáculos geométricos o formas ASCII en movimiento. Sirve como referencia técnica para implementar efectos interactivos como juegos de palabras, tipografía explosiva y máscaras de desplazamiento sin necesidad de recortar el contenido textual.

## Datos clave
- **Tecnología**: `@chenglou/pretext` (vía ESM).
- **Patrones principales**: Flujo alrededor de obstáculos variables, texto como geometría para juegos (cajas AABB), explosión tipográfica con partículas y máscaras ASCII móviles.
- **Funciones críticas**: `prepareWithSegments`, `layoutNextLineRange`, `materializeLineRange`, `walkLineRanges`.
- **Lógica de colisión**: Uso de coordenadas por gráema para física y animación de partículas.
- **Optimización**: Medición precisa de celdas rasterizadas en lugar de usar contenedores de límites grandes para evitar espacios vacíos innecesarios.

## Etiquetas
#pretext #tipografía #javascript #canvas #demos

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\pretext\references\patterns.md`
