---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/Lostovayne/Complete-Clone-of-Youtube"
tema: "React Server Components Suspense"
tags: [web]
---
# Lostovayne/Complete-Clone-of-Youtube

## Resumen
NewTube es un clon avanzado y reinventado de YouTube construido con Next.js 15, TypeScript y Tailwind CSS 4. El proyecto integra tecnologías modernas como tRPC para APIs seguras, Drizzle ORM con NeonDB y servicios externos como Mux y UploadThing para el procesamiento de video. Funciona como un laboratorio personal que demuestra arquitectura modular, autenticación con Clerk y flujos complejos de subida de archivos con webhooks.

## Datos clave
- **Stack principal**: Next.js 15 (App Router), TypeScript, Tailwind CSS 4, Radix UI, Lucide React.
- **Backend & API**: tRPC (type-safe), Drizzle ORM + NeonDB, Upstash Redis (caching/rate limiting).
- **Procesamiento de video**: Mux Direct Uploads para assets y playback; UploadThing para thumbnails persistentes.
- **Autenticación**: Clerk con gestión segura de usuarios.
- **Flujo de subida**: Webhooks de Mux validados en `/api/videos/webhook` que actualizan la DB y refrescan estados (thumbnail, duración).
- **Desarrollo**: Uso de Bun como package manager, Turbopack para hot reload y Ngrok para exponer servidores locales a webhooks externos.
- **Estructura**: Organización modular por características (`modules/`) con componentes reutilizables en `components/`.

## Etiquetas
#NextJS15 #tRPC #Mux #VideoClon #React19

Fuente: https://github.com/Lostovayne/Complete-Clone-of-Youtube
