---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/software-development/hermes-agent-skill-authoring/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía define los estándares para crear y mantener archivos SKILL.md dentro del repositorio de Hermes Agent, asegurando consistencia en la estructura, validación automática y calidad del contenido. Su objetivo es mejorar la predictibilidad del proceso del agente al establecer reglas claras sobre metadatos obligatorios, límites de longitud y principios de redacción efectiva.

## Datos clave
- **Ubicación:** Archivos deben residir en `/home/bb/hermes-agent/skills/<categoría>/<nombre>/SKILL.md`.
- **Herramientas:** Se usa `write_file` para crear o reescribir, `patch` para ediciones pequeñas y `git add` para commits. La herramienta `skill_manage(action='create')` solo funciona en el árbol local del usuario.
- **Validación de Frontmatter:** El archivo debe comenzar con `---`, incluir campos obligatorios (`name`, `description` ≤ 1024 caracteres) y cerrar correctamente antes del cuerpo.
- **Límites de tamaño:** La descripción máxima es de 1024 caracteres; el contenido total no debe superar los 100,000 caracteres (aprox. 36k tokens). Las habilidades pares suelen tener entre 8k y 14k caracteres.
- **Principios de escritura:** Optimizar para predictibilidad del proceso, usar jerarquías de información (mover referencias voluminosas a carpetas `references/`) y terminar cada paso con criterios de finalización verificables.
- **Estructura recomendada:** Secciones obligatorias incluyen "Overview", "When to Use", cuerpo accionable, "Common Pitfalls" y una lista de verificación de validación.

## Etiquetas
#hermes-agent #skills-authoring #guidelines #software-development

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\software-development\hermes-agent-skill-authoring\SKILL.md`
