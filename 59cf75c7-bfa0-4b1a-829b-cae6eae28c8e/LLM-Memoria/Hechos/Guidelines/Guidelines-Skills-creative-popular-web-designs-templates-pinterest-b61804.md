---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/popular-web-designs/templates/pinterest.md"
tags: [hecho]
---
# pinterest.md

## Resumen
Este documento define el sistema de diseño de Pinterest para replicar su atmósfera cálida y visualmente inspiradora en entornos web propios. Sirve como guía técnica para implementar tipografías, paletas de colores específicos y reglas de espaciado que eviten un aspecto corporativo estéril.

## Datos clave
- **Tipografía**: Sustitución de la fuente propietaria "Pin Sans" por `DM Sans` vía CDN Google Fonts; uso de pilas de fuentes del sistema para fallback global (incluyendo CJK).
- **Paleta de colores**: Rojo marca (`#e60023`), grises cálidos tipo arena/oliva (`#e5e5e0`, `#91918c`) y texto negro con tinte púrpura (`#211922`).
- **Arquitectura de tokens**: Sistema jerárquico de tres niveles: `--comp-*` (componentes), `--sema-*` (semánticos) y `--base-*` (básicos).
- **Tipografía compacta**: Escala entre 12px y 70px, con pesos predominantes de 400–700; bordes redondeados generosos (16px a 40px).
- **Flujo de trabajo**: Generación de HTML mediante `write_file`, despliegue local con `generative-widgets` y validación visual usando `browser_vision`.

## Etiquetas
#design-system #ui-design #frontend-dev

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\popular-web-designs\templates\pinterest.md`
