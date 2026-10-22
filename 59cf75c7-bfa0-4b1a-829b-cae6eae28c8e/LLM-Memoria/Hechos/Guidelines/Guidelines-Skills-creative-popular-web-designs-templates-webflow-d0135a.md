---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/popular-web-designs/templates/webflow.md"
tags: [hecho]
---
# webflow.md

## Resumen
Esta guía define el sistema de diseño visual de Webflow para replicar su estética "sin código" en entornos web propios. Establece reglas estrictas sobre tipografía, paleta de colores y componentes interactivos para garantizar una fidelidad visual precisa. Sirve como referencia técnica para agentes de desarrollo que deben generar interfaces idénticas usando fuentes CDN y animaciones específicas.

## Datos clave
- **Tipografía:** Sustitución de la fuente propietaria "WF Visual Sans" por `Inter` (Google Fonts) con pesos 500–600; fallback a `system-ui`. Monoespaciado: `ui-monospace`, `Menlo`, `Consolas`.
- **Colores primarios:** Negro casi puro (`#080808`) para texto y Azul Webflow (`#146ef5`) para CTAs.
- **Paleta secundaria:** Púrpura (`#7a3dff`), Rosa (`#ed52cb`), Verde (`#00d722`), Naranja, Amarillo y Rojo.
- **Sombras:** Sistema de cascada de 5 capas con opacidades decrecientes para crear profundidad.
- **Componentes:** Botones con animación `translate(6px)` al pasar el cursor; bordes conservadores de 4px–8px (máximo).
- **Responsive:** Puntos de ruptura en 479px, 768px y 992px.
- **Flujo de trabajo:** Generar HTML con `write_file`, servir vía `generative-widgets` y validar visualmente con `browser_vision`.

## Etiquetas
#Webflow #DesignSystem #FrontendDevelopment #UIUX

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\popular-web-designs\templates\webflow.md`
