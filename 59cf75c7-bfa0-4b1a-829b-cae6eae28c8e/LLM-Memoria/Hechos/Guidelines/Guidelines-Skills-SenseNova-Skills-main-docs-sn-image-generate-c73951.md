---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/docs/sn-image-generate.md"
tags: [hecho]
---
# sn-image-generate.md

## Resumen
Este documento describe un conjunto de habilidades para generación y edición de imágenes utilizando la API de SenseNova, integrables en entornos como OpenClaw o Hermes. Sirve como guía técnica para configurar el entorno, gestionar credenciales y ejecutar flujos de trabajo avanzados como la creación de infografías, currículums visuales o imitación de estilos artísticos específicos.

## Datos clave
- **Habilidades principales**: `sn-image-doctor` (diagnóstico), `sn-image-base` (herramientas base: generación, edición, reconocimiento VLM), `sn-infographic`, `sn-image-resume`, `sn-image-imitate`.
- **Entrada unificada**: Todos los scripts se ejecutan vía `skills/sn-image-base/scripts/sn_agent_runner.py`.
- **Configuración de entorno**: Se requieren variables `SN_BASE_URL` y `SN_API_KEY` (soporte para regiones China y Overseas).
- **Instalación en OpenClaw/Hermes**: Copiar el directorio `skills/` a `~/.openclaw/skills/` o usar `extraDirs` en `openclaw.json`.
- **Dependencias**: Python 3.9+ e instalación vía `pip install -r skills/sn-image-base/requirements.txt`.

## Etiquetas
#SenseNova #GeneraciónDeImágenes #OpenClaw #IAVisual

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\docs\sn-image-generate.md`
