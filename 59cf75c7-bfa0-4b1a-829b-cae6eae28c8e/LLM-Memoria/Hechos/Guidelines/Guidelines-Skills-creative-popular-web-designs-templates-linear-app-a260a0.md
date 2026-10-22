---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/popular-web-designs/templates/linear.app.md"
tags: [hecho]
---
# linear.app.md

## Resumen
Este documento define el sistema de diseño visual de Linear, enfocado en un enfoque nativo de modo oscuro que utiliza una paleta casi monocromática con acentos violetas. Sirve como guía técnica para replicar la atmósfera de precisión y jerarquía luminosa del sitio web original mediante especificaciones detalladas de tipografía, colores y componentes.

## Datos clave
- **Tipografía:** Fuente `Inter Variable` (con características OpenType "cv01", "ss03") y monoespaciada `JetBrains Mono`. Peso distintivo 510 para UI. Espaciado negativo agresivo en títulos grandes (-1.584px a 72px).
- **Paleta de colores:** Fondo principal `#08090a`, texto primario `#f7f8f8` y acento de marca violeta (`#7170ff`). Bordes semitransparentes blancos (`rgba(255,255,255,0.05)`).
- **Componentes:** Uso de primitivos Radix UI. Botones con fondos de opacidad casi nula. Sombras multi-capa para profundidad.
- **Implementación:** Sustitución de fuentes propietarias vía CDN (Google Fonts) y generación de HTML usando la herramienta `write_file` verificada con `browser_vision`.

## Etiquetas
#diseño-web #modo-oscuro #sistema-de-diseño #linear

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\popular-web-designs\templates\linear.app.md`
