---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/webs/portfolio/Nueva carpeta/CascadeProjects/ecommerce-basictech-master/CLAUDE.md"
tags: [hecho]
---
# CLAUDE.md

## Resumen
Este archivo guía a la IA en el desarrollo del e-commerce BasicTechShop, una aplicación Next.js 16 con TypeScript y Tailwind CSS. Establece normas específicas para la arquitectura de componentes, gestión de datos y estilos, priorizando la separación entre lógica del servidor y cliente.

## Datos clave
- **Tecnologías**: Next.js 16 (App Router), TypeScript, Tailwind CSS v4, shadcn/ui ("new-york" style).
- **Organización**: Componentes divididos por áreas (`layout`, `home`, `products`, etc.) y datos mockeados en `src/data/`.
- **Reglas de implementación**: Usar páginas dedicadas para formularios (no modales), evitar Server Actions (usar Route handlers) y Zustand para estado global.
- **Formularios**: Obligatoria la combinación de `react-hook-form` con `zod` para validación.
- **Estilos**: Sistema basado en variables CSS OKLCH y uso de `cn()` para clases.

## Etiquetas
#NextJS #Ecommerce #TypeScript #TailwindCSS

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\webs\portfolio\Nueva carpeta\CascadeProjects\ecommerce-basictech-master\CLAUDE.md`
