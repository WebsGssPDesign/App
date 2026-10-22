---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2512.12314v1"
tema: "Tracing OpenTelemetry"
tags: [web]
---
# Evaluating Asynchronous Semantics in Trace-Discovered Resilience Models: A Case Study on the OpenTelemetry Demo

## Resumen
Este estudio evalúa si incluir semánticas asíncronas mejora la precisión de los modelos de resiliencia descubiertos mediante trazas en el caso del "Astronomy Shop" de OpenTelemetry. Los autores comparan un modelo que trata las dependencias de Kafka como bloqueantes frente a uno que las considera no bloqueantes para respuestas HTTP inmediatas. Los resultados indican que, para este escenario específico, modelar explícitamente la asincronía no aporta beneficios significativos en la estimación de disponibilidad.

## Datos clave
- **Modelo**: Gráfico de dependencias derivado directamente de trazas crudas de OpenTelemetry.
- **Método**: Simulación de Monte Carlo para estimar disponibilidad bajo fallos "fail-stop".
- **Herramienta**: Workflow de GitHub Actions que ejecuta experimentos de caos (matando microservicios) en Docker Compose.
- **Hallazgo principal**: La inclusión de semánticas asíncronas cambia las predicciones de disponibilidad en máximo 10⁻⁵ (0.001 puntos porcentuales).
- **Conclusión**: Un modelo de conectividad simple es suficiente para estimar la degradación de disponibilidad inmediata HTTP; no se justifica modelar dependencias asíncronas explícitamente aquí.

## Etiquetas
#OpenTelemetry #Resiliencia #TrazabilidadDistribuida #ChaosEngineering #SimulaciónMonteCarlo

Fuente: http://arxiv.org/abs/2512.12314v1
