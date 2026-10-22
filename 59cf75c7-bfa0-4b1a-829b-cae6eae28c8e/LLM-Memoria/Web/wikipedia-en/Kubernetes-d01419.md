---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Kubernetes"
tema: "Kubernetes Operators"
tags: [web]
---
# Kubernetes

## Resumen
Kubernetes es un sistema de orquestación de contenedores de código abierto diseñado para automatizar el despliegue, escalado y gestión de aplicaciones. Desarrollado originalmente por Google y ahora mantenido por la Cloud Native Computing Foundation (CNCF), agrupa computadoras en clústeres que ejecutan cargas de trabajo mediante contenedores. La arquitectura se divide entre un plano de control que gestiona los recursos y nodos donde corren las aplicaciones reales.

## Datos clave
- **Origen**: Creado por Google (Joe Beda, Brendan Burns) inspirado en Borg; escrito en Go.
- **Nombre**: Viene del griego "kubernētēs" (timonel); abreviado como K8s (K + 8 letras + s).
- **Herramientas principales**: `kubectl` y `kubeadm` para interactuar con la API REST.
- **Componentes del plano de control**:
    - **Etcd**: Almacén distribuido clave-valor que guarda el estado del clúster (prioriza consistencia).
    - **API Server**: Interfaz JSON/HTTPS que valida solicitudes y actualiza el estado en Etcd.
    - **Scheduler**: Selecciona qué nodo debe ejecutar un "pod" no asignado.
- **Política de soporte**: Hasta v1.18 usaba política N-2 (3 versiones recientes); desde v1.19 usa N-3.

## Etiquetas
#Kubernetes #OrquestaciónDeContenedores #InfraestructuraCloud #DevOps #CNCF

Fuente: https://en.wikipedia.org/wiki/Kubernetes
