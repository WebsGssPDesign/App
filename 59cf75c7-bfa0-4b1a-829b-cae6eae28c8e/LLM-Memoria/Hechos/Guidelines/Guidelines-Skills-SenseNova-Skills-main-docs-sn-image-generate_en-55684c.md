---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/docs/sn-image-generate_en.md"
tags: [hecho]
---
# sn-image-generate_en.md

## Resumen
Este documento describe un conjunto de habilidades para generación y edición de imágenes utilizando la API de SenseNova dentro del ecosistema OpenClaw/Hermes. Sirve como guía técnica para configurar el entorno, instalar dependencias y ejecutar tareas específicas como diagnóstico, creación de infografías, diseño de currículums visuales y edición basada en lenguaje natural.

## Datos clave
- **Habilidades principales**: `sn-image-doctor` (diagnóstico), `sn-image-base` (infraestructura base), `sn-infographic`, `sn-image-resume`, `sn-image-imitate`.
- **Requisitos técnicos**: Python 3.9+ (recomendado 3.10), credenciales de API (`SN_API_KEY`, `SN_BASE_URL`).
- **Entrada unificada**: Todas las herramientas se ejecutan mediante `skills/sn-image-base/scripts/sn_agent_runner.py`.
- **Configuración**: Instalación de dependencias vía `pip install -r skills/sn-image-base/requirements.txt` y registro en OpenClaw copiando carpetas a `~/.openclaw/skills/` o configurando `extraDirs` en `openclaw.json`.
- **Comandos de ejemplo**: Uso de `sn-image-edit` con parámetros como `--prompt`, `--images` y `--save-path`.

## Etiquetas
#SenseNova #OpenClaw #GeneraciónDeImágenes #IAVisual

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\docs\sn-image-generate_en.md`
