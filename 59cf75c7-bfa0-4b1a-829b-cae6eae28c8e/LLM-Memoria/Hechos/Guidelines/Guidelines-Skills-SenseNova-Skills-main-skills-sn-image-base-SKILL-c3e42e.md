---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-image-base/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe la capa base de habilidades `sn-image-base` del proyecto SenseNova-Skills, diseñada para ofrecer APIs de bajo nivel que llaman a servicios externos sin realizar preprocesamiento. Su función es facilitar operaciones como generación, edición y reconocimiento de imágenes, así como optimización de texto, exclusivamente para ser utilizadas por otras habilidades superiores.

## Datos clave
- **Proyecto**: SenseNova-Skills (Capa 0 / Tier 0).
- **Herramientas principales**: `sn-image-generate` (generación), `sn-image-edit` (edición con U1.5 Lite), `sn-image-recognize` (reconocimiento VLM) y `sn-text-optimize`.
- **Instalación**: `pip install -r requirements.txt`.
- **Parámetros críticos**: Uso de claves API (`SN_IMAGE_GEN_API_KEY`, etc.) con prioridad en argumentos CLI; soporte para modelos como `sensenova-u1.5-lite` (4K) y `sensenova-6.8-flash-lite`.
- **Comandos de ejemplo**: Ejecución vía `python scripts/sn_agent_runner.py` con flags específicos para prompts, rutas de imágenes y guardado.
- **Restricciones**: No acepta entradas preprocesadas; requiere que las claves API estén configuradas o se lancen errores `MissingApiKeyError`.

## Etiquetas
#SenseNova #IA #APIs #Imagenes #LLM

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-image-base\SKILL.md`
