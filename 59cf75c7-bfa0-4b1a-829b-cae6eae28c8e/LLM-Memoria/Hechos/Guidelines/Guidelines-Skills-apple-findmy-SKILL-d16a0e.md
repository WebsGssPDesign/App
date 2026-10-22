---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/apple/findmy/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe una técnica para rastrear dispositivos Apple y AirTags en macOS mediante la automatización de la interfaz gráfica de FindMy.app, ya que carece de una API oficial. El método combina AppleScript para abrir la aplicación, captura de pantalla para extraer coordenadas y análisis visual para interpretar la ubicación mostrada.

## Datos clave
- **Proyecto**: Skill `findmy` para Hermes Agent (versión 1.0.0).
- **Tecnologías**: macOS, AppleScript (`osascript`), `screencapture`, `vision_analyze`.
- **Herramienta recomendada**: `peekaboo` (instalable vía Homebrew) para una automatización de UI más fiable que la nativa.
- **Permisos críticos**: Se requiere habilitar "Grabación de pantalla" en los ajustes de privacidad del sistema.
- **Comandos principales**:
  - Abrir app: `osascript -e 'tell application "FindMy" to activate'`
  - Capturar imagen: `screencapture -w -o /tmp/findmy.png`
  - Analizar ubicación: `vision_analyze(image_url="...", question="...")`.
- **Limitaciones**: Los AirTags solo actualizan su posición si la pestaña de "Items" permanece activa en primer plano; no existe CLI ni API directa.

## Etiquetas
#macOS #AppleScript #FindMy #AirTag #Automatización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\apple\findmy\SKILL.md`
