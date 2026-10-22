---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/github/github-pr-workflow/references/conventional-commits.md"
tags: [hecho]
---
# conventional-commits.md

## Resumen
Este documento establece un estándar para escribir mensajes de commit en GitHub siguiendo el formato Conventional Commits. Su objetivo es automatizar la generación de changelogs, facilitar las releases semánticas y mejorar la legibilidad del historial de cambios del proyecto.

## Datos clave
- **Formato base**: `tipo(scope): descripción` (ej: `feat(auth): añadir flujo OAuth2`).
- **Tipos principales**: `feat` (nuevas funcionalidades), `fix` (correcciones de errores), `refactor`, `docs`, `test`, `ci`, `chore`, `perf`, `style`, `build`.
- **Cambio rompedor**: Se indica añadiendo `!` después del tipo o usando el pie de página `BREAKING CHANGE:`.
- **Enlace a issues**: Uso de palabras clave como `Closes #42`, `Fixes #42` o `Refs #42` en el cuerpo del commit.
- **Estructura multi-línea**: El cuerpo debe limitarse a 72 caracteres por línea y usar viñetas para listar múltiples cambios.

## Etiquetas
#conventional-commits #github-workflow #versioning #best-practices

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\github\github-pr-workflow\references\conventional-commits.md`
