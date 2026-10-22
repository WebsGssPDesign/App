---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/artefactual-sdps/cva-enduro-workflows"
tema: "Temporal Child Workflows"
tags: [web]
---
# artefactual-sdps/cva-enduro-workflows

## Resumen
Este repositorio proporciona dos flujos de trabajo hijos para Enduro, diseñados específicamente para los Archivos de la Ciudad de Vancouver. Estos flujos automatizan procesos de preprocesamiento y post-lote, gestionando metadatos y preparando archivos para sistemas de preservación como Archivematica y AtoM mediante tareas coordinadas en Temporal.

## Datos clave
- **Flujo de preprocesamiento**: Verifica el ID del lote, sube `ContainerMetadata.xml` al bucket de ingestión y convierte los SIPs en bolsas BagIt usando checksums SHA512.
- **Flujo post-lote**: Genera un archivo CSV compatible con AtoM listando cada SIP del lote y limpia archivos temporales del bucket tras el procesamiento.
- **Configuración requerida**: El worker debe compartir sistema de archivos, conectarse al mismo servidor Temporal y usar la cola `cva-enduro`.
- **Entorno local**: Se desarrolla usando Go 1.26+, GNU Make/GCC y se ejecuta mediante `tilt up` en un entorno Kubernetes.
- **Comandos útiles**: `make help`, `make env DBG_MAKEFILE=1` para depuración, configuración vía variables de entorno como `CHILD_WORKFLOW_PATHS`.

## Etiquetas
#preservación #archivística #automatización #workflow #Enduro

Fuente: https://github.com/artefactual-sdps/cva-enduro-workflows
