---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/yannh/kubeconform"
tema: "Kubernetes Custom Resources"
tags: [web]
---
# yannh/kubeconform

## Resumen
Kubeconform es una herramienta de validación rápida para manifiestos de Kubernetes, diseñada para integrarse en flujos de CI o usarse localmente. Aunque inspirada en Kubeval, ofrece mayor rendimiento y soporte nativo para recursos personalizados (CRDs) mediante esquemas actualizados.

## Datos clave
- **Rendimiento**: Valida archivos en múltiples rutinas con caché en memoria; es significativamente más rápido que Kubeval en conjuntos grandes de manifiestos.
- **Limitaciones**: Solo valida contra especificaciones OpenAPI oficiales y no cubre validaciones adicionales del servidor (server-side).
- **Instalación**: Disponible vía Homebrew (`brew install kubeconform`), winget para Windows, descargas directas o `go install`.
- **Comandos principales**: `-ignore-missing-schemas` (ignora archivos sin esquemas), `-exit-on-error` (detiene ejecución al primer error), `-cache` (ruta para caché de esquemas).
- **Integración CI**: Soporta GitHub Actions y GitLab CI.

## Etiquetas
#Kubernetes #DevOps #CI_CD #Validación #Go

Fuente: https://github.com/yannh/kubeconform
