---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/productivity/powerpoint/pptxgenjs.md"
tags: [hecho]
---
# pptxgenjs.md

## Resumen
Esta guía técnica explica cómo generar presentaciones de PowerPoint automáticamente utilizando la librería PptxGenJS en Node.js. Detalla la configuración inicial, dimensiones de diapositivas y métodos para añadir texto formateado, listas, formas geométricas e imágenes con diversas opciones de manipulación.

## Datos clave
- **Tecnología**: Librería `pptxgenjs` (Node.js).
- **Configuración**: Definición del layout (`LAYOUT_16x9`, etc.), autor y título antes de añadir diapositivas.
- **Texto**: Uso de arrays para texto rico, espaciado de caracteres (`charSpacing`) y manejo de saltos de línea (`breakLine`). Se recomienda `margin: 0` para alineación precisa con formas.
- **Listas**: Implementación mediante la opción `bullet: true` en objetos de texto; evitar el uso directo de viñetas Unicode.
- **Formas**: Creación de rectángulos, óvalos y líneas con propiedades de relleno (`fill`), bordes (`line`) y sombras (`shadow`). Las sombras requieren coordenadas hexadecimales sin `#` y ángulo positivo para evitar corrupción del archivo.
- **Imágenes**: Soporte para rutas locales, URLs y datos Base64. Opciones de redimensionamiento incluyen `contain`, `cover` y `crop`. Formatos soportados: PNG, JPG, GIF y SVG.
- **Iconos**: Flujo recomendado para usar React Icons (SVG) rasterizados a PNG con la librería `sharp`.

## Etiquetas
#PptxGenJS #GeneraciónDePresentaciones #NodeJS #DocumentaciónTécnica

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\productivity\powerpoint\pptxgenjs.md`
