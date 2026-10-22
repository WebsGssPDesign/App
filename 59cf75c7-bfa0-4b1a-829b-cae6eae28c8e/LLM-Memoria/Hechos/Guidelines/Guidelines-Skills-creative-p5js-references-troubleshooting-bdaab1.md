---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/p5js/references/troubleshooting.md"
tags: [hecho]
---
# troubleshooting.md

## Resumen
Esta guía técnica ofrece estrategias para optimizar el rendimiento de sketches en p5.js, enfocándose en la eliminación de sobrecargas innecesarias y la mejora de algoritmos costosos. Su objetivo es permitir que las aplicaciones creativas mantengan tasas de cuadros estables (60fps o 30fps) incluso con operaciones complejas como renderizado por píxel o sistemas de partículas masivos.

## Datos clave
- **Desactivar FES**: Usar `p5.disableFriendlyErrors = true` o el archivo `p5.min.js` para evitar un rendimiento diez veces menor.
- **Densidad de píxeles**: Forzar `pixelDensity(1)` en la función `setup()` para reducir la carga computacional en pantallas Retina/HiDPI.
- **Matemáticas nativas**: Reemplazar funciones de p5 (`sin`, `cos`) por `Math.*` y evitar `sqrt()` usando distancias al cuadrado (`magSq`).
- **Optimización de renderizado**: Sustituir bucles de `ellipse()` por `beginShape/endShape` o manipulación directa de píxeles (`loadPixels`).
- **Estructuras de datos**: Implementar *Spatial Hashing* para consultas de vecinos y *Object Pooling* para evitar fugas de memoria.
- **Presupuesto de píxeles**: Renderizar a menor resolución (ej. paso=3) y rellenar bloques si las operaciones por píxel superan los 10ms en 1080p.

## Etiquetas
#p5js #optimización #rendimiento #javascript #creatividad

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\p5js\references\troubleshooting.md`
