---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/github/github-auth/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define un procedimiento para configurar la autenticación de GitHub en tres entornos (Linux, macOS y Windows), permitiendo a los agentes gestionar repositorios, PRs y CI. Establece una lógica de detección que prioriza el uso del CLI `gh` si está instalado; de lo contrario, recurre a métodos nativos de Git con tokens HTTPS o claves SSH sin necesidad de permisos de root.

## Datos clave
- **Proyecto**: Configuración de autenticación para agentes GitHub (versión 1.1.0).
- **Tecnologías**: Git, CLI `gh`, SSH (ed25519), curl, tokens de acceso personal.
- **Decisiones principales**: Priorizar `gh auth` si está disponible; usar `credential.helper store` o `cache` para autenticación HTTPS sin sudo; preferir claves ed25519 sobre RSA.
- **Comandos y pasos críticos**:
  - Detección: `git --version`, `gh --version`, `gh auth status`.
  - Token HTTPS: Crear token con scopes `repo` y `workflow`; configurar `git config --global credential.helper store`.
  - Clave SSH: Generar `ssh-keygen -t ed25519`; añadir clave pública en GitHub; redirigir URLs HTTPS a SSH.
  - API fallback: Usar variable de entorno `GITHUB_TOKEN` con curl si no hay CLI instalado.

## Etiquetas
#GitHub #Autenticación #Git #DevOps #SSH

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\github\github-auth\SKILL.md`
