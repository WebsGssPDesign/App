---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/DNXLabs/terraform-aws-eks-metrics-server"
tema: "Kubernetes Vertical Pod Autoscaler"
tags: [web]
---
# DNXLabs/terraform-aws-eks-metrics-server

## Resumen
Este módulo de Terraform automatiza el despliegue del Kubernetes Metrics Server en entornos AWS EKS, permitiendo la recolección de métricas de recursos desde los nodos. Estas métricas se exponen a través de la API para habilitar la escalabilidad automática de las aplicaciones mediante Horizontal y Vertical Pod Autoscalers.

## Datos clave
- **Función principal**: Recoge métricas de recursos (CPU, memoria) desde Kubelets y las expone en el apiserver.
- **Compatibilidad**: Escalable hasta clústers con 5,000 nodos; consume ~1m CPU y 3 MB RAM por nodo.
- **Uso típico**: Requiere Terraform >= 0.13, AWS provider >= 3.13, Helm >= 1.0 y Kubernetes provider >= 1.10.0.
- **Configuración principal**: Se activa mediante el input `enabled = true` en la definición del módulo.
- **Repositorio de Helm por defecto**: `https://charts.bitnami.com/bitnami`.
- **Namespace predeterminado**: `kube-system`.

## Etiquetas
#Terraform #Kubernetes #AWS #EKS #MetricsServer #DevOps

Fuente: https://github.com/DNXLabs/terraform-aws-eks-metrics-server
