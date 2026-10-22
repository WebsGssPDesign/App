---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/touchdesigner-mcp/references/operators.md"
tags: [hecho]
---
# operators.md

## Resumen
Este documento detalla la referencia de operadores de TouchDesigner, organizándolos en seis familias según el tipo de datos que procesan. Sirve como guía esencial para entender cómo conectar nodos, generar texturas procedurales y manipular señales temporales en proyectos visuales.

## Datos clave
- **Familias**: Se dividen en TOPs (texturas), CHOPs (canales/audió), SOPs, DATs, MATs y COMPs.
- **TOPs principales**: `noiseTop` para ruido procedural, `glslTop` para shaders personalizados, `renderTop` para renderizado 3D y `feedbackTop` para efectos recursivos.
- **CHOPs principales**: `lfoChop` como motor de animación, `constantChop` para parámetros estáticos y `noiseChop` para movimiento orgánico.
- **Conversión**: Uso de `choptopTop` (datos a imagen) y `topchopChop` (imagen a datos).
- **Composición**: Operadores como `compositeTop`, `addTop` y `switchTop` para mezclar entradas.

## Etiquetas
#TouchDesigner #GenerativeArt #VisualEffects #NodeBased

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\touchdesigner-mcp\references\operators.md`
