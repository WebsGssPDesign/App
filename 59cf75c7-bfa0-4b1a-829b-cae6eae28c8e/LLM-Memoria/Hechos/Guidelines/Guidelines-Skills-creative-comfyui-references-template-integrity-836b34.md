---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/comfyui/references/template-integrity.md"
tags: [hecho]
---
# template-integrity.md

## Resumen
Esta guía técnica explica cómo convertir correctamente los flujos de trabajo de ComfyUI desde el formato de editor a la API para su envío, evitando errores de validación comunes. Su objetivo es preservar la integridad de nodos complejos como Reroute y estructuras dinámicas al adaptar plantillas oficiales para entornos de producción o nube.

## Datos clave
- **Proyecto**: Adaptación de `comfyui-workflow-templates` (v0.9.69) a formato API `/api/prompt`.
- **Tecnologías**: ComfyUI, Python, JSON, nodos personalizados (`ComfyMathExpression`, `COMFY_DYNAMICCOMBO_V3`).
- **Reglas críticas**: Nunca eliminar nodos ni simplificar topología; mantener nombres de claves con puntos (ej. `resize_type.width`) sin aplanar.
- **Manejo de Reroute**: Reemplazar referencias al nodo por `[source_node_id, source_slot]` y eliminar el nodo Reroute del mapeo API.
- **Depuración**: Usar el campo `extra_info.input_name` en los errores del servidor para identificar claves JSON exactas.
- **Comando de ruta**: `comfy --workspace <ws> run-python -c "import comfyui_workflow_templates, pathlib; print(pathlib.Path(comfyui_workflow_templates.__file__).parent / 'templates')"`

## Etiquetas
#ComfyUI #WorkflowsAPI #GeneraciónDeVideo #DevOps

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\comfyui\references\template-integrity.md`
