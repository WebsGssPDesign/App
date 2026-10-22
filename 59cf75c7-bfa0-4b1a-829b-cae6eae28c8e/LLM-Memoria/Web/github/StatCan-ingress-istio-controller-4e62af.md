---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/StatCan/ingress-istio-controller"
tema: "Kubernetes Istio VirtualServices"
tags: [web]
---
# StatCan/ingress-istio-controller

## Resumen
Este repositorio contiene un controlador reescrito para Istio que genera y configura objetos `VirtualService` a partir de recursos `Ingress` de Kubernetes. La implementación fue necesaria debido a cambios en la lógica interna de Istio 1.6, donde cada servicio recibe su propia puerta de enlace en lugar de una única, lo cual causaba problemas con certificados comodín en la plataforma de Statistics Canada.

## Datos clave
- **Función principal**: Traduce `Ingress` a `VirtualService` y enruta el tráfico mediante un `Gateway`.
- **Motivo del reescritado**: Adaptarse a Istio 1.6+ donde se requiere un Gateway por VirtualService para compatibilidad con certificados comodín.
- **APIs compatibles**: `istio.io/api/networking/v1beta1` y `k8s.io/api/networking/v1`.
- **Versiones probadas**: Istio 1.5, 1.6, 1.7; Kubernetes 1.17, 1.18, 1.19.
- **Identificación de Ingress**: A través de la anotación `kubernetes.io/ingress.class` (prioritaria) o el recurso `IngressClass` con controlador `ingress.statcan.gc.ca/ingress-istio-controller`.
- **Instalación**: Disponible vía Helm Chart y Docker Image.
- **Licencia**: MIT (Copyright del Gobierno de Canadá).

## Etiquetas
#Istio #Kubernetes #Ingress #VirtualService #Networking

Fuente: https://github.com/StatCan/ingress-istio-controller
