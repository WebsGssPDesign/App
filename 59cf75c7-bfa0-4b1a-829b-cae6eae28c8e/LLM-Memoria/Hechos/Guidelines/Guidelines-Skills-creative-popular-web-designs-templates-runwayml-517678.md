---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/popular-web-designs/templates/runwayml.md"
tags: [hecho]
---
# runwayml.md

## Resumen
Este documento define el sistema de diseño visual para Runway, orientado a una estética cinematográfica donde la fotografía y el video son los elementos principales de la interfaz. Establece reglas estrictas para tipografía monocromática, paleta de colores oscuros y un diseño minimalista que prioriza el contenido generado por IA sobre los elementos gráficos tradicionales.

## Datos clave
- **Proyecto:** Hermes Agent (implementación del sitio web).
- **Tecnologías:** HTML autocontenido con fuentes CDN (`Inter` como sustituto de `abcNormal`), Tailwind CSS, `generative-widgets`, `browser_vision`.
- **Decisiones de diseño:** Uso exclusivo de una fuente geométrica sin sombras ni bordes visibles; paleta basada en negros profundos y grises fríos.
- **Tipografía:** Altura de línea 1.0 para titulares con espaciado negativo (-0.9px a -1.2px); peso 450 para texto pequeño mayúscula.
- **Paleta de colores:** Fondos `#000000` y `#1a1a1a`; textos secundarios en tonos pizarra (`#767d88`, `#7d848e`).
- **Comandos/Flujo:** Generar HTML -> Servir vía túnel cloudflared -> Verificar visualmente con visión del navegador.

## Etiquetas
#design-system #ui-ux #runwayml #typography

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\popular-web-designs\templates\runwayml.md`
