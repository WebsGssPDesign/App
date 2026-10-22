---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/webs/portfolio/Nueva carpeta/CascadeProjects/files/files/README.md"
tags: [hecho]
---
# README.md

## Resumen
Este archivo documenta una tienda online estática construida con HTML, CSS y JavaScript que utiliza JSON para cargar productos dinámicamente. Su propósito es servir como guía completa para configurar la interfaz, gestionar inventario, optimizar imágenes y desplegar el sitio en plataformas como Netlify o GitHub Pages sin necesidad de un servidor backend complejo.

## Datos clave
- **Estructura**: Separación clara entre estilos (CSS modular), lógica (JS ES Modules) y datos (`productos.json`).
- **Inicio rápido**: Requiere servidor local para módulos ES; opciones sugeridas: `python3 -m http.server 8080` o `npx serve .`.
- **Configuración crítica**: Número de WhatsApp en `js/cart.js`, paleta de colores en `css/base/variables.css` y datos de productos en `data/productos.json`.
- **Funcionalidades**: Catálogo dinámico, búsqueda con debounce, filtros por categoría, carrito persistente en localStorage y checkout vía WhatsApp.
- **Optimización**: Uso obligatorio de imágenes WebP (800x800px) con lazy loading mediante IntersectionObserver.
- **Automatización**: Script opcional para generar `productos.json` desde Supabase antes del despliegue.

## Etiquetas
#e-commerce #frontend-statico #javascript #html-css #whatsapp-checkout

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\webs\portfolio\Nueva carpeta\CascadeProjects\files\files\README.md`
