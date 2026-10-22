---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/webs/portfolio/Nueva carpeta/CascadeProjects/ecommerce-app-main/ecommerce-app-main/README.md"
tags: [hecho]
---
# README.md

## Resumen
Este documento describe una aplicación de comercio electrónico nativa en la nube que utiliza React con Vite para el frontend y Supabase Cloud como backend completo, eliminando la necesidad de servidores tradicionales. Su propósito es servir como guía técnica para configurar el entorno, gestionar migraciones de base de datos mediante SQL y desplegar la aplicación siguiendo un flujo de trabajo basado en características.

## Datos clave
- **Tecnologías**: React (Vite), Supabase Cloud (Auth, Postgres, RLS, Storage), Zustand, TanStack Query.
- **Arquitectura**: Sin backend tradicional; seguridad a nivel de base de datos mediante Row Level Security (RLS).
- **Estructura**: Separación clara entre `frontend/` y `backend/supabase/`. Las migraciones SQL en `migrations/` son la fuente única de verdad.
- **Flujo de trabajo**: Crear migración -> Escribir SQL -> Empujar a Supabase Cloud -> Commit en Git.
- **Comandos esenciales**: `npx supabase login`, `npx supabase link`, `npx supabase db push` para el backend; `npm install` y `npm run dev` para el frontend.
- **Seguridad**: Los archivos `.env` nunca se deben subir al repositorio; solo se usa `.env.example`.

## Etiquetas
#ecommerce #react #supabase #cloud-native

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\webs\portfolio\Nueva carpeta\CascadeProjects\ecommerce-app-main\ecommerce-app-main\README.md`
