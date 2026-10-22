---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/popular-web-designs/templates/clay.md"
tags: [hecho]
---
# clay.md

## Resumen
Este documento define el sistema de diseño "Clay" para la web de Hermes Agent, enfocándose en una estética cálida y artesanal que humaniza herramientas B2B. Sirve como guía técnica para replicar la identidad visual única mediante paletas de colores nombradas, tipografías específicas y micro-interacciones físicas.

## Datos clave
- **Tipografía:** Roobert (con 5 conjuntos OpenType) para textos principales y Space Mono para código; sustitutos CDN: DM Sans y system monospace stack.
- **Paleta de colores:** Fondo crema (`#faf9f7`) con bordes tono avena; acentos llamativos como Matcha, Slushie, Lemon, Ube, Pomegranate, Blueberry y Dragonfruit.
- **Animaciones:** Botones rotan -8 grados y se desplazan al subir 80% al pasar el cursor, generando una sombra dura de desplazamiento.
- **Sombras:** Sistema multicapa con resalte interior (`inset`) y sombras duras para estados hover.
- **Flujo de trabajo:** Generar HTML con `write_file`, servir vía `generative-widgets` (túnel cloudflared) y verificar visualmente con `browser_vision`.

## Etiquetas
#design-system #clay-theme #ui-design #frontend-development

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\popular-web-designs\templates\clay.md`
