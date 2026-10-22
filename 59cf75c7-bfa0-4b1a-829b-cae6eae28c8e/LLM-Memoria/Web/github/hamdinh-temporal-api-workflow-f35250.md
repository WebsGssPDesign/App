---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/hamdinh/temporal-api-workflow"
tema: "Temporal Workflow Retry Policies"
tags: [web]
---
# hamdinh/temporal-api-workflow

## Resumen
Este proyecto de ejemplo en Python utiliza el framework Temporal para ejecutar un flujo de trabajo de dos pasos contra una API FastAPI: crear un widget y luego leerlo. El diseño implementa políticas de reintento diferenciadas, donde la creación tiene retries limitados explícitamente, mientras que la lectura falla controlando el código del workflow para reejecutar toda la secuencia si es necesario.

## Datos clave
- **Pasos del flujo**: `POST /api/v1/widgets` (crear) y `GET /api/v1/widgets/{widget_id}` (leer).
- **Política de reintento POST**: 3 intentos explícitos en caso de fallo transitorio.
- **Manejo de errores GET**: No tiene política de retry; el workflow captura la excepción y reejecuta toda la secuencia una vez desde el inicio.
- **Idempotencia**: Se envía un header `Idempotency-Key` para garantizar que las operaciones de creación sean seguras ante reintentos.
- **Requisitos técnicos**: Python 3.12+, gestor `uv`, servidor Temporal en puerto 7233 y API FastAPI local.

## Etiquetas
#temporal #fastapi #python #workflow #idempotencia

Fuente: https://github.com/hamdinh/temporal-api-workflow
