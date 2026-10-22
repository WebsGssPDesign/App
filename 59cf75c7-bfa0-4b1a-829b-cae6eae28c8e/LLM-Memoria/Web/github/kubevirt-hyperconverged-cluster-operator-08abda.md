---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/kubevirt/hyperconverged-cluster-operator"
tema: "Kubernetes Operator Patterns"
tags: [web]
---
# kubevirt/hyperconverged-cluster-operator

## Resumen
El documento describe al Hyperconverged Cluster Operator (HCO), un patrón de operador diseñado para gestionar y desplegar conjuntamente KubeVirt junto con varios operadores auxiliares esenciales. Este componente permite una instalación unificada y controlada a través del Operator Lifecycle Manager (OLM) en entornos como OpenShift, generando los recursos personalizados necesarios para sus subcomponentes.

## Datos clave
- **Componentes gestionados**: KubeVirt, Containerized Data Importer, Scheduling Scale and Performance (SSP), Cluster Network Addons y Node Maintenance.
- **Instalación estándar**: Se realiza mediante `kustomize` ejecutando el script `deploy_kustomize.sh` hasta que la condición del recurso sea `Available`.
- **Comandos de construcción**: Requiere `opm` para generar imágenes personalizadas; comandos clave incluyen `make build-push-multi-arch-operator-image`, `build-manifests` y `hack/build-index-image.sh`.
- **Imágenes de catálogo**: La versión inestable más reciente se encuentra en `quay.io/kubevirt/hyperconverged-cluster-index:1.20.0-unstable`.
- **Instalación vía OLM**: Se crea un recurso `CatalogSource` apuntando a la imagen del índice para consumir el paquete de operadores.

## Etiquetas
#KubeVirt #HyperconvergedClusterOperator #OpenShiftOLM #DevOps

Fuente: https://github.com/kubevirt/hyperconverged-cluster-operator
