---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://github.com/prometheus-operator/prometheus-operator"
tema: "Kubernetes Operators"
tags: [web]
---
# prometheus-operator/prometheus-operator

## Resumen
El Prometheus Operator es una herramienta nativa de Kubernetes diseñada para automatizar la configuración y gestión de clusters de monitoreo basados en Prometheus. Permite definir despliegues, políticas de retención y reglas de alerta mediante recursos personalizados, eliminando la necesidad de configurar manualmente el lenguaje específico de Prometheus. El proyecto está listo para producción, aunque sus versiones de API tienen distintos niveles de estabilidad.

## Datos clave
- **Requisito mínimo**: Kubernetes 1.16.0 o superior.
- **Recursos Personalizados (CRDs)**: `Prometheus`, `Alertmanager`, `ServiceMonitor`, `PodMonitor`, `Probe`, `ScrapeConfig`, `PrometheusRule` y `AlertmanagerConfig`.
- **Versiones de API**: `v1` (estable), `v1beta1` (inestable, uso con precaución) y `v1alpha1` (altamente inestable).
- **Funcionalidad principal**: Generación automática de configuraciones de *scraping* basada en etiquetas de Kubernetes.

## Etiquetas
#Prometheus #Kubernetes #Monitoreo #DevOps #Infraestructura

Fuente: https://github.com/prometheus-operator/prometheus-operator
