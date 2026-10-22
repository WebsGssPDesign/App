---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/productivity/notion/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía técnica explica cómo interactuar con la API de Notion utilizando el CLI oficial `ntn` o herramientas HTTP estándar como `curl`. Su objetivo es automatizar tareas de productividad, permitiendo crear, editar y consultar páginas y bases de datos desde la línea de comandos en Linux, macOS y Windows.

## Datos clave
- **Herramientas**: CLI `ntn` (preferido en macOS/Linux) vs HTTP + `curl` (fallback universal).
- **Autenticación**: Requiere variable de entorno `NOTION_API_KEY` (token que empieza por `ntn_` o `secret_`) y configuración de `NOTION_KEYRING=0`.
- **Comandos esenciales**: `ntn files create <archivo>` para subida rápida, `ntn api v1/pages/{id}/markdown` para lectura de contenido.
- **Restricciones**: El CLI nativo no está disponible en Windows (requiere WSL2 o usar curl); la versión de API obligatoria es `2025-09-03`.
- **Pasos críticos**: Compartir páginas con la integración en Notion antes de acceder vía API.

## Etiquetas
#Notion #CLI #Automatización #API #Productividad

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\productivity\notion\SKILL.md`
