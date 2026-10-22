---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/github/github-repo-management/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento establece las directrices para gestionar repositorios en GitHub, cubriendo operaciones como clonar, crear, bifurcar (fork) y sincronizar. Sirve como referencia técnica que prioriza el uso de la herramienta `gh` pero proporciona alternativas robustas utilizando comandos nativos de `git` y solicitudes a la API con `curl`.

## Datos clave
- **Herramientas principales**: CLI oficial `gh`, `git` estándar, `curl` para la API.
- **Gestión de autenticación**: Detección automática entre token `gh auth` o variables de entorno (`GITHUB_TOKEN`).
- **Creación de repositorios**: Uso de flags como `--public`, `--private`, `--license` y plantillas (`--template`).
- **Bifurcación (Fork)**: Comando `gh repo fork --clone` o creación manual vía API seguida de configuración del remote `upstream`.
- **Sincronización**: Mantener forks actualizados con `git fetch upstream` y merge, o usando `gh repo sync`.
- **Búsqueda y listado**: Consultas a la API para listar repositorios propios o buscar proyectos por lenguaje y estrellas.

## Etiquetas
#GitHub #GestiónDeRepositorios #Git #Automatización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\github\github-repo-management\SKILL.md`
