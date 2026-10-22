---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-ppt-doctor/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define la habilidad `sn-ppt-doctor`, una herramienta de diagnóstico para verificar el entorno de configuración y dependencias del proyecto SenseNova-Skills, específicamente relacionadas con la generación de PPT. Su función es reportar el estado de herramientas nativas (Agent) y empaquetadas (Bundled), validando APIs de búsqueda e imagen, motores de renderizado como Playwright/Chromium y exportadores HTML a PPTX sin modificar archivos ni instalar dependencias automáticamente.

## Datos clave
- **Proyecto**: SenseNova-Skills (Tier: aux).
- **Comandos principales**: `python3 "$SKILL_DIR/ppt_doctor/check_environment.py"`, con opciones `--probe-search` y `--probe-image-generation`.
- **Variables de entorno críticas**: `SN_PPT_SEARCH_API_KEY`, `SN_PPT_IMAGE_GEN_URL`, `SN_PPT_IMAGE_GEN_API_KEY`, `SN_PPT_ENV_FILE`.
- **Rutas de configuración**: `~/.hermes/.env`, `~/.openclaw/.env`.
- **Lógica de estado**: Clasifica herramientas en `absent`, `present_unverified`, `misconfigured` o `available` basándose en pruebas reales, no solo en la presencia del script.
- **Dependencias verificadas**: Playwright, Chromium, Node.js, `pptxgenjs`, `python-pptx`.

## Etiquetas
#diagnóstico #SenseNova-Skills #PPTX #Playwright #automatización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-ppt-doctor\SKILL.md`
