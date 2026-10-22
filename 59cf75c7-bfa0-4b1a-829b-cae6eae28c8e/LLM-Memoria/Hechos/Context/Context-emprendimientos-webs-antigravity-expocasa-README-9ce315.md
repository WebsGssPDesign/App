---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/webs/antigravity/expocasa/README.md"
tags: [hecho]
---
# README.md

## Resumen
Este documento describe ExpoCasa, una plataforma web completa para una inmobiliaria que incluye un sitio público y un panel administrativo. Utiliza Next.js 15 con MongoDB para gestionar propiedades, agentes y consultas, además de integrar autenticación segura y envío de correos electrónicos.

## Datos clave
- **Tecnologías**: Next.js 15 (App Router), MongoDB/Mongoose, NextAuth.js v5, Tailwind CSS v4, Recharts, Leaflet.
- **Instalación**: `npm install` seguido de la configuración del archivo `.env.local`.
- **Comandos principales**: `npm run dev` para iniciar el entorno local.
- **Estructura crítica**: Rutas públicas (`/propiedades`, `/contacto`) y administrativas (`/admin/dashboard`, `/admin/agentes`).
- **API REST**: Endpoints definidos en `src/app/api/` para propiedades, agentes, consultas y estadísticas.
- **Configuración de seguridad**: Se requiere generar una "Contraseña de aplicación" en Gmail para el envío de correos y cambiar el `AUTH_SECRET`.

## Etiquetas
#inmobiliaria #nextjs15 #mongodb #panel-administrativo #vercel

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\webs\antigravity\expocasa\README.md`
