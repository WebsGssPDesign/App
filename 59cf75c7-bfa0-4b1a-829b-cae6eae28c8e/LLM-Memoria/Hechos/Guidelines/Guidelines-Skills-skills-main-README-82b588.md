---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/skills-main/README.md"
tags: [hecho]
---
# README.md

## Resumen
Este archivo define dos habilidades para Claude que generan explicaciones breves o páginas HTML resumidas, enfocándose en el resultado deseado más que en las palabras usadas. Sirve para estandarizar la creación de documentación visual y textual accesible sin necesidad de pasos de compilación complejos.

## Datos clave
- **Proyecto**: `skills` (paquete de habilidades para Claude).
- **Tecnologías**: HTML, SVG inline, Git (`git status`, `log`, `diff`).
- **Decisiones**: El sistema lee el estado real del repositorio antes de generar el resumen; no usa frameworks ni dependencias externas.
- **Rutas**: `skills/eli5-succinct/SKILL.md` y `skills/summary/SKILL.md`.
- **Comandos de instalación**: `cp -r skills/eli5-succinct ~/.claude/skills/` y `cp -r skills/summary ~/.claude/skills/`.
- **Modos disponibles**: Accessible (amigable para ADHD), Artistic, Animated.

## Etiquetas
#documentación #automatización #html #claude-skills

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\skills-main\README.md`
