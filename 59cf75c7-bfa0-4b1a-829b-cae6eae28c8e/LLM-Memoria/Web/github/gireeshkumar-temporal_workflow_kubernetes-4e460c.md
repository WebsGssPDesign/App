---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/gireeshkumar/temporal_workflow_kubernetes"
tema: "Temporal Child Workflows"
tags: [web]
---
# gireeshkumar/temporal_workflow_kubernetes

## Resumen
Este repositorio es una base de código de ejemplo que implementa workflows de Temporal utilizando Quarkus, Kotlin y Kubernetes. La arquitectura se basa en la gestión de workflows padre-hijo y actividades remotas o locales, orquestando todo mediante skaffold.dev para facilitar el desarrollo y despliegue en contenedores.

## Datos clave
- **Tecnologías**: Kotlin, Quarkus, Temporal, Kubernetes (Minikube), Docker, Gradle, Skaffold.
- **Conceptos principales**: Workflows padre-hijo (Parent-child workflows), actividades remotas y locales, ejecución asíncrona dinámica vs estática.
- **Pasos de implementación**:
  1. Configurar Temporal con Helm (`helm install temporaltest .`).
  2. Acceder a servicios mediante `kubectl port-forward`.
  3. Construir proyectos: `./gradlew build`.
  4. Desplegar imágenes y pods: `skaffold dev -p dev`.
  5. Ejecutar el cliente de prueba: `./gradlew :wf_client:run`.
- **Estructura**: Subproyectos independientes (Lib, Stringactions-wf, reverse, kebab, uppercase) con sus propias imágenes Docker.

## Etiquetas
#Temporal #Kotlin #Quarkus #Kubernetes #DevOps

Fuente: https://github.com/gireeshkumar/temporal_workflow_kubernetes
