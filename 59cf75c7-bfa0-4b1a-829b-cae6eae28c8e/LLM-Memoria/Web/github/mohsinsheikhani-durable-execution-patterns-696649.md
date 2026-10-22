---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/mohsinsheikhani/durable-execution-patterns"
tema: "Temporal Workflow Idempotency Patterns"
tags: [web]
---
# mohsinsheikhani/durable-execution-patterns

## Resumen
Este repositorio demuestra la implementación de patrones de ejecución duradera utilizando Temporal para un flujo de trabajo de triage de tickets. El enfoque central es almacenar el estado en un historial de eventos del servidor, lo que permite a los trabajadores recuperarse automáticamente tras fallos sin reprocesar tareas costosas ni repetir efectos secundarios ya ejecutados.

## Datos clave
- **Arquitectura**: Separación clara entre `workflows.py` (sandbox determinista) y actividades externas (`activities.py`).
- **Recuperación**: Si un worker muere durante una actividad, esta se reejecuta; si ya completó, el flujo continúa con el resultado guardado.
- **Comandos de prueba**:
  - `temporal server start-dev`: Inicia la UI en localhost:8233.
  - `uv run starter.py`: Inicia el cliente que lanza el workflow.
  - Señalización: `temporal workflow signal --workflow-id <id> --name approve`.
- **Ventajas**: Las consultas (`query`) solo leen estado sin costo de historial, mientras que las señales (`signal`) son entradas duraderas. Los temporizadores permiten esperar horas o días sin consumir CPU ni memoria del worker.
- **Determinismo**: El sandbox bloquea funciones no deterministas (como `random`) antes de la ejecución; errores de lógica no matan el workflow, solo lo ponen en bucle de reintentos.

## Etiquetas
#Temporal #EjecuciónDuradera #PatronesDeSoftware #IAAgente #Orquestación

Fuente: https://github.com/mohsinsheikhani/durable-execution-patterns
