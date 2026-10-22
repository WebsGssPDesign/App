---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/comfyui/references/rest-api.md"
tags: [hecho]
---
# rest-api.md

## Resumen
Este documento detalla la interfaz de API REST y WebSocket de ComfyUI, diferenciando entre el uso local y en la nube. Sirve como guía técnica para ejecutar flujos de trabajo, consultar estados de tareas y descargar resultados, manejando automáticamente las divergencias de autenticación y rutas entre ambos entornos.

## Datos clave
- **Proyecto**: Referencia API ComfyUI (local vs Cloud).
- **Tecnologías**: REST, WebSocket, Bash (`curl`, `wscat`).
- **Decisiones/Rutas**: Las rutas locales (ej. `/prompt`) cambian a `/api/prompt` en la nube; el historial se renombró de `/history` a `/api/history_v2`.
- **Comandos importantes**:
  - Envío local: `curl ... http://127.0.0.1:8188/prompt` (sin auth).
  - Envío Cloud: `curl ... https://cloud.comfy.org/api/prompt` con header `X-API-Key`.
  - Descarga Cloud: Usar `-L` para seguir redirección 302 a URL firmada.
- **Diferencias críticas**: En la nube, `/object_info`, `/queue` y `/view` requieren suscripción de pago; la respuesta de lista de modelos cambia de array plano a objetos JSON.

## Etiquetas
#ComfyUI #APIReference #PythonScripts #CloudComputing

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\comfyui\references\rest-api.md`
