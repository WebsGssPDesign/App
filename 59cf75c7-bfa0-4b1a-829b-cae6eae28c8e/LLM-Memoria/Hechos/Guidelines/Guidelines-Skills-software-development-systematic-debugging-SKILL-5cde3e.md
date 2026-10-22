---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/software-development/systematic-debugging/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define un protocolo de depuración sistemática en cuatro fases para identificar la causa raíz antes de aplicar cualquier corrección, evitando parches superficiales. Su objetivo es estandarizar el proceso de investigación técnica mediante bucles de retroalimentación estrictos y análisis exhaustivo de errores.

## Datos clave
- **Principio central:** NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST (No arreglos sin investigar la causa raíz primero).
- **Fase 1 obligatoria:** Investigación de causa raíz que incluye leer mensajes de error, construir bucles de retroalimentación cerrados y verificar cambios recientes.
- **Herramientas sugeridas:** `read_file`, `search_files`, `terminal` para ejecutar pruebas o scripts de reproducción (`pytest`, `curl`, headless browsers).
- **Comandos clave:** `git log --oneline -10`, `git diff`, `git log -p`.
- **Estrategia de bucles:** Priorizar tests fallantes, luego scripts HTTP/CLI, y finalmente harnesses de bisección o fuzzing.

## Etiquetas
#debugging #root-cause #systematic-process #software-quality

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\software-development\systematic-debugging\SKILL.md`
