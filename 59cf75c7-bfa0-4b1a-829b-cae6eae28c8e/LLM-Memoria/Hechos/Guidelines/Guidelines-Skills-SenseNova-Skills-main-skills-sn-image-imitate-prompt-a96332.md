---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-image-imitate/prompts/layout_review.md"
tags: [hecho]
---
# layout_review.md

## Resumen
Este documento define un prompt para evaluar la similitud visual entre una imagen de referencia y una generada por IA. Su función es analizar la consistencia del diseño (jerarquía, bloques, flujo) y el estilo (paleta, tipografía), devolviendo resultados estructurados en JSON para guiar mejoras iterativas.

## Datos clave
- **Proyecto**: SenseNova-Skills (módulo de evaluación visual).
- **Entradas**: `image[0]` (referencia) e `image[1]` (candidata).
- **Dimensiones evaluadas**: Similaridad de layout y estilo.
- **Criterios de layout**: Jerarquía visual, disposición de bloques, proporciones relativas, dirección del flujo de lectura y alineación de diagramas.
- **Criterios de estilo**: Paleta de colores, contraste, textura visual y consistencia tipográfica.
- **Formato de salida**: JSON estricto (sin texto narrativo).
- **Reglas de puntuación**: Valores entre 0.0 y 1.0 con dos decimales; `pass` es verdadero si el layout >= 0.75 sin desviaciones estructurales mayores.
- **Salidas específicas**: Listas concisas para `major_deviations` (inconsistencias) y `fix_hints` (sugerencias de edición del prompt).

## Etiquetas
#evaluación_visual #IA_generativa #layout_design #prompt_engineering

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-image-imitate\prompts\layout_review.md`
