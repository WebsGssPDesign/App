---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/touchdesigner-mcp/references/layout-compositor.md"
tags: [hecho]
---
# layout-compositor.md

## Resumen
Este documento establece patrones para construir interfaces modulares de múltiples paneles en TouchDesigner, ideales para HUDs y dashboards. Ofrece tres enfoques principales: `layoutTOP` para grids uniformes rápidos, contenedores con `overTOP` para flexibilidad total, y GLSL para divisiones procedurales.

## Datos clave
- **Enfoques**: `layoutTOP` (grid fijo), `containerCOMP` + `overTOP` (paneles de tamaño mixto), GLSL compositor (líneas divisorias dinámicas).
- **Estructura recomendada**: Separar elementos visuales en `baseCOMP` reutilizables dentro de una carpeta `/elements/`, mientras el audio se gestiona en un bus separado (`audio_bus`).
- **Conexiones**: Usar `resolutionTOP` antes de cadenas `overTOP` si los paneles tienen tamaños diferentes.
- **Pasos críticos**: Definir resolución y columnas/filas en `layout.par`; conectar inputs a `inputConnectors`; aplicar efectos post-procesamiento (bloom, CRT) en una carpeta `/postfx/`.

## Etiquetas
#TouchDesigner #LayoutCompositor #HUDDesign #ModularArchitecture

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\touchdesigner-mcp\references\layout-compositor.md`
