---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2606.20772v1"
tema: "Dapr Sidecar"
tags: [web]
---
# Mind the Privileged-to-Camera Gap: Actor-Centric Sidecar Supervision for Camera-First Open-Loop Waypoint Prediction

## Resumen
Este estudio aborda la brecha entre información privilegiada de simuladores y datos limitados de cámaras en la predicción de trayectorias para vehículos autónomos. Propone un método de supervisión centrado en actores que utiliza etiquetas derivadas de simuladores durante el entrenamiento para mejorar la representación de usuarios viales cercanos, sin introducir estas etiquetas como entrada en tiempo real. Los resultados demuestran una reducción significativa del error final (FDE) al incorporar esta supervisión lateral ("sidecar") comparada con enfoques basados únicamente en imágenes o control estándar.

## Datos clave
- **Métricas de error:** El método RU-sidecar reduce el FDE a 1.223 ± 0.01 m, frente a 1.815 ± 0.02 m del baseline y 1.716 ± 0.02 m del control sin maestro.
- **Reducción de error:** Mejora del 32.6% sobre el baseline plano y del 28.7% sobre el control no sidecar.
- **Casos específicos:** Gains del 29.1% con cuatro o más actores válidos y del 30.0% cuando hay usuarios vulnerables presentes.
- **Limitaciones:** La evidencia proviene exclusivamente de diagnósticos en simulación abierta; existe una brecha persistente entre estados de simulador (privilegiados) y datos de cámara.

## Etiquetas
#conducción-autónoma #predicción-de-trayectoria #aprendizaje-supervisado #visión-computacional

Fuente: http://arxiv.org/abs/2606.20772v1
