---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/github/github-code-review/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define una guía técnica para realizar revisiones de código en GitHub, cubriendo tanto la evaluación de cambios locales antes del empuje como la revisión de Pull Requests abiertos. Su objetivo es estandarizar el proceso de auditoría de calidad mediante comandos `git` nativos y herramientas de línea de comando (`gh`, `curl`) para interactuar con la API de GitHub.

## Datos clave
- **Herramientas**: Uso preferente de `git`; alternativas `gh` (CLI oficial) o `curl` + Python para interacciones vía API.
- **Comandos críticos**: `git diff main...HEAD --stat`, `git fetch origin pull/123/head:pr-123`, `gh pr view`.
- **Flujo de autenticación**: Detección automática entre token `GITHUB_TOKEN` en entorno, archivo `.env` o credenciales en `~/.git-credentials`.
- **Estrategia de revisión**: Análisis global (`--stat`), búsqueda de patrones inseguros (contraseñas, logs) y comentarios estructurados por severidad.

## Etiquetas
#GitHub #CodeReview #Git #DevOps #Seguridad

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\github\github-code-review\SKILL.md`
