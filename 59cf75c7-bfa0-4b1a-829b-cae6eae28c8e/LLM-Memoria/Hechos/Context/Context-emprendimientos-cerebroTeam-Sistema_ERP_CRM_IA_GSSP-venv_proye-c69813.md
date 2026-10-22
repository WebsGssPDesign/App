---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/cerebroTeam/Sistema_ERP_CRM_IA_GSSP/venv_proyecto/Lib/site-packages/fastapi/.agents/skills/fastapi/references/streaming.md"
tags: [hecho]
---
# streaming.md

## Resumen
Este documento explica cómo implementar flujos de datos en tiempo real (streaming) dentro de aplicaciones FastAPI. Detalla las técnicas para transmitir JSON Lines, Server-Sent Events (SSE) y bytes binarios utilizando generadores asíncronos (`yield`) y respuestas especializadas. Su utilidad radica en optimizar la transferencia de grandes volúmenes de datos o contenido multimedia sin bloquear la conexión del cliente.

## Datos clave
- **Tecnologías**: FastAPI, Pydantic, `EventSourceResponse`, `StreamingResponse`.
- **Decisiones**: Se prefiere heredar de `StreamingResponse` definiendo el `media_type` en lugar de usar la clase base directamente para mayor control.
- **Pasos importantes**:
  - Para JSON Lines: declarar el tipo de retorno como `AsyncIterable[Item]` y usar `yield`.
  - Para SSE: configurar `response_class=EventSourceResponse` y usar `ServerSentEvent` para controlar campos personalizados (`event`, `id`, `retry`) o `raw_data` para texto plano.
  - Para bytes: crear una subclase de `StreamingResponse` (ej. `PNGStreamingResponse`) con el tipo MIME adecuado y iterar sobre los datos binarios.

## Etiquetas
#FastAPI #Streaming #SSE #Backend

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\cerebroTeam\Sistema_ERP_CRM_IA_GSSP\venv_proyecto\Lib\site-packages\fastapi\.agents\skills\fastapi\references\streaming.md`
