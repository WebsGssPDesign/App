---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/touchdesigner-mcp/references/3d-scene.md"
tags: [hecho]
---
# 3d-scene.md

## Resumen
Este documento sirve como guía técnica para construir escenas 3D en TouchDesigner, detallando la arquitectura de renderizado y cómo configurar materiales PBR, iluminación y sombras. Proporciona ejemplos de código Python para crear nodos esenciales (geometría, cámara, luces) y explica estrategias optimizadas para el rendimiento gráfico.

## Datos clave
- **Arquitectura**: La secuencia es Geometry COMP → Material → Light/Camera COMPs → Render TOP → post-FX → windowCOMP. El `Render TOP` es central; combina geometría, cámara y luces (explícitas o automáticas).
- **Iluminación**: Se define un setup de tres puntos (Key, Fill, Rim) usando tipos `point`, `area` y `spot`. Para sombras, se recomienda `softshadow` con resolución inicial de 1024 para equilibrar calidad y costo GPU.
- **IBL/Materiales**: Los materiales PBR requieren una luz ambiental (`envlightCOMP`) conectada a un cubemap (vía `cubeTOP` o conversión de HDR). Los mapas de textura siguen la convención glTF (canal G para roughness, B para metallic).
- **Optimización**: Limitar luces que proyectan sombras a 1-2 en tiempo real; ajustar rangos `near/far` de las luces solo al contenido de la escena.

## Etiquetas
#TouchDesigner #Render3D #Iluminación #PBR #Optimización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\touchdesigner-mcp\references\3d-scene.md`
