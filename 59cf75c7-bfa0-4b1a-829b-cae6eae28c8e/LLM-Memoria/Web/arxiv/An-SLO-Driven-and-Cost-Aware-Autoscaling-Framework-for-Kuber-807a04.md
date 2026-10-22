---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2512.23415v1"
tema: "Kubernetes KEDA Autoscaling"
tags: [web]
---
# An SLO Driven and Cost-Aware Autoscaling Framework for Kubernetes

## Resumen
Este documento presenta un marco de escalado automático para Kubernetes impulsado por SLO y consciente del costo, que utiliza principios de AIOps para mejorar la gestión de recursos. La propuesta integra señales a nivel de aplicación con predicción ligera de demanda para cumplir objetivos de servicio y optimizar gastos simultáneamente. Las evaluaciones experimentales demuestran que este enfoque reduce significativamente las violaciones de SLO, acelera la respuesta al escalado y disminuye los costos de infraestructura en comparación con métodos tradicionales.

## Datos clave
- **Mecanismos nativos de Kubernetes:** Horizontal Pod Autoscaler (HPA), Vertical Pod Autoscaler (VPA) y escaladores a nivel de nodo.
- **Problemas identificados:** Violaciones de SLO por comportamiento reactivo, uso limitado de señales de aplicación y lógica de control opaca.
- **Mejoras cuantificadas:** Reducción del 31% en duración de violaciones de SLO, mejora del 24% en tiempo de respuesta al escalado y reducción del 18% en costos de infraestructura.
- **Características del marco:** Control seguro, explicable, multi-señal y auditable.

## Etiquetas
#Kubernetes #AIOps #EscaladoAutomático #SLO #OptimizaciónDeCostos

Fuente: http://arxiv.org/abs/2512.23415v1
