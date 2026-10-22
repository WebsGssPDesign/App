---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/github/github-repo-management/references/github-api-cheatsheet.md"
tags: [hecho]
---
# github-api-cheatsheet.md

## Resumen
Este documento es una guía de referencia rápida para la gestión de repositorios y automatización mediante la GitHub REST API. Sirve como manual técnico que detalla endpoints, métodos HTTP y patrones de comandos `curl` para operaciones comunes como crear pull requests, ejecutar acciones CI/CD y administrar secretos.

## Datos clave
- **Base URL**: `https://api.github.com`
- **Autenticación**: Requiere el encabezado `-H "Authorization: token $GITHUB_TOKEN"` en todas las solicitudes.
- **Helper de entorno**: Uso del script `gh-env.sh` para configurar automáticamente variables `$GH_OWNER`, `$GH_REPO` y el token.
- **Operaciones principales**: Crear/actualizar repositorios, gestionar pull requests (con métodos squash/rebase), listar issues y ejecutar workflows de GitHub Actions.
- **Comandos útiles**: Patrones específicos de `curl` para GET, POST con JSON, PATCH y DELETE; verificación de límites de tasa (`rate_limit`).
- **Paginación**: Soporte para parámetros `per_page` (máx 100) y navegación mediante el encabezado `Link`.

## Etiquetas
#GitHubAPI #DevOps #Automatización #CI_CD

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\github\github-repo-management\references\github-api-cheatsheet.md`
