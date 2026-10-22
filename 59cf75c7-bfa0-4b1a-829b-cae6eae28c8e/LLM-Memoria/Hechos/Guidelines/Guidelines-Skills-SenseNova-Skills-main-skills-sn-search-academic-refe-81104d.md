---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-search-academic/references/refTree.md"
tags: [hecho]
---
# refTree.md

## Resumen
Este documento describe `refTree.py`, un script de entrada unificada para consultar las referencias y los documentos citados por una publicación académica específica. Su función principal es orquestar múltiples proveedores (SDK oficial y araña web) para recuperar estos datos, generando un informe JSON estructurado que incluye detalles de cada intento y errores.

## Datos clave
- **Proyecto**: `refTree.py` dentro del repositorio SenseNova-Skills.
- **Tecnologías**: Python 3, Semantic Scholar SDK, Playwright, Node.js, camoufox-js.
- **Comandos principales**:
  - Consulta básica: `python3 scripts/refTree.py --paper_id "2309.16609" --title "Qwen Technical Report"`
  - Filtrado por dirección: Usar `--direction references` o `citations`.
  - Salida a archivo: Añadir `--output results/refTree.json`.
- **Lógica de reintentos**: Si el proveedor oficial (`semantic_official`) falla, el sistema cae automáticamente al araña web (`semantic_crawler`).
- **Formato de salida**: JSON con campos `source_results`, `citations`, `references` y `attempts` para rastrear la ejecución.

## Etiquetas
#SenseNova #SemanticScholar #Python #AcademicSearch #DataPipeline

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-search-academic\references\refTree.md`
