---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/github/github-pr-workflow/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía detalla el ciclo de vida completo de un Pull Request en GitHub, desde la creación de ramas hasta la fusión final. Proporciona instrucciones paso a paso para gestionar autenticación, commits y monitoreo de CI/CD, ofreciendo métodos nativos (`gh`) y alternativas mediante `git` + `curl` para entornos sin el CLI oficial.

## Datos clave
- **Flujo principal**: Crear rama (`feat/fix/refactor`), commit con mensajes convencionales, push y apertura del PR.
- **Autenticación flexible**: Detecta automáticamente si usar la herramienta `gh` o variables de entorno/tokens para llamadas `curl`.
- **Extracción dinámica**: Scripts para obtener `owner/repo` desde el remote de Git sin hardcodear nombres.
- **Monitoreo CI**: Comandos para verificar estados (`success`, `failure`) y logs de fallos en workflows.
- **Comandos críticos**: `gh pr create`, `git push -u origin HEAD`, bucles de polling con `curl` hasta completar la integración continua.

## Etiquetas
#GitHub #CI/CD #GitWorkflow #Automation #DevOps

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\github\github-pr-workflow\SKILL.md`
