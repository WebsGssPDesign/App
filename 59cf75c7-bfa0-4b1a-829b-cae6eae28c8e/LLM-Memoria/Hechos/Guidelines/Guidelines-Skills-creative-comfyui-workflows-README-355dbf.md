---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/comfyui/workflows/README.md"
tags: [hecho]
---
# README.md

## Resumen
Este documento describe flujos de trabajo API para ComfyUI diseñados para tareas comunes como generación de imágenes, inpainting y video. Sirven como punto de partida listos para ejecutarse localmente o en la nube mediante un script Python, especificando los modelos requeridos y el consumo mínimo de VRAM.

## Datos clave
- **Flujos disponibles**: Text-to-image (SD1.5, SDXL, Flux Dev), image-to-image, inpainting, escalado 4x ESRGAN y generación de video (AnimateDiff, Wan 2.x).
- **Requisitos de hardware**: Desde 4 GB hasta 24 GB de VRAM según el modelo; Flux Dev requiere optimización FP8 para reducir la carga.
- **Comandos principales**: `python3 ../scripts/run_workflow.py` con argumentos JSON para prompts y parámetros; `check_deps.py` para validar instalaciones.
- **Notas técnicas**: Los archivos JSON están en formato API (no editor); las máscaras de inpainting usan el canal rojo por defecto; los trabajos de video tienen un tiempo de espera extendido automático.

## Etiquetas
#ComfyUI #GeneraciónDeImágenes #FlujosDeTrabajo #IA

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\comfyui\workflows\README.md`
