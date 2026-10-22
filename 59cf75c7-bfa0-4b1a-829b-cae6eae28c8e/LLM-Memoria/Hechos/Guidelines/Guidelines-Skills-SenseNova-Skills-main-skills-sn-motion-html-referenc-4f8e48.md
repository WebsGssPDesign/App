---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-motion-html/references/seedance.md"
tags: [hecho]
---
# seedance.md

## Resumen
Este documento define la integración técnica con la API de generación de contenido Seedance para crear videos a partir de prompts y referencias visuales. Su función principal es estandarizar el flujo de trabajo, desde la solicitud asíncrona hasta la normalización final del video mediante FFmpeg, asegurando la recuperación de errores y la gestión segura de credenciales.

## Datos clave
- **API Base**: `https://ark.cn-beijing.volces.com/api/v3`
- **Endpoints**: `POST /contents/generations/tasks` para iniciar tareas y `GET` con el ID para consultar estado (`succeeded`, `failed`, etc.).
- **Configuración**: El modelo, duración, resolución y políticas de audio deben ir en el manifiesto del proyecto; las credenciales en `.env`.
- **Concurrencia**: Uso de un pool de hilos acotado (4 por defecto) donde los "conectores" dependen de que existan los marcos de los "dives" adyacentes.
- **Normalización**: Salida final con FFmpeg, formato H.264 `yuv420p`, GOP corto y sin audio si está en silencio.
- **Seguridad**: Nunca enviar la clave de autorización ni datos sensibles al frontend; no registrar URLs temporales ni tokens.

## Etiquetas
#Seedance #VolcengineAPI #VideoProcessing #FFmpeg #Automation

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-motion-html\references\seedance.md`
