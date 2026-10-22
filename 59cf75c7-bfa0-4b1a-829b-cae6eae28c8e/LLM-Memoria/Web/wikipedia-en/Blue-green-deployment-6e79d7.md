---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Blue%E2%80%93green_deployment"
tema: "Kubernetes Operator Lifecycle Manager"
tags: [web]
---
# Blue–green deployment

## Resumen
El despliegue azul-verde es una técnica de ingeniería de software que utiliza dos entornos idénticos (uno activo y otro en espera) para actualizar aplicaciones web o servidores. Al mantener un entorno inactivo para pruebas, este método permite realizar cambios con tiempos de inactividad mínimos y facilita una reversión rápida ante fallos.

## Datos clave
- **Mecanismo**: Se alternan dos servidores ("azul" activo y "verde" en espera) mediante redirección de tráfico (DNS).
- **Ventajas principales**: Reducción del tiempo de inactividad, capacidad inmediata de rollback al volver el tráfico al servidor anterior.
- **Desafíos**: Requiere mantener infraestructura duplicada simultáneamente; las migraciones complejas de bases de datos deben garantizar consistencia entre ambos entornos.
- **Herramientas mencionadas**: AWS CodeDeploy, Kubernetes (con ArgoCD o Spinnaker), Google Cloud Deployment Manager y Azure Container Apps.
- **Origen del término**: Popularizado por Dan North y Jez Humble alrededor de 2005 en el libro *Continuous Delivery*.

## Etiquetas
#despliegue #DevOps #InfraestructuraCloud #AWS #Kubernetes

Fuente: https://en.wikipedia.org/wiki/Blue%E2%80%93green_deployment
