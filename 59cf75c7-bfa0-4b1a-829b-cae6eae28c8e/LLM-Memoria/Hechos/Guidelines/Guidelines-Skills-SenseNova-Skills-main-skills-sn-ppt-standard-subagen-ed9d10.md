---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-ppt-standard/subagents/image.md"
tags: [hecho]
---
# image.md

## Resumen
Esta guía define las responsabilidades del subagente de imágenes dentro del sistema Box-Agent, detallando el flujo para obtener o generar visuales que cumplan con una "receta visual" unificada. Su función es asegurar la disponibilidad de activos verificables en `assets/`, gestionando tanto la descarga de imágenes reales como la generación sintética, y coordinando la integración final con el agente de diapositivas.

## Datos clave
- **Proyecto**: SenseNova-Skills (Box-Agent).
- **Tecnologías**: Python scripts (`deck.py`, `image_cutout.py`), APIs de búsqueda web/generación, gestión de archivos JSON.
- **Decisiones críticas**: Priorizar imágenes reales para sujetos identificados; prohibir el uso de generados como evidencia; separar datos visuales de diagramas (que corresponden al agente Slide).
- **Rutas y comandos importantes**:
  - Registro: `asset-register` (para descargar, generar o adjuntar).
  - Asignación: `asset-assign` para vincular archivos a IDs.
  - Revisión: `asset-contact`, `asset-review` y `figure-crop`.
  - Recorte: `image_cutout.py` con estrategias `auto` o `--subject-box`.
- **Reglas de calidad**: Los activos deben estar en estado `ready` en `catalog.json`; las imágenes hotlink están prohibidas; los recortes deben preservar partes protegidas (rostros, logos).

## Etiquetas
#SenseNova #GestiónDeActivos #FlujoDeTrabajo #Python

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-ppt-standard\subagents\image.md`
