---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/research/research-paper-writing/templates/README.md"
tags: [hecho]
---
# README.md

## Resumen
Este archivo documenta los plantillas oficiales de LaTeX para conferencias clave en aprendizaje automático e inteligencia artificial, como ICML, NeurIPS y ACL. Su propósito es guiar a los investigadores en la compilación correcta de sus manuscritos, gestionar referencias bibliográficas y cumplir con las restricciones específicas de formato y anonimato requeridas por cada evento.

## Datos clave
- **Proyectos/Conferencias**: ICML 2026, ICLR 2026, NeurIPS 2025, ACL (EMNLP, NAACL), AAAI 2026, COLM 2025.
- **Tecnologías**: LaTeX, TeX Live, VS Code con extensión "LaTeX Workshop", Overleaf, comandos de línea (`pdflatex`, `bibtex`, `latexmk`).
- **Decisiones y Rutas**: Se recomienda usar TeX Live completo para evitar errores de paquetes. Existen rutas distintas para versiones de "submission" (anonimizado) y "camera-ready".
- **Comandos importantes**: `latexmk -pdf -pvc main.tex` para compilación continua; secuencia manual `pdflatex -> bibtex -> pdflatex x2`.
- **Restricciones**: Límites de páginas varían por conferencia (ej. ICML 8/9, AAAI 7/8); se requiere anonimato total en la versión de envío.

## Etiquetas
#LaTeX #MachineLearning #AcademicWriting #Conferences #ICML #NeurIPS

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\research\research-paper-writing\templates\README.md`
