---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/p5js/references/export-pipeline.md"
tags: [hecho]
---
# export-pipeline.md

## Resumen
Este documento detalla las mejores prácticas para exportar arte generativo y animaciones creadas con p5.js, cubriendo formatos estáticos como PNG y GIF, secuencias de imágenes y la creación de videos MP4. Su objetivo es guiar al desarrollador en la configuración técnica adecuada para garantizar una alta calidad visual, evitar artefactos de compresión y manejar flujos de trabajo complejos de renderizado por lotes o multi-cena.

## Datos clave
- **Exportación PNG:** Uso de `saveCanvas()` con atajos de teclado; generación de imágenes de alta resolución mediante buffers offscreen (`createGraphics`) y escalado; exportación determinista usando `noLoop()` + `redraw()` para captura precisa sin bucles automáticos.
- **Exportación GIF:** Limitaciones a 256 colores y tamaños grandes; recomendación de usar canvas pequeños (640x360) y framerate estándar de 15 fps con `saveGif()`.
- **Secuencias y Video:** Generación de frames individuales con `saveFrames()` o lógica manual para luego convertirlos a MP4 usando `ffmpeg` con codificación H.264 (`libx264`) y formato YUV420p.
- **Optimización de video:** Solución al problema del recorte de valores oscuros en YUV420 (mantener brillo mínimo ~10); uso de transiciones suaves (fade envelopes) para evitar cortes duros entre escenas; arquitectura modular por escena para facilitar el re-renderizado.

## Etiquetas
#p5js #exportación #video #ffmpeg #generativo

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\p5js\references\export-pipeline.md`
