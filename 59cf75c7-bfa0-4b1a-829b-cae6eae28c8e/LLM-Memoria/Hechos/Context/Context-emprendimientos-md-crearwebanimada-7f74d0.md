---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/.md/crearwebanimada.md"
tags: [hecho]
---
# crearwebanimada.md

## Resumen
Este archivo detalla la construcción de una página web premium para "ClinicaPura" utilizando Next.js 14, TypeScript y Framer Motion. Su función principal es implementar un efecto de scroll animado que carga secuencias de imágenes en un lienzo HTML5 (Canvas) mientras el usuario navega por la sección del héroe.

## Datos clave
- **Tecnologías:** Next.js 14+ (App Router), TypeScript, Tailwind CSS, Framer Motion.
- **Recursos visuales:** Secuencia de imágenes desde `/public/frames-dental/1.webp` hasta `120.webp`.
- **Diseño:** Paleta específica con colores #F8F7F4 (fondo) y #00B4D8 (primario); fuentes 'Playfair Display' y 'DM Sans'.
- **Componente HeroCanvas:** Utiliza un contenedor de 700vh para activar la animación; el canvas se mantiene fijo (`sticky`) mientras las imágenes avanzan del 1 al 120.
- **Lógica de renderizado:** Carga todas las imágenes en memoria al inicio, calcula escalado automático y aplica un degradado radial (vignette) sobre cada frame dibujado.
- **Estructura de archivos:** `app/page.tsx`, `components/HeroCanvas.tsx`, `components/Navbar.tsx`.

## Etiquetas
#NextJS #FramerMotion #WebAnimada #DiseñoFrontend

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\.md\crearwebanimada.md`
