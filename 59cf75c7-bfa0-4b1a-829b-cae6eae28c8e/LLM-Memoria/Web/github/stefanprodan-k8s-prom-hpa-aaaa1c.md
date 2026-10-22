---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/stefanprodan/k8s-prom-hpa"
tema: "Kubernetes HPA"
tags: [web]
---
# stefanprodan/k8s-prom-hpa

## Resumen
Este documento describe la configuración de un Horizontal Pod Autoscaler (HPA) en Kubernetes que utiliza métricas personalizadas de Prometheus, además de las métricas estándar de CPU y memoria. Se explica cómo instalar el servidor de métricas para obtener datos básicos y cómo integrar una aplicación de demostración con el controlador HPA mediante la API de agregadores.

## Datos clave
- **Herramientas**: Kubernetes Metrics Server (sucesor de Heapster), Prometheus, Aggregation Layer.
- **Comandos principales**: `kubectl create -f ./metrics-server`, `kubectl get --raw "/apis/metrics.k8s.io/v1beta1/nodes"`.
- **Métricas de ejemplo**: Escalado automático basado en CPU (umbral 80%) y memoria (200Mi).
- **Aplicación de prueba**: `podinfo` desplegada con un HPA que escala entre 2 y 10 réplicas.
- **Carga de prueba**: Uso de la herramienta `hey` para simular tráfico y disparar el escalado.

## Etiquetas
#kubernetes #autoscaling #prometheus #devops #cloud-native

Fuente: https://github.com/stefanprodan/k8s-prom-hpa
