---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/k8s-operatorhub/community-operators"
tema: "Kubernetes Operator Lifecycle Manager"
tags: [web]
---
# k8s-operatorhub/community-operators

## Resumen
Este repositorio es la fuente canónica para los Operadores de Kubernetes que se publican en OperatorHub.io y forman parte del catálogo predeterminado del Operator Lifecycle Manager (OLM). Las soluciones aquí integradas se distribuyen mediante un índice catalogado en Quay.io, permitiendo a los usuarios instalarlas en cualquier cluster Kubernetes o plataforma como OpenShift.

## Datos clave
- **Repositorio**: `k8s-operatorhub/community-operators`
- **Catálogo de distribución**: `quay.io/operatorhubio/catalog`
- **Instalación**: Se realiza agregando una nueva `CatalogSource` apuntando al índice anterior en el cluster.
- **Advertencia de versiones**: Las API versiones eliminadas en Kubernetes 1.22/1.25/1.26 y OpenShift 4.9/4.12/4.13 pueden causar fallos; los desarrolladores deben verificar compatibilidad usando `spec.minKubeVersion` y la anotación `operatorhub.io/ui-metadata-max-k8s-version`.
- **Documentación**: Generada con mkdocs en `https://k8s-operatorhub.github.io/community-operators/`.

## Etiquetas
#Kubernetes #Operators #OLM #DevOps

Fuente: https://github.com/k8s-operatorhub/community-operators
