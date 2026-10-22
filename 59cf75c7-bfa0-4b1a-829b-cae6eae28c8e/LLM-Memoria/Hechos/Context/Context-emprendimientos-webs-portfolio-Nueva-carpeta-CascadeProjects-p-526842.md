---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/webs/portfolio/Nueva carpeta/CascadeProjects/public/README.md"
tags: [hecho]
---
# README.md

## Resumen
Este documento describe el proyecto "MinimarketUy", una tienda online para un minimarket uruguayo desarrollada con Astro SSR, Supabase y MercadoPago. Su objetivo es permitir la gestión de catálogos, carritos de compras, pagos seguros y seguimiento de órdenes mediante una arquitectura escalable y optimizada para SEO.

## Datos clave
- **Proyecto:** MinimarketUy GSSP (E-commerce Uruguayo).
- **Tecnologías:** Astro (^4.15.0), Supabase (PostgreSQL + Auth), MercadoPago API, Tailwind CSS, TypeScript estricto.
- **Configuración inicial:** Clonar repositorio, ejecutar `npm install`, copiar `.env.example` a `.env` y configurar credenciales de Supabase y MercadoPago.
- **Base de datos:** Migración inicial vía SQL Editor (`supabase/migrations/001_initial.sql`) que crea tablas para categorías, productos, blog, órdenes y contactos con Row Level Security (RLS).
- **Pasos críticos:** Configurar variables de entorno (URLs, claves públicas y tokens privados) y registrar la URL del webhook en MercadoPago para actualizar estados de pago automáticamente.
- **Comandos principales:** `npm run dev` (puerto 4321), `git clone`, `cp .env.example .env`.

## Etiquetas
#Astro #Supabase #MercadoPago #Ecommerce #Uruguay

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\webs\portfolio\Nueva carpeta\CascadeProjects\public\README.md`
