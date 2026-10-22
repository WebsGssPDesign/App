---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/popular-web-designs/templates/vercel.md"
tags: [hecho]
---
# vercel.md

## Resumen
Este documento define el sistema de diseño "Geist" de Vercel, centrado en una estética minimalista y técnica que utiliza sombras para simular bordes y fuentes personalizadas con espaciado negativo agresivo. Su propósito es guiar la implementación visual precisa del sitio web, asegurando coherencia entre tipografía, paleta de colores y efectos de profundidad mediante especificaciones detalladas.

## Datos clave
- **Tipografía:** Fuentes `Geist` (Sans) y `Geist Mono` vía CDN; espaciado negativo extremo (-2.4px a -2.88px) en títulos.
- **Técnica de bordes:** Uso exclusivo de `box-shadow: 0px 0px 0px 1px rgba(0,0,0,0.08)` para reemplazar bordes CSS tradicionales.
- **Paleta de colores:** Fondo blanco puro (`#ffffff`), texto casi negro (`#171717`) y acentos de flujo de trabajo (Ship Red `#ff5b4f`, Preview Pink `#de1d8d`, Develop Blue `#0a72ef`).
- **Herramientas:** Generación de HTML con `write_file`, servicio vía `generative-widgets` y verificación visual con `browser_vision`.

## Etiquetas
#DiseñoDeSistemas #Vercel #GeistUI

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\popular-web-designs\templates\vercel.md`
