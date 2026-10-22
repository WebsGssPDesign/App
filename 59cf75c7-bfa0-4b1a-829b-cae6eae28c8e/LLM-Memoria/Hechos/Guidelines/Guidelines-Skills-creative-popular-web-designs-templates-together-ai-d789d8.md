---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/popular-web-designs/templates/together.ai.md"
tags: [hecho]
---
# together.ai.md

## Resumen
Este documento define el sistema de diseño visual para Together AI, orientado a crear una interfaz que equilibre la infraestructura técnica con un estilo optimista y accesible. Sirve como guía para replicar fielmente la atmósfera "AI-Native Cloud" mediante una paleta de colores específica, reglas tipográficas estrictas y el uso de gradientes suaves contrastados con secciones oscuras para contenido técnico.

## Datos clave
- **Tipografía:** Fuentes primarias `Inter` (fallback a `The Future`) y monoespaciada `JetBrains Mono` (fallback a `PP Neue Montreal Mono`). Se requiere usar CDN de Google Fonts para evitar dependencias locales.
- **Paleta de colores:** Magenta (`#ef2cc1`) y naranja (`#fc4c02`) como acentos; azul medianoche (`#010120`) para secciones oscuras; gradientes pastel (rosa, lavanda, azul) sobre blanco puro.
- **Reglas tipográficas:** Uso agresivo de espaciado negativo en títulos (ej: `-1.92px` para el hero a 64px) y geometría angular (radio de 4px/8px), evitando bordes redondeados tipo píldora.
- **Flujo de trabajo:** Generar HTML con `write_file`, servir mediante `generative-widgets` usando un túnel `cloudflared`, y validar la fidelidad visual con `browser_vision`.

## Etiquetas
#design-system #ui-ux #ai-infrastructure #typography

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\popular-web-designs\templates\together.ai.md`
