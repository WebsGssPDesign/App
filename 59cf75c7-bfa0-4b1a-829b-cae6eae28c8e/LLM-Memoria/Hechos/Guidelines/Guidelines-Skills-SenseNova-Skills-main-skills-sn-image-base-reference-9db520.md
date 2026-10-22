---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-image-base/references/api_spec.md"
tags: [hecho]
---
# api_spec.md

## Resumen
Este documento define la especificación de la API para herramientas de procesamiento de imágenes del proyecto SenseNova, incluyendo generación, edición y reconocimiento visual. Sirve como guía técnica para configurar comandos, gestionar parámetros de modelos y manejar errores en entornos de automatización.

## Datos clave
- **Herramientas principales**: `sn-image-generate` (generación), `sn-image-edit` (edición con U1.5 Lite) y `sn-image-recognize` (análisis VLM).
- **Ejecución**: Uso del script `python sn_agent_runner.py` seguido del subcomando específico.
- **Parámetros críticos**: `--prompt`, `--api-key` (precedencia CLI > entorno), `--image-size` (2k/4k según modelo) y `--aspect-ratio`.
- **Modelos y tipos VLM**: Soporte para `sensenova-u1.5-lite`, `sensenova-6.8-flash-lite` y tipos de API compatibles con OpenAI o Anthropic.
- **Manejo de errores**: Lanzamiento de `MissingApiKeyError` si no se proporcionan credenciales válidas en ninguna fuente configurada.

## Etiquetas
#SenseNova #API-Specification #ImageProcessing #Automation

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-image-base\references\api_spec.md`
