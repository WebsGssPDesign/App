---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/popular-web-designs/templates/miro.md"
tags: [hecho]
---
# miro.md

## Resumen
Esta guía define el sistema de diseño visual de la plataforma Miro para agentes de desarrollo, especificando una estética limpia basada en tipografía Roobert PRO y Noto Sans. Su objetivo es permitir la recreación fiel del sitio web utilizando fuentes CDN como sustitutos de las propietarias y definiendo reglas estrictas de color, espaciado y componentes.

## Datos clave
- **Tipografía:** Sustituto `Inter` (CDN) para pantallas; `Roobert PRO Medium` con variantes OpenType (`blwf`, `cv03`) para diseño original. Cuerpo en `Noto Sans`.
- **Paleta de colores:** Fondo blanco (`#ffffff`), texto casi negro (`#1c1c1e`), interactivo azul 450 (`#5b76fe`). Acentos pastel: coral, rose, teal, orange, yellow, moss.
- **Componentes:** Botones con borde fino (`#c7cad5`) y radio de 8px; tarjetas con fondos pastel (radio 12–24px); sombras tipo anillo en lugar de sombras pesadas.
- **Implementación:** Usar `write_file` para generar HTML, servir vía `generative-widgets` y verificar visualmente con `browser_vision`.
- **Restricciones:** No usar más de dos acentos pastel por sección; evitar sombras fuertes; respetar jerarquía tipográfica específica (ej. espaciado negativo en títulos).

## Etiquetas
#design-system #ui-guidelines #web-development #miro

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\popular-web-designs\templates\miro.md`
