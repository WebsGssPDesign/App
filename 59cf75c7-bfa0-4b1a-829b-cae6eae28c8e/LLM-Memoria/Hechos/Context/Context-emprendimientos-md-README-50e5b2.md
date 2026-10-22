---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/.md/README.md"
tags: [hecho]
---
# README.md

## Resumen
Este documento describe un agente de ventas y marketing local y gratuito para GSSP Mini Market, diseñado para funcionar offline sin costos de API. Su propósito es automatizar tareas comerciales como el cálculo de precios, análisis de catálogos en PDF e imágenes, utilizando modelos de lenguaje ejecutados localmente.

## Datos clave
- **Proyecto**: Agente de IA para GSSP Sales & Marketing (GSSP Mini Market).
- **Tecnologías**: Python 3.10+, LM Studio (localhost:1234), Qwen2.5 14B Instruct, GLM-4.6V Flash.
- **Instalación**: Ejecutar `powershell -ExecutionPolicy Bypass -File setup.ps1`.
- **Comandos principales**: `/precio`, `/pdf`, `/json`, `/imagen`, `/guardar`, `/nuevo`, `/ayuda`.
- **Configuración crítica**: Ajustar `MODELO_TEXTO` y `MODELO_VISION` en `agente.py` (líneas 23-24) con los nombres exactos de LM Studio.
- **Requisitos hardware**: Recomendado para RTX 3060 12GB + 16GB RAM.

## Etiquetas
#IA #MarketingLocal #Python #OpenSource

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\.md\README.md`
