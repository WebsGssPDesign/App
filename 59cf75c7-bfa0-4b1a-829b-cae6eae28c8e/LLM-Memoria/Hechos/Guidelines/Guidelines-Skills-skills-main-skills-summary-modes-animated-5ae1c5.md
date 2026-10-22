---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/skills-main/skills/summary/modes/animated.md"
tags: [hecho]
---
# animated.md

## Resumen
Esta guía establece principios para animaciones web que priorizan la legibilidad y el rendimiento, exigiendo que el contenido sea funcional sin JavaScript ni movimiento. Su objetivo es crear experiencias fluidas utilizando solo CSS y SVG nativos, evitando dependencias externas para garantizar compatibilidad a largo plazo y accesibilidad.

## Datos clave
- **Regla de oro:** La página debe ser totalmente legible con animaciones desactivadas; el movimiento no puede transportar información crítica.
- **Tecnologías permitidas:** Solo CSS y SVG (transiciones, `@keyframes`, `stroke-dasharray`, IntersectionObserver básico). Prohibido usar librerías como GSAP o Anime.js.
- **Qué animar:** Contadores únicos, líneas de flujo, gráficos que crecen en menos de 600ms y secciones con entrada escalonada (60ms).
- **Qué evitar:** Animaciones en texto corporal, elementos que retrasan el titular, bucles decorativos sin estado vivo y propiedades de layout.
- **Presupuesto técnico:** Las animaciones de entrada deben terminar en menos de 1 segundo; usar solo `transform` y `opacity`. Easing: `cubic-bezier(0.22, 1, 0.36, 1)`.
- **Requisitos obligatorios:** Incluir media queries para `prefers-reduced-motion` y `print`; el estado final de cada elemento debe ser su estilo por defecto.

## Etiquetas
#animaciones #css #accesibilidad

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\skills-main\skills\summary\modes\animated.md`
