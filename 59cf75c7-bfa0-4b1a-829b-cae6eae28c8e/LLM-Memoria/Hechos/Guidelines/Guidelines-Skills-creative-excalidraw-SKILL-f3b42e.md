---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/excalidraw/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía define una habilidad para generar diagramas de arquitectura y flujos en formato JSON nativo de Excalidraw, permitiendo crear archivos `.excalidraw` sin necesidad de cuentas ni librerías de renderizado. Sirve como referencia técnica para estructurar elementos geométricos, textos vinculados y flechas con las propiedades exactas requeridas por la plataforma.

## Datos clave
- **Proyecto**: Skill `excalidraw` (versión 1.0.0) bajo licencia MIT.
- **Tecnologías**: JSON estándar, Excalidraw Web App (`excalidraw.com`).
- **Comandos y pasos**:
  - Generar array de elementos JSON y guardar con `write_file` (ej: `~/diagrams/diagram.excalidraw`).
  - Subir para obtener enlace compartible ejecutando: `python skills/diagramming/excalidraw/scripts/upload.py <ruta_archivo>`.
- **Decisiones técnicas**:
  - Usar `fontFamily: 1` (Virgil) para texto.
  - Evitar propiedad `"label"` en formas; usar `boundElements` y `containerId` para textos dentro de figuras o flechas.
  - El orden del array JSON determina el orden de superposición (z-order).

## Etiquetas
#Excalidraw #DiagramasJSON #ArquitecturaTécnica #Visualización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\excalidraw\SKILL.md`
