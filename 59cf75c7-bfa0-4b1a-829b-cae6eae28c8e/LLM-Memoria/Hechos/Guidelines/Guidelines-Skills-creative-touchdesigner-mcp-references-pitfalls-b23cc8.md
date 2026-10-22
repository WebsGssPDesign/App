---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/touchdesigner-mcp/references/pitfalls.md"
tags: [hecho]
---
# pitfalls.md

## Resumen
Este documento recopila errores críticos y lecciones aprendidas al automatizar TouchDesigner mediante MCP, enfocándose en la compatibilidad entre versiones de parámetros, el manejo seguro de nodos y las particularidades del compilador GLSL. Su objetivo es guiar a los desarrolladores para evitar fallos comunes como scripts que se detienen abruptamente o shaders que no compilan correctamente.

## Datos clave
- **Parámetros dinámicos**: Nunca hardcodear nombres; usar `td_get_par_info` y el patrón `safe_par()` para evitar `tdAttributeError`.
- **Respuestas de Python**: El formato de respuesta de `td_execute_python` incluye un prefijo `(ok)`, no solo el dict resultante.
- **GLSL en TOPs**: No existe `uTDCurrentTime`; usar `absTime.seconds` o Constant TOP con formato `rgba32float`.
- **Compatibilidad macOS**: El output GLSL requiere obligatoriamente la función `TDOutputSwizzle()`.
- **Gestión de nodos**: Separar la destrucción y creación de nodos en llamadas distintas a `td_execute_python` para evitar errores de referencia.

## Etiquetas
#TouchDesigner #MCP #GLSL #Automatización #PythonAPI

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\touchdesigner-mcp\references\pitfalls.md`
