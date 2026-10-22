---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/touchdesigner-mcp/references/postfx.md"
tags: [hecho]
---
# postfx.md

## Resumen
Este documento sirve como referencia técnica para implementar efectos visuales avanzados en TouchDesigner, específicamente brillo (bloom), líneas de barrido CRT, aberración cromática y estelas de retroalimentación. Proporciona ejemplos de código listos para usar tanto con nodos nativos como mediante shaders GLSL personalizados para lograr resultados en tiempo real.

## Datos clave
- **Proyecto**: Referencias de efectos post-procesamiento (Post-FX) para visualización en vivo.
- **Tecnologías**: TouchDesigner, Python, GLSL.
- **Decisiones técnicas**: Uso de `bloomTOP` nativo para rendimiento rápido frente a shaders personalizados para mayor control de color y múltiples pasos.
- **Rutas y nodos**: `glslTOP`, `blurTOP`, `addTOP`, `compositeTOP`, `resolutionTOP`.
- **Comandos/Pasos importantes**:
  - Configurar parámetros como `threshold`, `size` y `strength` en el bloom.
  - Implementar curvatura de barril, líneas de escaneo y vineta dentro del shader CRT.
  - Desplazar canales RGB individualmente para la aberración cromática.
  - Usar `uDecay` (0.92-0.98) para controlar la duración de las estelas en feedback glow.
  - Orden recomendado: bloom → chromatic aberration → CRT → null_out.

## Etiquetas
#TouchDesigner #GLSL #PostFX #VisualizaciónEnVivo

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\touchdesigner-mcp\references\postfx.md`
