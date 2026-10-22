---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/thangchung/shopping-cart-k8s"
tema: "Kubernetes Service Mesh Patterns"
tags: [web]
---
# thangchung/shopping-cart-k8s

## Resumen
Este documento presenta una guía para construir una aplicación de carrito de compras basada en microservicios utilizando Kubernetes e Istio. Incluye instrucciones detalladas para configurar el entorno local con Hyper-V o VirtualBox, instalar componentes como Ambassador y Helm, y desplegar los servicios mediante comandos específicos.

## Datos clave
- **Stack tecnológico**: Kubernetes (v1.9/v1.10), Istio, Ambassador, Docker, .NET Core, NodeJS.
- **Comandos de instalación**: `minikube start --vm-driver=hyperv`, `kubectl create -f install/kubernetes/istio.yaml`.
- **Gestión de paquetes**: Helm (`helm init`, `helm install`).
- **Acceso a servicios**: Port-forwarding para RabbitMQ (`kubectl port-forward <pod> 15672`) y uso de URLs virtuales (xip.io/nip.io).

## Etiquetas
#microservicios #kubernetes #istio #devops #shopping-cart

Fuente: https://github.com/thangchung/shopping-cart-k8s
