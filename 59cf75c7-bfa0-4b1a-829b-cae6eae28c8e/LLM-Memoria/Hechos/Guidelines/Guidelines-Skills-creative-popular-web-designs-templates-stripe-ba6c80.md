---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/popular-web-designs/templates/stripe.md"
tags: [hecho]
---
# stripe.md

## Resumen
Este documento define el sistema de diseño visual de Stripe, detallando su paleta de colores, tipografía personalizada y efectos de sombra para lograr una estética fintech premium. Sirve como guía técnica para replicar la identidad de marca en entornos web autocontenidos utilizando fuentes CDN y estilos CSS específicos.

## Datos clave
- **Tipografía:** Sustitución de `sohne-var` por `Source Sans 3` (principal) y `Source Code Pro` (mono). Uso obligatorio del conjunto estilístico OpenType `"ss01"` con peso 300 para titulares.
- **Colores primarios:** Púrpura marca (`#533afd`), Azul marino profundo (`#061b31`) y Blanco puro (`#ffffff`).
- **Sombras:** Sistema multicapa con tinte azul (`rgba(50,50,93,0.25)`) para elevar elementos sin perder coherencia de marca.
- **Acentos:** Rojo rubí (`#ea2261`) y magenta (`#f96bee`) para degradados e iconos.
- **Implementación:** Generar HTML vía `write_file`, servir mediante `generative-widgets` (túnel cloudflared) y validar con `browser_vision`.

## Etiquetas
#Stripe #DesignSystem #UIUX #Fintech

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\popular-web-designs\templates\stripe.md`
