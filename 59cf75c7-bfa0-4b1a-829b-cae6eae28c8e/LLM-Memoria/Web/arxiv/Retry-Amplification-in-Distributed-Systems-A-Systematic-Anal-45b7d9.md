---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2608.25403v1"
tema: "Temporal Workflow Retry Policies"
tags: [web]
---
# Retry Amplification in Distributed Systems: A Systematic Analysis of Retry Policies and Their Role in Cascading Failures

## Resumen
Este artículo analiza cómo las políticas de reintento en sistemas distribuidos pueden generar fallos en cascada al amplificar la carga durante errores parciales. Los autores introducen el "factor de amplificación por reintento" (RAF) y estudian 200 proyectos, encontrando que muchas configuraciones carecen de estrategias adecuadas como el *backoff*. Se demuestra que las políticas estándar reducen significativamente la tasa de éxito bajo fallos correlacionados, mientras que una propuesta llamada "Adaptive Retry Budgeting" mantiene la estabilidad del sistema.

## Datos clave
- **Factor de Amplificación por Reintento (RAF)**: Métrica que cuantifica el volumen adicional de solicitudes generadas durante fallos parciales.
- **Prevalencia real**: Cerca del 41% de los proyectos tienen lógica explícita de reintento, aunque solo se detectó automáticamente en un 11.5%.
- **Configuraciones problemáticas**: El 60.9% de los proyectos analizados incluyen al menos una configuración sin *backoff*.
- **Impacto negativo**: Bajo fallos correlacionados, el reintento estándar reduce la tasa de éxito del 55.4% al 41.5%.
- **Solución propuesta**: Adaptive Retry Budgeting (ARB), que limita los reintentos para mantener tasas de éxito cercanas a las de no realizar ningún reintento.

## Etiquetas
#sistemas-distribuidos #microservicios #fiabilidad #fallos-en-cascada #arquitectura-de-sistemas

Fuente: http://arxiv.org/abs/2608.25403v1
