---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/.md/webanimadaconvideo.md"
tags: [hecho]
---
# webanimadaconvideo.md

## Resumen
Guía técnica para desarrollar el sitio web de la clínica dental "ClinicaPura" utilizando Next.js, TypeScript y Tailwind CSS. El proyecto se centra en implementar una animación de scroll única que carga secuencias de imágenes mediante un elemento Canvas adhesivo, permitiendo una experiencia visual premium antes de mostrar el contenido principal.

## Datos clave
- **Tecnologías**: Next.js 14+ (App Router), TypeScript, Tailwind CSS, Framer Motion.
- **Recursos visuales**: Secuencia de 120 imágenes (`/public/frames-dental/{1-120}.webp`) para el fondo del Canvas.
- **Componentes críticos**: `HeroCanvas.tsx` (lógica de scroll y renderizado de frames) y `Navbar.tsx`.
- **Estilos**: Paleta de colores específica (#F8F7F4, #00B4D8) y fuentes Google Fonts ('Playfair Display', 'DM Sans').
- **Pasos de implementación**: Configurar `next.config.mjs` sin exportación estática, generar variables CSS en `globals.css`, y estructurar la página con un contenedor de 700vh para el efecto de scroll.

## Etiquetas
#NextJS #AnimacionScroll #ClinicaDental #Frontend

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\.md\webanimadaconvideo.md`
