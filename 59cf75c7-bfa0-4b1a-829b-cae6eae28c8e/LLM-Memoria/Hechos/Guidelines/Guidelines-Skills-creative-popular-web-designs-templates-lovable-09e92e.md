---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/popular-web-designs/templates/lovable.md"
tags: [hecho]
---
# lovable.md

## Resumen
Este documento define el sistema de diseño visual para la web de Lovable, centrado en una estética cálida y analógica que evita el blanco clínico típico. Establece reglas estrictas para tipografía, paleta de colores basada en opacidad y componentes UI utilizando tecnologías como Tailwind CSS y Radix UI. Su objetivo es guiar a los desarrolladores para replicar fielmente la atmósfera editorial y humana del sitio original mediante sustitutos de fuentes y configuraciones específicas de estilo.

## Datos clave
- **Proyecto:** Design System Lovable (Hermes Agent).
- **Tecnologías:** Tailwind CSS, Radix UI, shadcn/ui, `generative-widgets`, `browser_vision`.
- **Decisiones de diseño:** Fondo crema (`#f7f4ed`) en lugar de blanco; uso exclusivo de opacidad para la escala de grises derivada del color carbón (`#1c1c1c`); bordes redondeados completos (`9999px`).
- **Tipografía:** Fuente principal "Camera Plain Variable" con sustitutos CDN (DM Sans) y pila mono (`system monospace stack`).
- **Comandos/Pasos:** Usar `write_file` para generar HTML, servir mediante túnel cloudflared y verificar visualmente con `browser_vision`.

## Etiquetas
#design-system #ui-ux #frontend #tailwindcss #typography

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\popular-web-designs\templates\lovable.md`
