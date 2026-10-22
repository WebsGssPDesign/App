---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/comfyui/references/workflow-format.md"
tags: [hecho]
---
# workflow-format.md

## Resumen
Este documento define el formato JSON de la API para flujos de trabajo de ComfyUI, diferenciándolo del formato visual no ejecutable. Sirve como guía técnica para scripts que inyectan parámetros en nodos específicos (como prompts o configuraciones de muestreo) y detalla cómo identificar dependencias como modelos y embeddings.

## Datos clave
- **Formato API**: Estructura jerárquica donde las claves son IDs de nodo y los valores contienen `class_type` e `inputs`.
- **Detección**: El formato API se identifica por la presencia de `class_type`; el formato editor tiene arrays `nodes[]` y `links[]`.
- **Inyección de parámetros**: Los scripts deben modificar solo campos literales (ej. `text`, `seed`) y nunca sobrescribir enlaces (`["id", slot]`).
- **Nodos críticos**: Se listan clases para prompts (`CLIPTextEncode`), muestreo (`KSampler`), carga de modelos (`CheckpointLoaderSimple`) y video (`VHS_VideoCombine`).
- **Embeddings**: El sistema extrae referencias `embedding:NAME` dentro del texto del prompt como dependencias.
- **Herramientas**: `scripts/extract_schema.py` descubre parámetros automatizados para `run_workflow.py`.

## Etiquetas
#ComfyUI #FlujosDeTrabajo #GeneraciónDeImágenes #API

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\comfyui\references\workflow-format.md`
