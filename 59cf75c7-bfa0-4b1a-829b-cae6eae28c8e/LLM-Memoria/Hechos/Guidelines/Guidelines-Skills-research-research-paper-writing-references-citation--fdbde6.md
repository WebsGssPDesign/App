---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/research/research-paper-writing/references/citation-workflow.md"
tags: [hecho]
---
# citation-workflow.md

## Resumen
Este documento establece un flujo de trabajo riguroso para la gestión programática de citas, diseñado específicamente para prevenir alucinaciones en referencias generadas por IA. Su objetivo principal es garantizar la integridad académica mediante la verificación cruzada de fuentes antes de incluir cualquier entrada en una bibliografía.

## Datos clave
- **APIs principales**: Semantic Scholar (búsqueda ML), CrossRef (DOI y BibTeX), arXiv (preprints) y OpenAlex.
- **Flujo de 5 pasos**: Búsqueda → Verificación en múltiples fuentes → Recuperación de BibTeX vía DOI → Validación del contenido → Adición al archivo `.bib`.
- **Verificación cruzada**: Un paper debe existir en al menos dos fuentes (ej. Semantic Scholar + CrossRef) para ser aceptado.
- **Generación de claves**: Algoritmo Python que extrae autor, año y primera palabra del título para crear identificadores únicos (`author_year_firstword`).
- **Prevención de errores**: Se evita generar citas desde la memoria; se utiliza negociación de contenido HTTP para obtener BibTeX directo.

## Etiquetas
#gestión_citas #verificación_académica #python_api #bibliotecas

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\research\research-paper-writing\references\citation-workflow.md`
