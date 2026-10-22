---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/popular-web-designs/templates/airbnb.md"
tags: [hecho]
---
# airbnb.md

## Resumen
Este documento detalla el sistema de diseño de Airbnb, definiendo su atmósfera visual basada en fotografía y un esquema de color minimalista dominado por blanco y el rojo Rausch. Sirve como guía técnica para replicar la interfaz utilizando fuentes sustitutas vía CDN y tokens CSS específicos para mantener la fidelidad estética sin depender de activos propietarios.

## Datos clave
- **Proyecto:** Diseño System Airbnb (Hermes Agent).
- **Tecnologías:** HTML, CSS Variables (`--palette-*`), Google Fonts (DM Sans como sustituto).
- **Decisiones:** Sustitución de la fuente propietaria "Airbnb Cereal VF" por DM Sans; uso exclusivo del rojo Rausch (#ff385c) como acento de marca.
- **Rutas/Comandos:** `write_file` para generar HTML, `generative-widgets` para servir vía túnel cloudflared, y `browser_vision` para verificación visual.
- **Paleta crítica:** Rausch Red (#ff385c), Near Black (#222222), Luxe Purple (#460479).
- **Sombras:** Sistema de tres capas (borde + desenfoque suave + desenfoque fuerte) para tarjetas.

## Etiquetas
#design-system #airbnb #ui-ux #css-tokens

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\popular-web-designs\templates\airbnb.md`
