---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/touchdesigner-mcp/references/projection-mapping.md"
tags: [hecho]
---
# projection-mapping.md

## Resumen
Este documento es una guía técnica para configurar proyecciones mapeadas en TouchDesigner, cubriendo desde la salida básica de ventanas hasta técnicas avanzadas como el warping de superficies curvas y el mezclado de bordes entre múltiples proyectores. Su objetivo principal es estandarizar los flujos de trabajo para instalaciones y eventos, asegurando una calibración precisa y una imagen coherente en pantallas físicas.

## Datos clave
- **Proyecto**: Configuración de mapeo de proyección (Projection Mapping) para instalaciones.
- **Tecnologías**: TouchDesigner 2025.32, shaders GLSL personalizados, GPU Mosaic/Eyefinity.
- **Decisiones**: Uso de `windowCOMP` con pulsado (`winopen.pulse()`) obligatorio; preferencia por mallas subdivididas para superficies curvas sobre el `cornerPinTOP`.
- **Rutas y comandos**: Creación de nodos `geometryCOMP`, `renderTOP` y aplicación de shaders de mezcla (`edge_blend_pixel.glsl`).
- **Pasos importantes**: Calibración iterativa con patrones (cuadrícula, cruz) y ajuste manual de vértices; uso de uniformes GLSL para desplazamiento por vértice.

## Etiquetas
#touchdesigner #projectionmapping #glshading #calibration #multiscreen

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\touchdesigner-mcp\references\projection-mapping.md`
