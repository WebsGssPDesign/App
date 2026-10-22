---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2610.02914v2"
tema: "Terraform Sentinel Custom Rules"
tags: [web]
---
# Custom Forcing: Training-Free Subject Customization for Autoregressive Video Generation

## Resumen
Custom Forcing es un método sin entrenamiento para personalizar sujetos específicos en la generación de video autoregresiva, almacenando fotogramas de referencia en el caché KV persistente del modelo congelado. Para superar las limitaciones de los anclajes fijos, como la deriva de identidad y la preferencia por sujetos genéricos, introduce mecanismos de amplificación adaptativa y guía de contraste. Esta técnica mantiene una alta fidelidad visual durante rodados largos sin sacrificar la velocidad de generación ni el movimiento del video.

## Datos clave
- **Método**: Custom Forcing (entrenamiento libre).
- **Mecanismos**: Drift-adaptive value amplification (DVA) y anchor contrast guidance (ACG).
- **Almacenamiento**: Fotogramas ancla en caché KV persistente.
- **Velocidad**: 9.5 a 28.5 veces más rápido que las líneas base de video largo.
- **Métrica de identidad (DINO-I)**: Mantiene entre 0.58 y 0.62 (vs caída a 0.42 en anclajes fijos).
- **Duración**: Efectivo en rodados de hasta dos minutos.

## Etiquetas
#generacion_de_video #customization #autoregresivo #eficiencia #identidad_visual

Fuente: http://arxiv.org/abs/2610.02914v2
