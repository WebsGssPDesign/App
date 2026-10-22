---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/data-science/jupyter-live-kernel/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía describe una habilidad técnica para ejecutar Python iterativo mediante un kernel de Jupyter en vivo, permitiendo que las variables persistan entre ejecuciones. Es ideal para exploración de datos y ciencia de datos cuando se requiere mantener el estado a diferencia de scripts sin estado o comandos de terminal.

## Datos clave
- **Prerrequisitos**: Instalación de `uv` y `JupyterLab`.
- **Configuración**: Clonar repositorio `hamelnb`, iniciar servidor con `jupyter-lab --no-browser --port=8888` y crear sesión vía API REST.
- **Comandos principales**: `execute` para correr código, `variables` para inspeccionar estado, `edit` para modificar celdas y `restart-run-all` para verificación limpia.
- **Flujo de trabajo**: Usar siempre la bandera `--compact` para ahorrar tokens; el orden de argumentos es crítico (ej. `variables --path nb.ipynb list`).

## Etiquetas
#jupyter #datascience #python #repl #iterative

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\data-science\jupyter-live-kernel\SKILL.md`
