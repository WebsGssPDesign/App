---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/ninlil/kubectl-vpa"
tema: "Kubernetes Vertical Pod Autoscaler"
tags: [web]
---
# ninlil/kubectl-vpa

## Resumen
kubectl-vpa es una herramienta de línea de comandos diseñada para gestionar recursos VerticalPodAutoscaler (VPA) en clústeres de Kubernetes. Facilita tareas como la creación, comparación y modificación del modo de actualización de estos autoscalers, además de sugerir límites de recursos.

## Datos clave
- **Instalación**: `go install github.com/ninlil/kubectl-vpa` o uso como plugin (`kubectl vpa ...`).
- **Creación automática**: `kubectl-vpa compare -A -! -b | kubectl-vpa create -f - | kubectl apply -f -`.
- **Comandos principales**:
  - `create <namespace>/<nombre>`: Genera el recurso VPA para un Pod, Deployment, DaemonSet, StatefulSet o CronJob.
  - `mode <modo> ...`: Cambia la configuración de `UpdateMode` (ej. 'Initial').
  - `suggest <namespace>/<nombre>`: Propone snippets de límites para despliegues sin usar el módulo recomendador.
  - `compare [opciones]`: Compara las solicitudes actuales con los objetivos del VPA, mostrando diferencias en CPU y RAM.
- **Salida de compare**: Muestra columnas como Namespace, Name, Mode, Req-CPU, VPA-CPU, CPU diff%, Req-RAM, VPA-RAM y Mem. diff%.

## Etiquetas
#Kubernetes #VerticalPodAutoscaler #DevOps #Infraestructura

Fuente: https://github.com/ninlil/kubectl-vpa
