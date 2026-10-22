---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/docs/sn-ppt-generate_cn.md"
tags: [hecho]
---
# sn-ppt-generate_cn.md

## Resumen
Este documento describe un conjunto de habilidades para generar presentaciones (PPT) estáticas, dinámicas o creativas utilizando agentes Hermes y OpenClaw. Su función principal es orquestar el flujo desde la entrada de datos hasta la exportación final en formatos HTML o PPTX, gestionando dependencias y herramientas de respaldo.

## Datos clave
- **Proyecto**: `sn-ppt-generate` (Hermes/OpenClaw).
- **Tecnologías**: Python 3.9+, Node.js, Playwright, Chromium, LLM/VLM APIs.
- **Decisiones**: Uso de `sn-ppt-entry` como único punto de entrada; fallback a herramientas nativas o configuradas vía `.env`.
- **Rutas/Comandos**:
  - Instalación: `pip install -r skills/sn-ppt-entry/requirements.txt`, `bash skills/sn-ppt-standard/scripts/install.sh`.
  - Configuración Chromium: `npm --prefix ... exec playwright install chromium`.
  - Variables de entorno críticas: `SN_PPT_SEARCH_API_KEY`, `SN_PPT_IMAGE_GEN_URL`, `SN_PPT_IMAGE_GEN_API_KEY`.

## Etiquetas
#GeneraciónPPT #Automatización #Python #NodeJS

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\docs\sn-ppt-generate_cn.md`
