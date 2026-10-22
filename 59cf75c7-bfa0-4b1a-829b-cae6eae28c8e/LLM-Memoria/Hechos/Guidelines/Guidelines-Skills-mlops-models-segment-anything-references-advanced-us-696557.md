---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/mlops/models/segment-anything/references/advanced-usage.md"
tags: [hecho]
---
# advanced-usage.md

## Resumen
Este documento detalla guías avanzadas para utilizar Segment Anything (SAM) y SAM 2 en tareas de segmentación semántica. Explica cómo extender el modelo a videos con seguimiento temporal, integrar prompts de texto mediante Grounded SAM y optimizar el procesamiento masivo de imágenes mediante batching o servicios web.

## Datos clave
- **Proyectos**: Segment Anything 2 (SAM 2), Grounded SAM.
- **Tecnologías**: PyTorch, FastAPI, Hiera architecture, Streaming memory bank.
- **Decisiones**: Uso de `sam2_hiera_large.pt` para video y `vit_h` checkpoint para imágenes estáticas.
- **Rutas/Comandos**: Instalación vía pip desde repositorios GitHub (`segment-anything-2`, `groundingdino-py`).
- **Pasos importantes**: Inicialización del predictor con `init_state(video_path)`, propagación de máscaras mediante `propagate_in_video()`, y conversión de coordenadas normalizadas a píxeles para Grounded SAM.

## Etiquetas
#mlops #segmentation #sam2 #groundedsam

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\mlops\models\segment-anything\references\advanced-usage.md`
