---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/salesforce/generic-sidecar-injector"
tema: "Kubernetes Sidecar Injectors"
tags: [web]
---
# salesforce/generic-sidecar-injector

## Resumen
Este proyecto es un framework de código abierto para Kubernetes que facilita la inyección de sidecars, contenedores iniciales y volúmenes mediante controladores webhooks de admisión. Su objetivo principal es reducir la duplicación de código al permitir una configuración impulsada por archivos en lugar de requerir cambios en el código fuente.

## Datos clave
- **Comandos principales**: `make` para ejecutar pruebas, `make docker` para construir imágenes.
- **Archivos de configuración**: Requiere dos archivos: `sidecar-config-file` (define sidecars y volúmenes) y `mutation-config-file` (define reglas de inyección basadas en anotaciones).
- **Anotaciones críticas**: Se usan para activar la inyección (ej. `rsyslog.k8s-integration.sfdc.com/inject`) y pasar configuraciones dinámicas a los contenedores.
- **Componentes inyectables**: InitContainers, containers, volumes y volume mounts.

## Etiquetas
#kubernetes #sidecar-injection #mutating-webhook #devops #salesforce

Fuente: https://github.com/salesforce/generic-sidecar-injector
