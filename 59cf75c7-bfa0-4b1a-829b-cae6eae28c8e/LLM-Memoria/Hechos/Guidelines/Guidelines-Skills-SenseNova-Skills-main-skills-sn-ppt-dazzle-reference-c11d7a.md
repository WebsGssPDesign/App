---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-ppt-dazzle/references/fancy-cookbook.md"
tags: [hecho]
---
# fancy-cookbook.md

## Resumen
Este documento establece las directrices técnicas y creativas para el sistema de animaciones "fancy" en presentaciones, definiendo cómo seleccionar estilos según la solemnidad del evento. Su función es garantizar que los efectos visuales sean coherentes con el tema sin caer en el exceso decorativo o el uso incorrecto de tecnologías 3D.

## Datos clave
- **Reglas de selección**: Elegir una sola combinación global (fondo + transición) por presentación; evitar superposición de técnicas similares.
- **Niveles de densidad**: "Solemn" (negocios/académicos) usa solo fórmulas marcadas y parámetros mínimos; "Libre" (creativo/eventos) permite todo el catálogo.
- **Tecnologías 3D**: Diferenciar entre fondos abstractos (Three.js/Shaders, siempre permitidos) e inmersión total (solo para temas espaciales o arquitectónicos).
- **Prohibiciones**: No usar fondos de cuadrícula (GridHelper); prohibido degradar escenas 3D planificadas a partículas 2D.
- **Implementación técnica**: Animaciones deben depender de `.slide.active` para reinicio automático; capas con `pointer-events:none`; canvas limitado a 1280x720.
- **Fórmulas destacadas**: Staggered reveal (base universal), SVG draw-in, contadores ascendentes y efectos "popIn" elásticos.

## Etiquetas
#presentaciones #animaciónCSS #ThreeJS #diseñoUI #guías

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-ppt-dazzle\references\fancy-cookbook.md`
