---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/popular-web-designs/templates/ibm.md"
tags: [hecho]
---
# ibm.md

## Resumen
Esta guía técnica define el sistema de diseño IBM basado en Carbon, estableciendo reglas estrictas para la tipografía (IBM Plex), una paleta monocromática con un único acento azul y un espaciado modular de 8px. Su objetivo es replicar la autoridad corporativa y la precisión ingenieril de IBM mediante tokens CSS semánticos y componentes sin bordes redondeados, permitiendo la creación de interfaces escalables y coherentes.

## Datos clave
- **Tipografía:** IBM Plex Sans (peso 300 para títulos, 400 para cuerpo) e IBM Plex Mono para código; espaciado de letras de 0.16px en textos pequeños.
- **Paleta de colores:** Fondo blanco (#ffffff), texto casi negro (#161616) y acento único IBM Blue 60 (#0f62fe).
- **Tokens CSS:** Uso obligatorio de variables `--cds-*` para estados interactivos, bordes y superficies.
- **Geometría:** Grid estricto de 8px; botones primarios con radio de borde 0px (rectangulares); tarjetas planas sin sombras.
- **Implementación:** Sustitución de fuentes propietarias vía CDN Google Fonts para HTML autocontenido; verificación visual con `browser_vision`.

## Etiquetas
#IBM #CarbonDesignSystem #UIPatterns #Typography

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\popular-web-designs\templates\ibm.md`
