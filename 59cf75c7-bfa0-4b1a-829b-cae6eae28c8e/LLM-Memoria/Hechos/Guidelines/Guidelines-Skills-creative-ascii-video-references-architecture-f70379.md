---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/ascii-video/references/architecture.md"
tags: [hecho]
---
# architecture.md

## Resumen
Este documento define la arquitectura de referencia para un sistema de video ASCII, estableciendo estándares para resoluciones, sistemas de rejilla adaptativos y selección de fuentes. Su objetivo es garantizar una renderización consistente y optimizada en múltiples formatos (horizontal, vertical y cuadrado) utilizando caracteres pre-rasterizados.

## Datos clave
- **Resoluciones**: Presets definidos para landscape (1920x1080), portrait (1080x1920), square (1080x1080) y versiones 4K.
- **Sistema de rejilla**: Cálculo automático de columnas y filas basado en la resolución; diferencias específicas para modo retrato (menos columnas, más filas).
- **Fuentes**: Listado de fuentes monoespaciadas por plataforma (Menlo, Consolas, DejaVu Sans Mono) con lógica de detección automática.
- **Caracteres**: Recolección global de todos los caracteres necesarios antes de la inicialización para pre-rasterización en múltiples paletas.

## Etiquetas
#ascii-art #video-rendering #grid-system #font-selection

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\ascii-video\references\architecture.md`
