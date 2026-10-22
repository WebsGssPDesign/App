---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-ppt-standard/references/layout-patterns.md"
tags: [hecho]
---
# layout-patterns.md

## Resumen
Este documento define un patrón de diseño modular para diapositivas basándose en HTML y CSS, enfocado en la reutilización de estructuras dentro del contenedor `.slide-body`. Su objetivo es estandarizar layouts complejos como líneas de tiempo, comparativas y métricas clave, asegurando consistencia visual sin copiar plantillas rígidas.

## Datos clave
- **Proyecto**: Sistema de diseño para presentaciones (SenseNova).
- **Tecnologías**: HTML5, CSS3 (Grid, Flexbox), variables CSS (`--gutter`, `--accent`).
- **Reglas críticas**: Usar solo tokens de `base.css`; evitar texto plano hex; máximo 6 nodos por línea de tiempo.
- **Layouts principales**:
    - `.tl`: Estructura de línea de tiempo con alineación vertical.
    - `.kpi-row`: Filas de indicadores numéricos con unidades escaladas.
    - `.split-media`: Disposición texto-imagen con recorte focal (`crop_contract`).
    - `.hero-figure`: Páginas rompedoras para énfasis visual en números grandes.
- **Restricciones**: No usar imágenes falsas o AI para rostros; priorizar la integridad del sujeto sobre el llenado de espacio.

## Etiquetas
#diseño-de-presentaciones #html-css #guias-de-estilo

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-ppt-standard\references\layout-patterns.md`
