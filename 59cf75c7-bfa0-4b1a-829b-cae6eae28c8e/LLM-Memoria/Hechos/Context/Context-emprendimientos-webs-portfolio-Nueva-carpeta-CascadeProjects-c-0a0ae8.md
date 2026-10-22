---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/webs/portfolio/Nueva carpeta/CascadeProjects/curved-conjunction/README.md"
tags: [hecho]
---
# README.md

## Resumen
Este documento detalla la arquitectura y configuración de "TechStore", una tienda e-commerce moderna construida con Astro, UnoCSS y Supabase. Su propósito es ofrecer un sitio de alto rendimiento, SEO optimizado y seguro para la venta de productos tecnológicos, integrando pagos vía MercadoPago y gestión de datos en tiempo real.

## Datos clave
- **Tecnologías**: Astro (frontend), UnoCSS (estilos atómicos), TypeScript, Supabase (PostgreSQL + Auth + Storage) y MercadoPago.
- **Estructura**: Uso de arquitectura "Islands" con componentes reutilizables en `src/components/` y páginas dinámicas en `src/pages/`.
- **Base de datos**: Tablas principales incluyen `products`, `orders`, `order_items`, `blog_posts` y `notifications`.
- **Edge Functions**: Implementación de webhooks para MercadoPago (`mercadopago-webhook`) y envío de notificaciones por correo (`send-notification`).
- **Configuración inicial**: Requiere copiar `.env.example`, ejecutar el esquema SQL en Supabase, crear buckets de almacenamiento y configurar credenciales de MercadoPago.
- **Despliegue**: Recomendado en Vercel con integración automática; alternativa Netlify requiere configuración manual del build command (`npm run build`) y directorio `dist`.

## Etiquetas
#Astro #Ecommerce #Supabase #MercadoPago #TypeScript

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\webs\portfolio\Nueva carpeta\CascadeProjects\curved-conjunction\README.md`
