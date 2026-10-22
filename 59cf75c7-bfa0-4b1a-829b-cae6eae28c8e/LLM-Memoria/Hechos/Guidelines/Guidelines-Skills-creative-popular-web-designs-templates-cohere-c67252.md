---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/popular-web-designs/templates/cohere.md"
tags: [hecho]
---
# cohere.md

## Resumen
Este documento define el sistema de diseño "Cohere" para la interfaz del agente Hermes, orientado a un estilo empresarial limpio y profesional. Establece reglas estrictas sobre tipografía dual (serif para títulos y sans-serif para cuerpo), una paleta de colores minimalista basada en blanco y grises con acentos azules y púrpuras, y especificaciones técnicas para implementar fuentes mediante CDN.

## Datos clave
- **Tipografía:** Sustitutos de fuentes propietarias usando `Inter` (principal) y `JetBrains Mono` (monoespaciada) vía Google Fonts.
- **Estilo visual:** Tarjetas con radio de 22px, fondo blanco puro (`#ffffff`) y bordes grises fríos (`#d9d9dd`).
- **Paleta de colores:** Azul interactivo `#1863dc`, púrpura heroico oscuro y gradientes de pie de página.
- **Implementación:** Generar HTML con `write_file`, servir mediante `generative-widgets` (tunnel cloudflared) y validar visualmente con `browser_vision`.

## Etiquetas
#diseño-web #sistema-de-diseño #cohere #frontend

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\popular-web-designs\templates\cohere.md`
