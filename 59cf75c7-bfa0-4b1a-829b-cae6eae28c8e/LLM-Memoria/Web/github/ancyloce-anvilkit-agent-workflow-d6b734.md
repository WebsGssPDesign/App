---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/ancyloce/anvilkit-agent-workflow"
tema: "Temporal Workflow Cancellation"
tags: [web]
---
# ancyloce/anvilkit-agent-workflow

## Resumen
Este repositorio implementa el trabajador de flujo de trabajo (Workflow Worker) para la plataforma AnvilKit Agent utilizando Temporal Go SDK. Su función principal es orquestar la ejecución, validación y recuperación de trabajos mediante flujos fijos como LocalCheck y Recovery, delegando todas las decisiones de negocio al servicio Control sin exponer RPC públicos ni gestionar credenciales directamente.

## Datos clave
- **Componentes principales**: `LocalCheckWorkflow`, `RecoveryWorkflow` y actividades para control (ej. `OpenAttempt`) y lanzamiento de Kubernetes Jobs (`CreateJob`).
- **Arquitectura**: Usa Fx para ensamblaje, `koanf` para configuración y `client-go` para interacciones con Kubernetes.
- **Seguridad**: Los pods del lanzador no usan tokens ServiceAccount; las imágenes están fijadas por digest y los perfiles de seguridad se revisan estrictamente.
- **Configuración**: Se lee un archivo único (`config.yaml`) que define límites congelados en cada ejecución, incluyendo tiempos de vida (TTL) de arrendamientos y rutas de análisis.
- **Desarrollo**: Incluye adaptadores para gRPC Control, transferencia de artefactos Pagix y pruebas de integración contra clústeres reales.

## Etiquetas
#Temporal #Kubernetes #Orquestación #Go #AnvilKit

Fuente: https://github.com/ancyloce/anvilkit-agent-workflow
