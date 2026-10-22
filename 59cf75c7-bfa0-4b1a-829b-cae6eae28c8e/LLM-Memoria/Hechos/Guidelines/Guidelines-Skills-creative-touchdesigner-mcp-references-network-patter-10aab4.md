---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/touchdesigner-mcp/references/network-patterns.md"
tags: [hecho]
---
# network-patterns.md

## Resumen
Este documento recopila recetas de red completas para TouchDesigner que vinculan datos de audio con generadores visuales. Sirve como guía técnica para construir efectos reactivos al ritmo, espectros y bandas de frecuencia utilizando operadores nativos y llamadas a herramientas MCP.

## Datos clave
- **Patrones principales**: Visuales reactivos al audio (espectro -> ruido), detección de golpes (beats) y separación multibanda.
- **Operadores clave**: `audiofileinChop`, `audiospectrumCHOP`, `mathCHOP`, `noiseTOP`, `feedbackTop`, `GLSL TOP`.
- **Configuraciones críticas**: FFT=512 para espectro, aislamiento de graves (bins 0-10), parámetros ADSR en `triggerCHOP`.
- **Comandos MCP**: Uso de `td_create_operator` para instanciar nodos y `td_set_operator_pars` para configurar rutas, archivos y valores numéricos.
- **Conexiones**: Scripts Python (`td_execute_python`) para conectar salidas e entradas de operadores y asignar expresiones matemáticas a parámetros (ej. `.par.seed.expr`).

## Etiquetas
#TouchDesigner #AudioVisuals #CreativeCoding #MCP

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\touchdesigner-mcp\references\network-patterns.md`
