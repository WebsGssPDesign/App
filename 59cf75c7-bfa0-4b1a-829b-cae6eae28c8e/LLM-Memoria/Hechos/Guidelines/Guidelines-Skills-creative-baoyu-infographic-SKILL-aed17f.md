---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/baoyu-infographic/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía define un sistema para generar infografías automatizadas combinando 21 estructuras de diseño con 21 estilos visuales. Sirve como referencia técnica para agentes que deben transformar texto o datos en imágenes informativas, asegurando la fidelidad del contenido y protegiendo credenciales sensibles.

## Datos clave
- **Proyecto**: baoyu-infographic (adaptado para Hermes Agent).
- **Tecnologías**: Soporte multiplataforma (Linux, macOS, Windows), generación de imágenes.
- **Decisiones**: Combinación libre de layout y style; uso de keywords para auto-selección automática.
- **Rutas importantes**: `references/layouts/<layout>.md`, `references/styles/<style>.md`.
- **Comandos/pasos clave**:
  - Paso 1: Analizar contenido y cargar marcos de referencia (`references/analysis-framework.md`).
  - Limpieza obligatoria: Eliminar credenciales, claves API o tokens antes del procesamiento.
  - Salida estructurada en `infographic/{topic-slug}/` con archivos fuente, análisis y la imagen final `.png`.

## Etiquetas
#visualización #automatización #diseño-gráfico

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\baoyu-infographic\SKILL.md`
