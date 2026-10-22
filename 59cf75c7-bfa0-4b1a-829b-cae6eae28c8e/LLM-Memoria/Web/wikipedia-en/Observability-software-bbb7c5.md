---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Observability_%28software%29"
tema: "OpenTelemetry Semantic Conventions"
tags: [web]
---
# Observability (software)

## Resumen
La observabilidad en ingeniería de software es la capacidad de entender el estado interno de un sistema distribuido analizando datos externos como métricas, registros y trazas. A diferencia del monitoreo tradicional que depende de conocimiento previo y alertas definidas, la observabilidad permite investigar estados novedosos sin necesidad de desplegar nuevo código.

## Datos clave
- **Pilares**: Métricas (mediciones escalares en un punto temporal), Registros (texto estructurado o no) y Trazas (secuencia de eventos que siguen una solicitud a través de servicios).
- **Diferencia principal**: El monitoreo usa conjuntos predefinidos de datos y requiere experiencia senior; la observabilidad se basa en el análisis exploratorio para entender cualquier estado del sistema.
- **Término**: "O11y" (numerónimo por las 11 letras entre la primera y la última).
- **Limitación de métricas**: Al ser instrumentadas antes del lanzamiento, no pueden añadirse nuevas sin desplegar código, lo que dificulta diagnosticar problemas desconocidos.
- **Trazas distribuidas**: Utilizan identificadores únicos en encabezados HTTP para correlacionar "spans" (eventos discretos) entre servicios y mostrar relaciones causales.

## Etiquetas
#observabilidad #ingenieria_de_software #telemetria #monitoreo #trazas_distribuidas

Fuente: https://en.wikipedia.org/wiki/Observability_%28software%29
