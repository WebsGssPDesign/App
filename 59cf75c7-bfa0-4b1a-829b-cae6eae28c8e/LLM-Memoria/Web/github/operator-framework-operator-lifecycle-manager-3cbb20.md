---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/operator-framework/operator-lifecycle-manager"
tema: "Kubernetes Operator Lifecycle Manager"
tags: [web]
---
# operator-framework/operator-lifecycle-manager

## Resumen
El Operator Lifecycle Manager (OLM) es un componente del Operator Framework diseñado para gestionar de forma declarativa la instalación, actualización y dependencia de Operadores en Kubernetes. Actualmente, esta versión v0 se encuentra en modo mantenimiento mientras se desarrolla una nueva arquitectura v1.

## Datos clave
- **Estado:** Versión 0 en modo mantenimiento (sin nuevas características); repositorio principal nuevo: `operator-controller`.
- **Funciones principales:** Gestión de catálogos para actualizaciones over-the-air, modelo de dependencias entre Operadores, descubrimiento de servicios y estabilidad del cluster evitando conflictos de APIs.
- **Requisitos técnicos:** Git, Go v1.12+, Docker 17.03+ (o Podman/Buildah), kubectl v1.11.3+ y Kubernetes v1.11.3+.
- **Integración:** Permite crear interfaces gráficas para Operadores y facilita el empaquetado de aplicaciones existentes sin escribir código Go mediante `helm-app-operator-kit`.

## Etiquetas
#Kubernetes #OperatorLifecycleManager #DevOps #ContainerManagement

Fuente: https://github.com/operator-framework/operator-lifecycle-manager
