---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/ExpediaGroup/kubernetes-sidecar-injector"
tema: "Kubernetes Sidecar Injectors"
tags: [web]
---
# ExpediaGroup/kubernetes-sidecar-injector

## Resumen
Este proyecto es un webhook de mutación para Kubernetes diseñado para inyectar contenedores sidecar en los pods. Permite a las aplicaciones acceder a estos sidecars únicamente dentro de su propio espacio de nombres y ofrece dos métodos principales para la implementación: Helm o kubectl.

## Datos clave
- **Mecanismo**: Webhook de mutación (`mutating webhook`).
- **Comandos de instalación**: `make helm-install`, `helm repo add`.
- **Anotación requerida**: `sidecar-injector.expedia.com/inject` para activar la inyección en el spec del pod.
- **Restricción de alcance**: Los sidecars solo son accesibles dentro del mismo namespace que la aplicación.
- **Configuración**: Se define mediante un `ConfigMap` con una clave `sidecars.yaml`.
- **Espacios excluidos por defecto**: `kube-system` y `kube-public`.

## Etiquetas
#Kubernetes #Sidecar #Webhook #DevOps #Infraestructura

Fuente: https://github.com/ExpediaGroup/kubernetes-sidecar-injector
