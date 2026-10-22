---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2401.05355v1"
tema: "OpenTelemetry Resource Detection"
tags: [web]
---
# Developing a Resource-Constraint EdgeAI model for Surface Defect Detection

## Resumen
El artículo propone una arquitectura EdgeAI ligera basada en Xception diseñada específicamente para entrenar modelos directamente en dispositivos de borde con recursos limitados, evitando así los problemas de ancho de banda y privacidad asociados al entrenamiento en la nube. Esta solución se evalúa mediante detección de defectos en placas de circuito impreso (PCB), demostrando un rendimiento competitivo frente a modelos existentes como MobileNetV2 y EfficientNetV2B0 sin necesidad de pre-entrenamiento.

## Datos clave
- **Modelo propuesto:** Arquitectura ligera derivada de Xception para entrenamiento *on-device*.
- **Tarea de prueba:** Detección de defectos en PCB (Placas de Circuito Impreso).
- **Precisión del modelo propuesto (sin pre-entrenamiento):** 73.45%.
- **Comparativa de precisión (sin pre-entrenamiento):** Superior a MobileNetV2 (50.05%) y EfficientNetV2B0 (54.30%); comparable a MobileViT-XXS (75.40%).
- **Ventaja adicional:** Mayor eficiencia en uso de memoria que EfficientNetV2B0 y MobileViT-XXS.
- **Conclusión principal:** La eficiencia de recursos depende no solo del número de parámetros, sino también de las consideraciones arquitectónicas.

## Etiquetas
#EdgeAI #AprendizajeEnElDispositivo #DetecciónDeDefectos #PCB #OptimizaciónDeRecursos

Fuente: http://arxiv.org/abs/2401.05355v1
