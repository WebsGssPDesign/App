---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/docs/sn-ppt-generate.md"
tags: [hecho]
---
# sn-ppt-generate.md

## Resumen
Este documento describe un conjunto de habilidades para generar presentaciones (PPT) estáticas, dinámicas y creativas a partir de prompts y documentos. Sirve como guía técnica para configurar el entorno, instalar dependencias y gestionar las credenciales necesarias para ejecutar estas herramientas en los sistemas Hermes o OpenClaw.

## Datos clave
- **Habilidades principales**: `sn-ppt-entry` (entrada), `sn-ppt-story` (esquema obligatorio), `sn-ppt-standard`, `sn-ppt-creative`, `sn-ppt-dazzle` (modo dinámico HTML) y `sn-ppt-workbench`.
- **Requisitos de software**: Python 3.9+ (recomendado 3.10+), Node.js runtime, Chromium y Playwright para renderizado.
- **Instalación crítica**: Ejecutar `bash skills/sn-ppt-standard/scripts/install.sh` para configurar entornos virtuales y fuentes; instalar Chromium manualmente con `npm ... playwright install chromium`.
- **Gestión de claves**: Las APIs nativas del agente no requieren variables, pero si fallan se usan las variables `SN_PPT_SEARCH_API_KEY`, `SN_PPT_IMAGE_GEN_URL` y `SN_PPT_IMAGE_GEN_API_KEY` en el archivo `.env`.
- **Exportación**: El proceso HTML a PPTX requiere un proceso separado de Node.js; puede fallar por falta de bibliotecas compartidas (`libnspr4.so`) si no se ajusta la variable de entorno `LD_LIBRARY_PATH`.

## Etiquetas
#generación-de-presentaciones #automatización-python #herramientas-hermes #documentación-técnica

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\docs\sn-ppt-generate.md`
