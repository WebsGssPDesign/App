---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2103.04273v2"
tema: "gRPC Protobuf Reflection"
tags: [web]
---
# Robust Reflection Removal with Reflection-free Flash-only Cues

## Resumen
Los autores proponen un método robusto para eliminar reflejos utilizando una señal libre de reflejos obtenida exclusivamente con destellos. Esta técnica resta la imagen ambiental a la imagen con flash en el espacio de datos crudos, asumiendo que el resultado es equivalente a una toma en un entorno oscuro y sin reflejos. Para evitar los artefactos inherentes a esta operación, se desarrolla un modelo dedicado que estima con precisión la reflexión y la transmisión.

## Datos clave
- **Cue libre de reflejos**: Imagen resultante de restar la imagen ambiental (sin flash) de la imagen con flash en datos crudos.
- **Equivalencia visual**: La imagen "flash-only" se comporta como una toma realizada en un entorno oscuro, lo que permite inferir los reflejos presentes en la imagen ambiental original.
- **Mejoras métricas**: El modelo supera a las técnicas state-of-the-art con más de 5.23dB en PSNR, 0.04 en SSIM y reduce LPIPS en 0.068.
- **Disponibilidad pública**: El código fuente y el conjunto de datos están alojados en GitHub bajo el repositorio `ChenyangLEI/flash-reflection-removal`.

## Etiquetas
#eliminación_de_reflejos #visión_por_computador #procesamiento_de_imágenes #destellos #arXiv

Fuente: http://arxiv.org/abs/2103.04273v2
