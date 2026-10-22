---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/richard-t-tam/temporal-workflow-patterns"
tema: "Temporal Workflow Idempotency Patterns"
tags: [web]
---
# richard-t-tam/temporal-workflow-patterns

## Resumen
Este repositorio documenta patrones de diseño para workflows en Temporal, enfocándose en la mecánica de reproducción (replay), la evolución segura de versiones y el manejo determinista del estado. A través de una progresión paso a paso, ilustra cómo garantizar la consistencia entre código actual e historia registrada, así como estrategias para evitar efectos duplicados durante reintentos.

## Datos clave
- **Mecánica de Replay**: Reconstrucción del estado desde el historial de eventos; si el código no coincide con la historia, falla.
- **Guías de versión (`workflow.patched`)**: Permiten despliegues seguros donde nuevas ejecuciones usan rama actual y viejas usan la histórica.
- **Idempotencia en actividades**: Uso de claves semánticas para detectar efectos duplicados al reintentar; el estado del negocio debe ser seguro ante múltiples ejecuciones.
- **Validación antes del efecto**: La lógica de validación debe ocurrir en el workflow *antes* de programar una actividad, ya que no se puede cancelar una vez programada.
- **Control por señales**: Uso de señales para autorización, condiciones compuestas y resolución determinista entre temporizadores y señales (el primero registrado gana).
- **Reducción de estado compartido**: Eliminar bloqueos explícitos aprovechando la ejecución secuencial garantizada del historial de Temporal.

## Etiquetas
#Temporal #WorkflowsPython #Idempotencia #PatronesDeDiseño #Determinismo

Fuente: https://github.com/richard-t-tam/temporal-workflow-patterns
