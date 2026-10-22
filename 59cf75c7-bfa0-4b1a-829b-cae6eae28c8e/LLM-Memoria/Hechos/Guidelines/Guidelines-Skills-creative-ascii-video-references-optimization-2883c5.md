---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/ascii-video/references/optimization.md"
tags: [hecho]
---
# optimization.md

## Resumen
Este documento establece una guía para optimizar el renderizado de videos ASCII detectando automáticamente la capacidad del hardware (CPU y RAM) del usuario. Su objetivo es ajustar dinámicamente parámetros como resolución, FPS, calidad de compresión y número de trabajadores para equilibrar rendimiento y resultados visuales sin necesidad de codificación manual.

## Datos clave
- **Detección de hardware**: El script calcula automáticamente el número de workers restando 1 o 2 núcleos del total para dejar margen al sistema operativo y a `ffmpeg`. También estima la memoria disponible en macOS, Linux y otros sistemas.
- **Perfiles de calidad**: Se definen presets (`draft`, `preview`, `production`, `max`) que modifican variables globales como `VW`, `VH`, `FPS` y `CRF`. El modo "auto" estima el tiempo de renderizado y degrada la calidad si supera una hora.
- **Integración CLI**: Se utilizan argumentos `--quality`, `--aspect`, `--workers` y `--resolution` para sobrescribir configuraciones automáticas.
- **Modo retrato**: Aunque tiene el mismo conteo de píxeles que el paisaje, requiere ajustes específicos en la densidad de la cuadrícula (columnas vs filas).

## Etiquetas
#optimización #renderizado #ascii-art #python #hardware-detection

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\ascii-video\references\optimization.md`
