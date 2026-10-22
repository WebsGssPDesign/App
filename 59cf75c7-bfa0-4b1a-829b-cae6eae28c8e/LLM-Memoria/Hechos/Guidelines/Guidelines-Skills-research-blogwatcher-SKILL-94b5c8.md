---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/research/blogwatcher/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe la herramienta `blogwatcher-cli`, una utilidad para monitorear actualizaciones en blogs y feeds RSS/Atom de forma automatizada. Permite gestionar suscripciones, descubrir fuentes automáticamente mediante scrapers HTML y organizar artículos leídos o no leídos en una base de datos local.

## Datos clave
- **Proyecto:** blogwatcher (versión 2.0.0, fork de Hyaxia/blogwatcher).
- **Tecnologías:** Go, Docker, SQLite (base de datos por defecto: `~/.blogwatcher-cli/blogwatcher-cli.db`).
- **Instalación:** Soporta instalación vía Go (`go install`), descarga directa de binarios o contenedores Docker.
- **Comandos principales:** `add` (añadir blog con URL o selector HTML), `scan` (buscar novedades), `articles` (listar no leídos) y `read`/`unread` (marcar estado).
- **Variables de entorno:** `BLOGWATCHER_DB`, `BLOGWATCHER_WORKERS`, `BLOGWATCHER_SILENT`.
- **Funcionalidad extra:** Importación masiva desde archivos OPML y migración de datos desde la versión original.

## Etiquetas
#RSS #Monitoreo #Blog #CLI #Automatización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\research\blogwatcher\SKILL.md`
