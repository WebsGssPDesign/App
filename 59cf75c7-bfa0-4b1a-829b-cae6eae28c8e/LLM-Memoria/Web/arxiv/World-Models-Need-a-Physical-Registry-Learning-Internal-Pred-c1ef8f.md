---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2610.16365v1"
tema: "Terraform Provider Registry"
tags: [web]
---
# World Models Need a Physical Registry: Learning Internal Predictive States for Physically Plausible World Models

## Resumen
El artículo presenta el "Physical Registry", un mecanismo que introduce slots de registro temporalmente fundamentados dentro de modelos DiT para video, permitiendo que las predicciones de la evolución escénica existan como un estado explícito y legible. Esta arquitectura mejora significativamente la generación físicamente plausible en comparación con los enfoques estándar donde dinámicas y apariencia están codificadas juntas. Además, se propone un selector (PRS) que evalúa futuros emergentes basándose en su desviación de una proyección inicial para mejorar la calidad sin necesidad de puntuación externa completa.

## Datos clave
- **Physical Registry**: Slots dentro del video DiT inicializados con pronósticos condicionados por observaciones y co-evolucionan con los tokens de video.
- **Mejora en Physics-IQ Verified**: Aumento de 9.9/8.7 puntos sobre el ajuste fino estándar (I2V/V2V).
- **Eficiencia paramétrica**: Logrado con solo un 0.45% de parámetros adicionales.
- **Récord de rendimiento**: Cosmos 3 Nano 16B supera a Cosmos 3 Super 64B en I2V (43.56 vs. 42.7).
- **Physical Registry Selector (PRS)**: Mejora las puntuaciones I2V entre un 5.6% y un 15.9% mediante la selección de futuros basada en lecturas intermedias del registro.

## Etiquetas
#WorldModels #VideoGeneration #PhysicsPlausibility #DeepLearning #PredictiveStates

Fuente: http://arxiv.org/abs/2610.16365v1
