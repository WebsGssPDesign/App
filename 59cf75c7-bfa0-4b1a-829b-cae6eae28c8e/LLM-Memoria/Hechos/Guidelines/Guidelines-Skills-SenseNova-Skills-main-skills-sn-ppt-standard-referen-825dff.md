---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-ppt-standard/references/fonts.md"
tags: [hecho]
---
# fonts.md

## Resumen
Este documento establece las directrices técnicas para la gestión de fuentes tipográficas en proyectos de presentaciones, priorizando el uso de licencias abiertas (OFL) y la seguridad jurídica sobre la estética. Su función es garantizar que los archivos sean autocontenidos, verificables y adaptables a diversos contextos sin depender de instalaciones locales del usuario.

## Datos clave
- **Proyecto**: SenseNova-Skills (sn-ppt-standard).
- **Requisitos legales**: Todas las fuentes deben tener licencia OFL-1.1 o ser subidas explícitamente por el usuario con derechos confirmados; se registran en `font_bundle.py`.
- **Restricciones de uso**: El archivo final no debe depender de fuentes locales del sistema ni usar CDN externas. Las fuentes personalizadas deben renombrarse como `Deck-*` al construirse.
- **Límite estricto**: Máximo 3 familias tipográficas por todo el documento (título, cuerpo y acentos).
- **Reglas de asignación**:
    - `--font-sans`: Texto principal, tablas y metadatos (Noto Sans SC).
    - `--font-mono`: Únicamente para código, coordenadas y números latinos; prohibido para texto chino.
    - `--font-number`: Mapeado semántico según el tipo de contenido (reporte, editorial o ingeniería).
- **Tipografía china**: Siempre debe tener Noto Sans/Serif SC como respaldo para evitar caracteres vacíos.

## Etiquetas
#tipografia #licencias #guia_de_estilo #senonenova

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-ppt-standard\references\fonts.md`
