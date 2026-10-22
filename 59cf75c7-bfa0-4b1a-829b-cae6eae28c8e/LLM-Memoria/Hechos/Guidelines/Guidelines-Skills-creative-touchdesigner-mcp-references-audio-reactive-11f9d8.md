---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/touchdesigner-mcp/references/audio-reactive.md"
tags: [hecho]
---
# audio-reactive.md

## Resumen
Este documento establece patrones técnicos para crear visuales reactivos al audio en TouchDesigner, cubriendo la extracción de bandas espectrales, detección de golpes y la transmisión de datos a shaders GLSL. Su objetivo es guiar el desarrollo de sistemas de visualización robustos mediante una estructura de nodos estandarizada y correcciones específicas para versiones recientes del software.

## Datos clave
- **Proyecto**: Referencias para audio-reactive visuals en TouchDesigner (versión 2025).
- **Tecnologías**: Python scripting, CHOPs, GLSL shaders, MIDI input.
- **Decisiones críticas**: Usar `analyzeCHOP.par.function = 'rmspower'` y evitar `lagCHOP` para suavizado de espectro debido a errores de muestreo.
- **Rutas y nodos clave**: `audiofilterCHOP` (filtros paso bajo/alto), `triggerCHOP` (detección de kick), `mathCHOP` con ganancia directa, conexión de expresiones en GLSL (`ParMode.EXPRESSION`).
- **Comandos/Pasos**: Crear buses dentro de un `baseCOMP`, conectar filtros en cascada para bandas Low/Mid/High, y mapear canales MIDI a parámetros de nodos visuales.

## Etiquetas
#TouchDesigner #AudioReactive #GLSL #PythonScripting #VisualEffects

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\touchdesigner-mcp\references\audio-reactive.md`
