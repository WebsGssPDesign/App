---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/touchdesigner-mcp/references/python-api.md"
tags: [hecho]
---
# python-api.md

## Resumen
Este documento describe la referencia de la API de Python para TouchDesigner, detallando cómo interactuar con nodos y parámetros desde scripts externos o MCP. Sirve como guía técnica para automatizar tareas, modificar la estructura del proyecto dinámicamente y conectar operadores mediante código en lugar de hacerlo manualmente en la interfaz gráfica.

## Datos clave
- **Módulo principal**: `td` (auto-importado), con accesos rápidos a `op`, `ops`, `me`, `parent` y `project`.
- **Búsqueda de nodos**: Uso de `op(path)` para nodos únicos y `ops(pattern)` con glob patterns para múltiples nodos.
- **Manipulación de parámetros**: Acceso vía `.par.nombre.val` para lectura/escritura, soporte para expresiones dinámicas (ej: `"me.time.frame"`) y tipos como Float, Int, Toggle, String y referencias a otros operadores.
- **Creación y destrucción**: Métodos `parent.create()`, `node.destroy()` y `parent.copy()`.
- **Conexiones (Wiring)**: Uso de `outputConnectors[0].connect(op_path)` para enlazar salidas con entradas, incluyendo patrones de cadena lineal o abanico.
- **Herramientas MCP**: Se mencionan herramientas específicas como `execute_python_script` y `create_td_node`.

## Etiquetas
#TouchDesigner #PythonAPI #Automatización #Nodos3D

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\touchdesigner-mcp\references\python-api.md`
