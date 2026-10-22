---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/popular-web-designs/templates/sentry.md"
tags: [hecho]
---
# sentry.md

## Resumen
Este documento define el sistema de diseño visual para la interfaz web de Sentry, orientada a desarrolladores con un tema oscuro y estética de editor de código. Sirve como guía técnica para replicar fielmente la atmósfera de marca utilizando una paleta específica de púrpuras, verdes lima y tipografías personalizadas.

## Datos clave
- **Tipografía**: `Dammit Sans` (display), `Rubik` (UI principal) y `JetBrains Mono`/`Monaco` (código). Se sugieren sustitutos en CDN (`Google Fonts`) para evitar fuentes propietarias.
- **Paleta de colores**: Fondos púrpura-negro (`#1f1633`, `#150f23`), acentos vibrantes como verde lima (`#c2ef4e`) y rosa coral (`#fa7faa`).
- **Estilo visual**: Botones con sombras internas (inset) para efecto táctil, efectos de vidrio esmerilado (`blur(18px)`) y jerarquía tipográfica estricta.
- **Implementación**: Uso de `write_file` para generar HTML y `browser_vision` para verificar la fidelidad visual antes del despliegue en `generative-widgets`.

## Etiquetas
#design-system #frontend #sentry #dark-mode

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\popular-web-designs\templates\sentry.md`
