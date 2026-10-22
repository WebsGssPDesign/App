---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-image-base/README.md"
tags: [hecho]
---
# README.md

## Resumen
Este documento detalla la configuración y los subcomandos de la habilidad `sn-image-base` del proyecto SenseNova-Skills, diseñada para generar imágenes, editarlas, reconocerlas mediante VLM y optimizar texto. Sirve como guía técnica para configurar las variables de entorno necesarias y seleccionar modelos específicos de proveedores como SenseNova, Anthropic o OpenAI.

## Datos clave
- **Subcomandos**: `sn-image-generate`, `sn-image-edit`, `sn-image-recognize`, `sn-text-optimize`.
- **Modelos soportados**: SenseNova (U1.5 Lite), Nano Banana API, GPT-Image-2, Claude Sonnet 4.6 y modelos compatibles de OpenAI.
- **Variables críticas**: `SN_BASE_URL` (ej. `https://token.sensenova.cn/v1`) y `SN_API_KEY`.
- **Configuración avanzada**: Uso de `.env` en `~/.openclaw/` o `~/.hermes/`, con prioridad sobre variables de proceso.
- **Tipos de generación**: `sensenova`, `nano-banana`, `openai-image`.

## Etiquetas
#SenseNova #GeneraciónDeImágenes #ConfiguraciónAPI #IAVisual

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-image-base\README.md`
