---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/touchdesigner-mcp/references/mcp-tools.md"
tags: [hecho]
---
# mcp-tools.md

## Resumen
Este documento referencia 36 herramientas de la suite MCP v2.774+ para interactuar con proyectos de TouchDesigner. Su función principal es automatizar tareas como la creación de nodos, ejecución de scripts Python y exploración de la estructura de red del proyecto sin necesidad de acceso manual al editor gráfico.

## Datos clave
- **Herramientas principales**: `td_execute_python` (ejecución de código), `td_create_operator` (creación de nodos TOP/CHOP/SOP/DAT/COMP/MAT), `td_get_network` (inspección de estructura).
- **Búsqueda y análisis**: `td_find_op` para localizar operadores por nombre o tipo, y `td_search` para buscar texto en scripts, expresiones y parámetros.
- **Navegación**: `td_navigate_to` para mover la vista del editor hacia un operador específico.
- **Parámetros comunes**: Uso de `target_instance` para escenarios multi-instancia; soporte para rutas como `/project1`, `/ui`, `/sys`.
- **Optimización**: Recomendado usar `td_create_operator` para nodos individuales y `td_execute_python` para lotes de 5 o más.

## Etiquetas
#TouchDesigner #Automatización #MCPTools #DesarrolloVisual

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\touchdesigner-mcp\references\mcp-tools.md`
