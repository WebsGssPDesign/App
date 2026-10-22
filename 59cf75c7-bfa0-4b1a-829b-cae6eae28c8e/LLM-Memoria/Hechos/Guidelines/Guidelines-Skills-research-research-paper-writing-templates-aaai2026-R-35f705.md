---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/research/research-paper-writing/templates/aaai2026/README.md"
tags: [hecho]
---
# README.md

## Resumen
Este archivo presenta una guía para un template LaTeX unificado de AAAI 2026, diseñado para gestionar tanto la versión anónima como la final (camera-ready) en un solo documento. Su función principal es facilitar el flujo de trabajo eliminando la necesidad de mantener dos archivos separados mediante mecanismos de compilación condicional.

## Datos clave
- **Proyecto**: Template unificado AAAI 2026 mejorado con Cursor.
- **Tecnologías**: LaTeX, Overleaf (para pruebas online), pdflatex, bibtex.
- **Mecanismo central**: Uso de `\def\aaaianonymous{true}` para activar/desactivar estilos anónimos vía condicionales (`\ifdefined`).
- **Archivos principales**: `aaai2026-unified-template.tex`, `aaai2026-unified-supp.tex`.
- **Comandos críticos**: `\usepackage[submission]{aaai2026}` (anónimo) vs `\usepackage{aaai2026}` (final).
- **Pasos de compilación**: `pdflatex` → `bibtex` → `pdflatex` × 2.
- **Advertencia**: No repetir `\bibliographystyle{aaai2026}` en el documento, ya que lo gestiona el `.sty`.

## Etiquetas
#AAAI2026 #LaTeX #AcademicWriting #Templates

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\research\research-paper-writing\templates\aaai2026\README.md`
