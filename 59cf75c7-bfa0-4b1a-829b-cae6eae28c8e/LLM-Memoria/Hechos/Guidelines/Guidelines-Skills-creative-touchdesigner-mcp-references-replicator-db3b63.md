---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/touchdesigner-mcp/references/replicator.md"
tags: [hecho]
---
# replicator.md

## Resumen
Este documento explica el uso del operador `replicatorCOMP` en TouchDesigner para crear redes de nodos dinámicas basadas en datos. Su función principal es clonar una plantilla única múltiples veces según las filas de una tabla, permitiendo generar interfaces como botones o paneles de control que se actualizan automáticamente sin reconstruir la red completa.

## Datos clave
- **Concepto central**: Clona un operador (plantilla) N veces usando una `tableDAT` como fuente de datos y parámetros.
- **Configuración mínima**: Requiere definir una plantilla, crear una tabla con encabezado y asignar el nombre del campo para nombrar los clones (`namefromdatname`).
- **Personalización por fila**: Se pueden sobrescribir parámetros individuales en cada clon mediante callbacks o expresiones usando `me.digits`.
- **Diseño de cuadrícula**: Utilizar un `containerCOMP` con alineación automática para organizar los clones generados.
- **Actualización en vivo**: Configuraciones como `recreatemissing` permiten añadir o eliminar nodos sin destruir el estado existente al modificar la tabla.
- **Patrones comunes**: Gestión de rosters de escenas, paneles de parámetros dinámicos y visualizadores por canal.
- **Comparativa**: Preferible a bucles de Python cuando los datos cambian en tiempo real; más lento para generación estática única.

## Etiquetas
#TouchDesigner #Replicator #DataDriven #NodeCloning #Automation

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\touchdesigner-mcp\references\replicator.md`
