---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/Just1B/kubernetes-istio-gateway"
tema: "Kubernetes Istio VirtualServices"
tags: [web]
---
# Just1B/kubernetes-istio-gateway

## Resumen
Este documento explica cómo configurar un Gateway de Istio y VirtualServices en Google Kubernetes Engine (GKE) para enrutar tráfico a dos servicios distintos mediante subdominios personalizados. El proceso implica crear un namespace, desplegar servidores de prueba y definir reglas de routing específicas sin depender de los objetos nativos de Ingress de Kubernetes.

## Datos clave
- **Requisitos**: Clúster online con Istio instalado.
- **Namespace**: `fruits` para alojar los servicios.
- **Servicios**: Dos instancias de `hashicorp/http-echo` (apple y banana).
- **Recursos Istio**: `Gateway`, `VirtualService`, `DestinationRule`.
- **Comandos principales**: `kubectl create namespace fruits`, `kubectl apply -f apple.yml/banana.yml/gateway.yml/virtual-service.yml`.
- **Configuración DNS**: Los subdominios deben apuntar al `EXTERNAL-IP` del servicio `istio-ingressgateway`.

## Etiquetas
#Kubernetes #Istio #Gateway #VirtualService #GKE

Fuente: https://github.com/Just1B/kubernetes-istio-gateway
