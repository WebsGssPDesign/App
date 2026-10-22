---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-image-imitate/README.md"
tags: [hecho]
---
# README.md

## Resumen
Este documento describe la habilidad `sn-image-imitate`, diseñada para imitar el estilo visual de una imagen de referencia mientras se reemplaza su contenido con una descripción objetivo. El flujo de trabajo automatiza la extracción de layout mediante VLM, la reescritura del prompt y la generación iterativa hasta cumplir un umbral de similitud estructural.

## Datos clave
- **Proyecto**: Habilidad `sn-image-imitate` (Tier 1) para OpenClaw/Hermes.
- **Tecnologías**: Python 3.9+, API de SenseNova (`SN_API_KEY`, `SN_BASE_URL`).
- **Dependencias**: Requiere instalación previa de `sn-image-base`.
- **Flujo**: Anotación VLM → Reescritura LLM → Generación + Revisión iterativa.
- **Parámetros críticos**: `reference_image` (requerido), `target_content`, `layout_threshold` (0.75 por defecto).
- **Modos de salida**: `friendly` (breve) o `verbose` (detallado con métricas).
- **Ruta de instalación**: Copiar/simular en `~/.openclaw/skills/` o workspace.

## Etiquetas
#IA #GeneraciónDeImágenes #SenseNova #OpenClaw

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-image-imitate\README.md`
