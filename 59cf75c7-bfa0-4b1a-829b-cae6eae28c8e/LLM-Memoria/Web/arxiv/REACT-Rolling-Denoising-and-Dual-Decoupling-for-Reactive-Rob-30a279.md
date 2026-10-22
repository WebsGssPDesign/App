---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2610.12007v1"
tema: "React Server Actions Streaming"
tags: [web]
---
# REACT: Rolling Denoising and Dual Decoupling for Reactive Robot Control with VLA Models

## Resumen
El artículo presenta REACT, un marco de control robótico que mejora la reactividad de los modelos VLA basados en flujo manteniendo el contexto a largo plazo. A diferencia de generar acciones desde cero, REACT utiliza un buffer persistente donde las acciones futuras se refinan iterativamente con nuevas observaciones antes de ejecutarse. La técnica incluye un mecanismo de "doble desacoplamiento" para separar la percepción del control y permitir actualizaciones de alta frecuencia dentro de límites computacionales prácticos.

## Datos clave
- **REACT**: Marco de desensiamiento en rodillo (rolling-denoising) para VLAs.
- **Buffer persistente**: Mantiene timesteps de flujo escalonados para evitar discontinuidades.
- **Refinamiento iterativo**: Cada bloque de acción se mejora con múltiples observaciones recientes antes del despliegue.
- **Doble desacoplamiento**: Sepera percepción, codificación VLM, desensiamiento DiT y ejecución de acciones en tiempo real.
- **Resultados**: Mejora el éxito de tareas y reduce la latencia de reacción en RoboTwin 2.0 y robots reales frente a líneas base de replaneamiento frecuente.

## Etiquetas
#control_robótico #IA_generativa #modelos_VLA #tiempo_real #optimización

Fuente: http://arxiv.org/abs/2610.12007v1
