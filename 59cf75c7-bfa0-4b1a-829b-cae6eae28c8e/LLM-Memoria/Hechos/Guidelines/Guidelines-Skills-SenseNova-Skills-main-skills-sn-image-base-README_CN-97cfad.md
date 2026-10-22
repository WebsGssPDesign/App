---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-image-base/README_CN.md"
tags: [hecho]
---
# README_CN.md

## Resumen
Este documento detalla la configuración del módulo `sn-image-base` del proyecto SenseNova-Skills, diseñado para orquestar capacidades de generación y edición de imágenes, reconocimiento visual (VLM) y optimización de texto mediante APIs. Sirve como guía técnica para configurar entornos locales, gestionar claves API y seleccionar modelos específicos para diferentes proveedores como SenseNova, OpenAI o Anthropic.

## Datos clave
- **Proyecto**: SenseNova-Skills (`sn-image-base`).
- **Comandos principales**: `sn-image-generate`, `sn-image-edit`, `sn-image-recognize`, `sn-text-optimize`.
- **Configuración de entorno**: Variables en `~/.openclaw/.env` o `~/.hermes/.env` (ej. `SN_BASE_URL`, `SN_API_KEY`).
- **Modelos soportados**: SenseNova U1.5 Lite, GPT-Image-2, Gemini 3.1 Flash Image Preview, Claude Sonnet 4.6.
- **Protocolos compatibles**: OpenAI (`/chat/completions`), Anthropic (`/messages`).
- **Jerarquía de configuración**: Variables específicas > variables compartidas por dominio > variables globales.

## Etiquetas
#SenseNova #IA #ConfiguraciónAPI #GeneraciónDeImágenes

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-image-base\README_CN.md`
