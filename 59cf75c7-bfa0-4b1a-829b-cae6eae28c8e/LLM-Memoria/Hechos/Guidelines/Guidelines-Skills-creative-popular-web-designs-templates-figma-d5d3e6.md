---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/popular-web-designs/templates/figma.md"
tags: [hecho]
---
# figma.md

## Resumen
Este documento detalla el sistema de diseño del sitio web de Figma para replicar su interfaz minimalista y sofisticada en entornos autocontenidos. Sirve como guía técnica para implementar tipografía variable, una paleta estricta de blanco y negro, y geometrías orgánicas que imitan la experiencia del editor de productos.

## Datos clave
- **Tipografía**: Sustitución de `figmaSans` por `Inter` (con pesos específicos: 320, 330, 340, 450, 480, 540) y `JetBrains Mono`. Uso obligatorio del rasgo OpenType `"kern"` y espaciado negativo en el cuerpo (-0.14px a -0.26px).
- **Paleta de colores**: Interfaz monocromática (`#000000` y `#ffffff`) con efectos de vidrio (`rgba(0, 0, 0, 0.08)` y `rgba(255, 255, 255, 0.16)`. Los colores vibrantes se reservan exclusivamente para el contenido del producto (gradientes heroicos).
- **Geometría**: Botones con radio de 50px (píldora) o 50% (círculo perfecto). Indicadores de foco discontinuos (`dashed 2px`).
- **Flujo de trabajo**: Generación de HTML vía `write_file`, despliegue mediante `generative-widgets` y verificación visual con `browser_vision`.

## Etiquetas
#design-system #figma #frontend-dev #typography

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\popular-web-designs\templates\figma.md`
