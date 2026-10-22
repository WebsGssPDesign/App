---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/zalando-incubator/kube-metrics-adapter"
tema: "Kubernetes HPA"
tags: [web]
---
# zalando-incubator/kube-metrics-adapter

## Resumen
El adaptador de métricas de Kubernetes es una herramienta general diseñada para recopilar y servir métricas personalizadas o externas, facilitando el escalado automático de aplicaciones mediante Horizontal Pod Autoscaling (HPA). Soporta nativamente fuentes como Prometheus y colas SQS, permitiendo configurar recolectores específicos a través de anotaciones en los recursos HPA.

## Datos clave
- **Función principal**: Adaptador de métricas para HPA que almacena datos en memoria usando la librería `custom-metrics-apiserver`.
- **Requisitos de compilación**: Go >= 1.11 con soporte a módulos (`GO111MODULE=on`).
- **Compatibilidad**: Soporta las tres últimas versiones menores de Kubernetes; API por defecto es `autoscaling/v2` (desde v1.23).
- **Instalación**: Clonar repositorio y ejecutar `kubectl apply -f .` desde la carpeta `docs`.
- **Recolector Pod**: Permite extraer métricas de cada pod seleccionado; actualmente soporta solo colección por `json-path`.
- **Objetos compatibles**: Deployment, StatefulSet y Rollout.
- **Configuración**: Se realiza mediante anotaciones tipo `metric-config.<tipo>.<nombre>.<recolector>/<clave>` (ej: `metric-config.pods.requests-per-second.json-path/json-key`).

## Etiquetas
#Kubernetes #HPA #Prometheus #DevOps #Infraestructura

Fuente: https://github.com/zalando-incubator/kube-metrics-adapter
