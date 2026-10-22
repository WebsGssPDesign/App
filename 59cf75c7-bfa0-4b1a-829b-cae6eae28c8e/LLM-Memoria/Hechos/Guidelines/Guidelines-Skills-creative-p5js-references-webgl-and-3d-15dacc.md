---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/p5js/references/webgl-and-3d.md"
tags: [hecho]
---
# webgl-and-3d.md

## Resumen
Esta guía técnica documenta la configuración y funcionalidades de gráficos 3D en p5.js utilizando WebGL. Explica cómo establecer el sistema de coordenadas, gestionar cámaras, aplicar iluminación avanzada y crear materiales personalizados para visualizaciones interactivas.

## Datos clave
- **Configuración inicial**: Uso de `createCanvas(..., WEBGL)` con origen centrado; conversión a P2D mediante `translate(-width/2, -height/2)`.
- **Primitivas y transformaciones**: Funciones como `box`, `sphere` y `cylinder`; uso de `push()`/`pop()` para gestionar pilas de transformación (traslación, rotación, escala).
- **Cámaras**: Control por órbita (`orbitControl`) o instanciación con `createCamera` para métodos granulares como `setPosition`, `lookAt`, `pan`, `tilt` e interpolación `slerp`.
- **Iluminación y materiales**: Tipos de luz (ambiental, direccional, puntual, spot); propiedades de material (`emissiveMaterial`, `specularMaterial`, `shininess`) y mapeo de texturas.
- **Geometría personalizada**: Creación eficiente mediante `buildGeometry` o `beginGeometry`/`endGeometry`; construcción manual con `p5.Geometry`.
- **Shaders GLSL**: Implementación de shaders personalizados (vertex y fragment) para efectos visuales avanzados usando matrices de proyección y modelos.

## Etiquetas
#p5js #WebGL #Gráficos3D #DesarrolloCreative

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\p5js\references\webgl-and-3d.md`
