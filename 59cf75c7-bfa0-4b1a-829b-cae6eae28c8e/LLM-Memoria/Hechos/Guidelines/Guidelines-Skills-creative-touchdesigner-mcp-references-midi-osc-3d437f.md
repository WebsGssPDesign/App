---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/touchdesigner-mcp/references/midi-osc.md"
tags: [hecho]
---
# midi-osc.md

## Resumen
Este documento sirve como guía técnica para integrar controladores externos (MIDI y OSC) en TouchDesigner, detallando cómo descubrir dispositivos, mapear controles a parámetros del proyecto y gestionar la comunicación de red para interfaces móviles o sistemas de show. Su objetivo es estandarizar flujos de trabajo para entradas de hardware MIDI y control remoto vía OSC.

## Datos clave
- **MIDI Input**: Usar `midiinDAT` para enumerar dispositivos o `op.MIDI.devices` en Python; conectar `midiinCHOP` a parámetros mediante expresiones (ej: `"op('midi_in')['ch1c74'][0] / 127.0"`).
- **MIDI Learn**: Patrón con `selectCHOP` y `tableDAT` para mapear CC desconocidos dinámicamente.
- **OSC Input/Output**: Configurar `oscinCHOP` (ej: puerto 7000) y `oscoutCHOP`; los nombres de canales se convierten en direcciones OSC con `/`.
- **Gotchas**: TD crea el canal de entrada solo tras recibir el primer mensaje; usar `oscinDAT` para acceso a argumentos crudos.
- **Red/Multimáquina**: Usar broadcast UDP (`192.168.x.255`) para sincronización entre instancias o relay web para WAN.

## Etiquetas
#TouchDesigner #MIDI #OSC #Networking #LivePerformance

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\touchdesigner-mcp\references\midi-osc.md`
