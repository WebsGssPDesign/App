---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/popular-web-designs/templates/airtable.md"
tags: [hecho]
---
# airtable.md

## Resumen
Este documento define el sistema de diseño oficial para replicar la interfaz web de Airtable, estableciendo reglas estrictas sobre tipografía, paleta de colores y componentes visuales. Su objetivo es guiar a agentes de desarrollo o diseñadores para crear interfaces que transmitan "sophisticated simplicity" utilizando fuentes sustitutas y una jerarquía visual precisa basada en el estilo suizo.

## Datos clave
- **Tipografía**: Sustitución de la fuente propietaria Haas por `Inter` (principal) y pilas monoespaciadas del sistema; uso obligatorio de espaciado positivo entre letras.
- **Paleta de colores**: Texto principal en Azul Marino Profundo (`#181d26`) y acentos/CTAs en Azul Airtable (`#1b61c9`); fondo blanco puro con sombras azuladas multicapa.
- **Componentes**: Botones con radio de 12px, tarjetas con bordes sutiles (`#e0e2e6`) y radios entre 16px–32px; inputs y textos con variables CSS semánticas (`--theme_*`).
- **Implementación**: Uso de `write_file` para generar HTML, servicio vía `generative-widgets` (túnel cloudflared) y verificación visual con `browser_vision`.
- **Responsive**: Sistema adaptativo definido por 23 puntos de ruptura entre 425px y 1664px.

## Etiquetas
#design-system #airtable #frontend-guidelines

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\popular-web-designs\templates\airtable.md`
