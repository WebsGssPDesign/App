---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/touchdesigner-mcp/references/glsl.md"
tags: [hecho]
---
# glsl.md

## Resumen
Este documento es una guía de referencia para escribir shaders GLSL dentro del entorno TouchDesigner, detallando cómo acceder a uniformes nativos, utilizar funciones auxiliares y estructurar el código para nodos TOP (píxeles) y MAT (vértices). Sirve como manual técnico para desarrollar efectos visuales personalizados, incluyendo ejemplos de ruido, transformaciones de matriz y matrices de dithering.

## Datos clave
- **Uniformes**: `uTime` para tiempo, `uTDOutputInfo.res.zw` para resolución de salida y `sTD2DInputs[0]` para texturas de entrada (únicamente en TOP).
- **Funciones nativas**: `TDPerlinNoise`, `TDHSVToRGB`, `TDTranslate`, `TDRotateX/Y/Z`, `TDOutputSwizzle`.
- **Estructura TOP**: Uso de DATs acoplados (`glsl1_pixel`, `glsl1_compute`) y actualización vía Python con `cook(force=True)`.
- **Estructura MAT**: Diferencia en parámetros (`vdat`/`pdat` vs `vertexdat`/`pixeldat`) y uso de funciones como `TDPos()` y `TDWorldToProj()`.
- **Dithering**: Implementación de una matriz de Bayer 8x8 para estética retro.

## Etiquetas
#TouchDesigner #GLSL #Shaders #VFX

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\touchdesigner-mcp\references\glsl.md`
