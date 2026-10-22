---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/github/github-pr-workflow/references/ci-troubleshooting.md"
tags: [hecho]
---
# ci-troubleshooting.md

## Resumen
Este documento es una guía rápida para diagnosticar y solucionar errores comunes en pipelines de integración continua (CI) basados en los registros de ejecución. Proporciona patrones de fallo específicos, comandos para extraer logs y un árbol de decisiones para identificar la causa raíz rápidamente.

## Datos clave
- **Comandos útiles**: `gh run view <RUN_ID> --log-failed`, `curl` con token para descargar logs ZIP, `gh secret list`.
- **Patrones de fallo**: Errores de test (assertions, imports), lint/formatting (flake8, black), type checking (mypy), build/compilation, permisos/auth, timeouts y Docker.
- **Pasos críticos**: Verificar versiones de dependencias entre local y CI, revisar scopes del token en el YAML del workflow, añadir `timeout-minutes` a pasos lentos.
- **Flujo de corrección**: Identificar la línea/archivo desde el traceback → corregir código o configuración (requirements.txt, Dockerfile) → commit y push para re-ejecutar.

## Etiquetas
#CI #DevOps #Troubleshooting #GitHubActions

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\github\github-pr-workflow\references\ci-troubleshooting.md`
