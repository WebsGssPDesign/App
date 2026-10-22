---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/touchdesigner-mcp/references/panel-ui.md"
tags: [hecho]
---
# panel-ui.md

## Resumen
Este documento describe cómo crear interfaces de usuario interactivas en TouchDesigner utilizando controles personalizados y widgets visuales. Sirve como guía para desarrollar racks de control, consolas de instalación o paneles táctiles que permiten a los usuarios modificar parámetros del proyecto en tiempo real mediante botones, deslizadores e inputs de texto.

## Datos clave
- **Conceptos principales**: Diferencia entre *Custom Parameters* (configuración persistente) y *Panel COMPs* (widgets visuales interactivos).
- **Widgets disponibles**: `buttonCOMP`, `sliderCOMP`, `fieldCOMP`, `listCOMP` dentro de un contenedor `containerCOMP`.
- **Lógica de conexión**: Los widgets actualizan parámetros usando expresiones en tiempo real (`ParMode.EXPRESSION`) o disparan eventos mediante nodos `panelExecuteDAT`.
- **Estructura de layout**: Uso del parámetro `align` (ej. 'toptobottom', 'lefttoright') para organizar automáticamente los hijos dentro del contenedor.
- **Flujo de trabajo típico**: Crear un `containerCOMP`, añadir widgets, vincular sus valores a parámetros del componente padre y programar callbacks para acciones específicas.

## Etiquetas
#TouchDesigner #UI_Diseño #Interfaz_Táctil #Automatización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\touchdesigner-mcp\references\panel-ui.md`
