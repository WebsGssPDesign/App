---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/apple/apple-notes/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía describe cómo gestionar la aplicación Apple Notes desde la terminal utilizando el CLI `memo`, permitiendo crear, buscar y editar notas que se sincronizan automáticamente entre dispositivos de Apple a través de iCloud. Su utilidad principal radica en organizar información personal o profesional con acceso multiplataforma sin necesidad de abrir la interfaz gráfica de la app.

## Datos clave
- **Proyecto**: apple-notes (versión 1.0.0, licencia MIT).
- **Tecnologías**: macOS, Apple Notes.app, iCloud, CLI `memo`.
- **Prerrequisitos**: Instalar `memo` vía Homebrew (`brew tap antoniorodr/memo`) y habilitar acceso a automatización en System Settings.
- **Comandos principales**: `memo notes -a` (crear), `-s "query"` (buscar), `-e` (editar), `-ex` (exportar a Markdown/HTML).
- **Decisiones de uso**: Priorizar este skill para sincronización cross-device; usar `memory` para notas internas del agente y `obsidian` para gestión de vaults.

## Etiquetas
#AppleNotes #macOS #CLI #iCloud

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\apple\apple-notes\SKILL.md`
