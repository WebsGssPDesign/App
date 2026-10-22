---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/operator-framework/operator-sdk"
tema: "Kubernetes Operator SDK"
tags: [web]
---
# operator-framework/operator-sdk

## Resumen
El Operator SDK es un marco de trabajo para desarrollar aplicaciones nativas de Kubernetes (Operators) que simplifica la escritura mediante APIs de alto nivel y herramientas de generación de código. El proyecto forma parte del Operator Framework y depende de la librería controller-runtime para abstraer la lógica operativa compleja.

## Datos clave
- **Funcionalidad principal**: Proporciona abstracciones, APIs intuitivas y andamiaje (scaffolding) para crear Operators rápidamente.
- **Dependencia crítica**: Utiliza la librería `controller-runtime` de Kubernetes SIGs.
- **Licencia**: Apache 2.0.
- **Advertencia importante**: Las imágenes en `gcr.io/kubebuilder/`, específicamente `kube-rbac-proxy`, dejarán de estar disponibles pronto (inicios de 2025). Se recomienda migrar a la autenticación y autorización nativa de Controller Runtime (`WithAuthenticationAndAuthorization`).
- **Soporte**: Binarios construidos con Go, compatibilidad con múltiples versiones de Kubernetes y plataformas específicas.

## Etiquetas
#Kubernetes #DevOps #Go #OperatorSDK #CloudNative

Fuente: https://github.com/operator-framework/operator-sdk
