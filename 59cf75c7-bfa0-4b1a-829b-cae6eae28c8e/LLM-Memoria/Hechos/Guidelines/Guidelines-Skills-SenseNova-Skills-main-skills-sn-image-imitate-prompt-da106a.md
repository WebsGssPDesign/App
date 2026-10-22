---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-image-imitate/prompts/image_annotate.md"
tags: [hecho]
---
# image_annotate.md

## Resumen
Este documento define un prompt para una IA experta en análisis visual. Su función es extraer contenido de imágenes, generar descripciones detalladas y crear un esquema estructural JSON para permitir la regeneración precisa del diseño gráfico original.

## Datos clave
- **Tareas principales**: Generar un "Short Caption" (aprox. 20 palabras) y un "Long Caption" exhaustivo que incluya títulos, datos numéricos inferidos de gráficos y texto literal sin traducción.
- **Formato de salida estricto**: Respuesta estructurada con secciones SHORT_CAPTION, LONG_CAPTION y LAYOUT_BLUEPRINT_JSON.
- **Especificaciones del JSON**: El "Layout Blueprint" debe usar coordenadas normalizadas [0, 1], definir jerarquías visuales (regiones, índices Z) y capturar estilos como paleta de colores y tipografía para mantener la fidelidad al diseño original.

## Etiquetas
#análisis_visual #procesamiento_de_imágenes #json_structure

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-image-imitate\prompts\image_annotate.md`
