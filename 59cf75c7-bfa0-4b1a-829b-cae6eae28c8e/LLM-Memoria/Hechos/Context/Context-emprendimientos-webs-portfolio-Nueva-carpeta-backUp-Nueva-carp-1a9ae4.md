---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/webs/portfolio/Nueva carpeta/backUp/Nueva carpeta/windsurf-project-7/README.md"
tags: [hecho]
---
# README.md

## Resumen
Este documento describe la arquitectura y configuración del sitio web "MiniMarketUy GSSP", una tienda online minimalista que integra Supabase para base de datos en tiempo real, MercadoPago para pagos y un panel administrativo completo. Su objetivo es facilitar la gestión de productos, órdenes y notificaciones mediante un diseño responsive y funcional.

## Datos clave
- **Tecnologías**: HTML, TailwindCSS, TypeScript, Supabase (Auth, Realtime, Storage), MercadoPago, PWA con Service Worker.
- **Configuración**: Variables de entorno en `js/config.js` (URLs y claves públicas); credenciales de desarrollo en `.env`.
- **Base de datos**: Tablas requeridas: `products`, `orders`, `cart`, `notifications`; implementación de Row Level Security (RLS).
- **Panel Admin**: Rutas `/admin/products/`, `/admin/orders/`, `/admin/payments/` y otros módulos placeholder.
- **Scripts principales**: `npm run dev` (desarrollo), `npm run build` (producción), `npm run deploy`.
- **SEO**: Configuración de Sitemap, robots.txt y meta tags optimizados para Google Analytics.

## Etiquetas
#ecommerce #supabase #mercadopago #pwa #adminpanel

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\webs\portfolio\Nueva carpeta\backUp\Nueva carpeta\windsurf-project-7\README.md`
