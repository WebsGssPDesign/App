---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/manim-video/references/production-quality.md"
tags: [hecho]
---
# production-quality.md

## Resumen
Este documento establece una lista de verificación exhaustiva para garantizar que las animaciones generadas con Manim sean listas para publicación. Cubre desde la planificación pre-código, como definir paletas y guiones visuales, hasta controles de calidad post-renderizado, asegurando coherencia visual, legibilidad y un flujo narrativo efectivo.

## Datos clave
- **Pre-código**: Definir script con beats visuales, lista de escenas, paleta de colores (`PRIMARY`, etc.) y fuente monoespaciada (`MONO = "Menlo"`).
- **Calidad de texto**: Evitar superposiciones (usar `ReplacementTransform`), limitar ancho del texto al marco y mantener consistencia tipográfica.
- **Diseño espacial**: Área utilizable aproximada en coordenadas [-6.5, 6.5] x [-3.5, 3.5]; límite máximo de 6 elementos activos simultáneos.
- **Animación**: Curva de tempo sugerida (Lento → Medio → Rápido → Lento) y transiciones suaves con `FadeOut` seguido de espera (`wait`).
- **Colores**: Uso de colores saturados para fondos oscuros y asignación semántica consistente de colores a conceptos.
- **Renderizado**: Comandos obligatorios como `-qh`, verificación previa con `-ql` y `-qm`, y uso estricto de constantes para colores y fuentes.

## Etiquetas
#manim #producción #animación #calidad

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\manim-video\references\production-quality.md`
