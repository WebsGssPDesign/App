---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-non-spreadsheet-analysis/capability/pdf-analysis/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define una metodología para analizar archivos PDF automatizando la distinción entre documentos de texto y escaneados. Su objetivo es extraer contenido completo (texto, tablas e imágenes) mediante parsers específicos o generación de descripciones con IA, asegurando el procesamiento correcto de páginas mixtas.

## Datos clave
- **Proyecto**: `sn-da-non-spreadsheet-analysis` (Capacidad: PDF Analysis).
- **Tecnologías**: PyMuPDF (`fitz`), pdfplumber, pandas, subprocess, JSON.
- **Decisiones críticas**: Detectar el tipo de PDF en la página 0; iterar sobre TODAS las páginas sin detenerse; usar `pdfplumber` para tablas y renderizado a PNG + Captioning para escaneos.
- **Comandos/Pasos importantes**:
    - Detección: Calcular promedio de caracteres por página (umbral > 50).
    - Extracción texto: `page.get_text("text")`.
    - OCR híbrido: Renderizar a PNG con DPI 150 y ejecutar script externo `/path/to/skills/sn-da-image-caption/scripts/caption.py` con prompt en chino.
- **Rutas**: Scripts de caption ubicados en `skills/sn-da-image-caption/scripts/`.

## Etiquetas
#PDF #OCR #Automatización #Python #ExtracciónDeDatos

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-non-spreadsheet-analysis\capability\pdf-analysis\SKILL.md`
