---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/ascii-video/references/shaders.md"
tags: [hecho]
---
# shaders.md

## Resumen
Este documento describe una arquitectura de procesamiento post-renderizado para video ASCII que transforma renders crudos en salida cinematográfica mediante efectos compuestos. El sistema se basa en la modularidad, permitiendo combinar shaders independientes, modos de mezcla a nivel de píxel y buffers de retroalimentación temporal para crear estilos visuales variados como glitch art o atmósferas oníricas.

## Datos clave
- **Tecnologías**: Python (NumPy), arrays uint8/float32.
- **Función principal**: `blend_canvas(base, top, mode, opacity)` para mezclar capas con modos específicos.
- **Modos de mezcla**: 20 modos disponibles (normal, add, screen, difference, etc.) operando en espacio float32 [0,1].
- **FeedbackBuffer**: Clase para efectos recursivos temporales con parámetros como `decay`, `blend`, `opacity` y transformaciones espaciales (`zoom`, `rotate_cw`).
- **Presets de feedback**: Configuraciones listas para usar (túnel infinito, estelas arcoíris, eco fantasmal).
- **ShaderChain**: Pipeline componible para orquestar múltiples efectos en secuencia.

## Etiquetas
#post-procesado #ascii-art #shaders-python #efectos-visuales

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\ascii-video\references\shaders.md`
