---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/productivity/powerpoint/editing.md"
tags: [hecho]
---
# editing.md

## Resumen
Esta guía detalla un flujo de trabajo basado en plantillas para editar presentaciones de PowerPoint, priorizando la variedad visual y el uso de scripts específicos sobre ediciones manuales. Su objetivo es garantizar una estructura coherente, evitar errores comunes al adaptar contenido a diseños fijos y asegurar que los cambios se realicen mediante herramientas automatizadas confiables.

## Datos clave
- **Flujo principal**: Analizar plantilla -> Planear mapeo de diapositivas -> Desempaquetar (`unpack.py`) -> Estructura (borrar/duplicar/reordenar) -> Editar contenido con subagentes -> Limpiar (`clean.py`) -> Empaquetar (`pack.py`).
- **Scripts esenciales**: `thumbnail.py` para análisis visual, `add_slide.py` para duplicación segura, y `clean.py` para eliminar archivos huérfanos.
- **Reglas de formato**: Usar `b="1"` en `<a:rPr>` para negritas; evitar viñetas unicode (•); separar listas en elementos `<a:p>` distintos.
- **Adaptación de plantillas**: Eliminar elementos completos (imágenes + texto) si el contenido fuente es menor al de la plantilla, no solo limpiar texto.
- **Comando crítico**: `python scripts/office/pack.py unpacked/ output.pptx --original template.pptx` para validar y reparar el archivo final.

## Etiquetas
#PowerPoint #EdiciónDePresentaciones #Automatización #GuíaTécnica

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\productivity\powerpoint\editing.md`
