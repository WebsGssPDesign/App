---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/didier-durand/microservices-on-cloud-kubernetes"
tema: "Kubernetes Istio Sidecar"
tags: [web]
---
# didier-durand/microservices-on-cloud-kubernetes

## Resumen
Este repositorio proporciona una aplicación demostrativa de microservicios ("Online Boutique") desplegada automáticamente en un clúster Kubernetes gestionado por Google (GKE). El proyecto facilita la exploración de arquitecturas cloud-native mediante el uso de una malla de servicios y herramientas de observabilidad preconfiguradas, permitiendo a los usuarios experimentar con infraestructura distribuida sin configuraciones manuales extensas.

## Datos clave
- **Aplicación**: Online Boutique (10 microservicios políglotos + frontend).
- **Plataforma**: Google Kubernetes Engine (GKE).
- **Malla de servicios**: Implementada para gestión del tráfico y observabilidad.
- **Generador de carga**: Incluye un componente integrado (`loadgenerator`) que simula tráfico real; también se sugieren herramientas externas como `hey` o `fortio`.
- **Comandos útiles**: `kubectl get service frontend-external`, `kubectl logs -l app=loadgenerator -c main`.
- **Automatización**: GitHub Actions despliega el clúster y la aplicación con un solo clic o mediante cron recurrente.
- **Licencia**: Apache 2.0 (permite uso libre).

## Etiquetas
#kubernetes #microservicios #cloud-native #gke #observabilidad

Fuente: https://github.com/didier-durand/microservices-on-cloud-kubernetes
