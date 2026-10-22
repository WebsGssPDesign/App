---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/ascii-video/references/inputs.md"
tags: [hecho]
---
# inputs.md

## Resumen
Este documento detalla las fuentes de entrada para generar videos en ASCII, describiendo cómo extraer y analizar características de audio (como energía por banda y ritmo) y video (luminancia, bordes y movimiento). Su objetivo es convertir señales multimedia complejas en datos numéricos normalizados que controlan la densidad de caracteres y los colores del resultado visual.

## Datos clave
- **Audio**: Uso de `ffmpeg` para conversión a WAV; análisis FFT con ventanas Hanning; características como RMS, centroid, flux y detección de beats mediante picos en el flujo.
- **Video**: Extracción de frames vía `ffmpeg` (tubo) o OpenCV; mapeo de luminancia a caracteres ASCII; detección de bordes usando diferencias simples entre píxeles adyacentes.
- **Procesamiento**: Aplicación de promedios móviles exponenciales (EMA) para suavizar características lentas y rápidas; normalización final de todos los datos al rango 0-1.
- **Lógica visual**: Uso de caracteres distintos para regiones con bordes versus áreas planas basándose en la detección de gradientes.

## Etiquetas
#ascii-art #procesamiento-audio #extraccion-video #analisis-de-senales

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\ascii-video\references\inputs.md`
