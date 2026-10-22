---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/github/github-issues/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento detalla procedimientos para gestionar issues en GitHub mediante la CLI oficial (`gh`) o directamente con la API REST usando `curl`. Su objetivo es estandarizar tareas de creación, filtrado, etiquetado y asignación de problemas técnicos. Incluye scripts de configuración automática, plantillas estructuradas para reportar bugs y solicitudes de características, así como comandos específicos para modificar estados y comentar en tickets existentes.

## Datos clave
- **Herramientas:** `gh` (GitHub CLI) y `curl` con Python para procesamiento JSON.
- **Configuración:** Detección automática del autenticador (`gh` vs token de entorno `.env`).
- **Comandos principales:** `gh issue list`, `gh issue create`, `gh issue edit`.
- **API Endpoints:** `/repos/{owner}/{repo}/issues`, `/search/issues`, `/labels`, `/assignees`.
- **Plantillas incluidas:** Estructuras estandarizadas para "Bug Report" y "Feature Request".

## Etiquetas
#GitHub #DevOps #ProjectManagement #Automation

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\github\github-issues\SKILL.md`
