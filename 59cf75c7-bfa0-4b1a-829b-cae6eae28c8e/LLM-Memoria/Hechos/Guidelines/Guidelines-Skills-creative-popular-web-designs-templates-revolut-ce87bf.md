---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/popular-web-designs/templates/revolut.md"
tags: [hecho]
---
# revolut.md

## Resumen
Este documento define el sistema de diseño de Revolut para crear interfaces fintech confiables mediante tipografía masiva, espacios generosos y una paleta semántica estricta. Sirve como guía técnica para replicar la estética visual oficial utilizando fuentes web alternativas y tokens CSS específicos.

## Datos clave
- **Fuentes:** Sustitución de `Aeonik Pro` por `Inter` (cuerpo) y `system monospace stack`. Uso obligatorio de tracking negativo (-2.72px) en títulos grandes para efecto "billboard".
- **Botones:** Sistema universal con radio de 9999px (forma píldora), padding generoso (14px/32px) y ausencia total de sombras.
- **Paleta CSS:** Tokens `--rui-*` definidos, incluyendo rojo peligro (`#e23b4a`), azul marca (`#494fdf`) y fondos neutros (`#191c1f`, `#ffffff`).
- **Implementación:** Generar HTML con `write_file`, servir vía `generative-widgets` (cloudflared) y validar visualmente con `browser_vision`.

## Etiquetas
#design-system #revolut #ui-tokens #typography

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\popular-web-designs\templates\revolut.md`
