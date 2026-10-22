---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/manim-video/references/camera-and-3d.md"
tags: [hecho]
---
# camera-and-3d.md

## Resumen
Este documento es una guía técnica para controlar cámaras y crear escenas tridimensionales en Manim. Sirve como referencia rápida para implementar efectos visuales avanzados, desde zoom dinámico hasta transformaciones lineales complejas, ayudando a los creadores de contenido matemático a elegir la herramienta adecuada según el tipo de escena.

## Datos clave
- **Clases principales**: `MovingCameraScene` (control 2D), `ThreeDScene` (escenas 3D), `ZoomedScene` (zooms insertados) y `LinearTransformationScene` (álgebra lineal).
- **Operaciones de cámara**: Ajuste de ancho (`set(width)`), movimiento (`move_to`), orientación en 3D (`set_camera_orientation`, `move_camera`) y rotación ambiental.
- **Objetos 3D**: Uso de `Sphere`, `Cube`, `Arrow3D` y curvas paramétricas como `ParametricFunction`.
- **Lógica de decisión**: Usar 3D para superficies o geometría espacial; evitarlo en gráficos planos o textos densos.
- **Ejemplo clave**: La clase `LinearTransformationScene` reproduce el estilo visual característico de las series sobre álgebra lineal deformando grillas y vectores base.

## Etiquetas
#manim #animación3d #documentación #matemáticas

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\manim-video\references\camera-and-3d.md`
