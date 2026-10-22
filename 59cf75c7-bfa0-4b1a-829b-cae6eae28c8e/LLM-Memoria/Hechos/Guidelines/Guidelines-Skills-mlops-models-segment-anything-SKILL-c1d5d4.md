---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/mlops/models/segment-anything/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía técnica documenta el uso del modelo Segment Anything (SAM) de Meta AI para realizar segmentación de imágenes sin necesidad de entrenamiento previo. Permite a los desarrolladores generar máscaras precisas utilizando prompts flexibles como puntos, cajas o máscaras anteriores, siendo ideal para herramientas interactivas y generación de datos.

## Datos clave
- **Proyecto**: Segment Anything Model (SAM) por Meta AI.
- **Tecnologías**: Python, PyTorch, HuggingFace Transformers, ONNX.
- **Decisiones**: Se ofrecen tres variantes según precisión/velocidad: ViT-H (2.4GB), ViT-L (1.2GB) y ViT-B (375MB).
- **Rutas de descarga**: Archivos `.pth` disponibles en `dl.fbaipublicfiles.com`.
- **Comandos importantes**: `pip install git+https://github.com/facebookresearch/segment-anything.git`, `wget [URL_checkpoint]`.
- **Pasos clave**: Cargar modelo con `SamPredictor`, establecer imagen (`set_image`) y predecir con coordenadas de puntos o cajas.

## Etiquetas
#SAM #ComputerVision #ZeroShotSegmentation #MLOps

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\mlops\models\segment-anything\SKILL.md`
