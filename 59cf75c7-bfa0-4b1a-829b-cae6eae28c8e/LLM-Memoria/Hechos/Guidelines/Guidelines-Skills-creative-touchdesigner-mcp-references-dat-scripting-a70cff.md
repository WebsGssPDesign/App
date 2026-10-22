---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/touchdesigner-mcp/references/dat-scripting.md"
tags: [hecho]
---
# dat-scripting.md

## Resumen
Este documento es una guía técnica sobre el modelo de eventos y callbacks en TouchDesigner, específicamente para scripts basados en DATs. Explica cómo configurar diferentes tipos de ejecutores (como `chopExecuteDAT` o `panelExecuteDAT`) para reaccionar a cambios en audio, datos tabulares, parámetros o interfaces gráficas mediante Python.

## Datos clave
- **Tipos de ejecutores**: `chopExecuteDAT` (audio), `datExecuteDAT` (tablas/APIs), `parameterExecuteDAT` (parámetros), `panelExecuteDAT` (UI), `opExecuteDAT` (ciclo de vida de operadores) y `executeDAT` (proyecto).
- **Patrones comunes**: Uso de funciones como `offToOn`, `onTableChange` o `onClick` dentro del DAT acoplado.
- **Objetos clave**: `Channel`, `Par`, `op()` para manipular nodos, y `json.loads()` para procesar respuestas webDAT.
- **Configuración típica**: Crear el nodo con `root.create()`, asignar la ruta (`par.chop` o `par.dat`) y activar flags como `offtoon=True`.
- **Rutas de ejemplo**: `/project1/audio/out_kick`, `/project1/api/web1`, `/project1/scene`.

## Etiquetas
#TouchDesigner #PythonScripting #DATs #Automation #EventCallbacks

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\touchdesigner-mcp\references\dat-scripting.md`
