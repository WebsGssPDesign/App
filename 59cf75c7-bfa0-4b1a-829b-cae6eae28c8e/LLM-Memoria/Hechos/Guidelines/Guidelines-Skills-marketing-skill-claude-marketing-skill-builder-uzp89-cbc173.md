---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/marketing-skill-claude-marketing-skill-builder-uzp891/skills/full-pipeline/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este archivo define una habilidad de IA para ejecutar campañas de marketing completas en un solo paso, integrando investigación, creación de contenido y publicación. Su función principal es orquestar automáticamente cuatro etapas distintas (investigación, reutilización de contenido, breves visuales y publicación) tras obtener la aprobación explícita del usuario antes de enviar cualquier material a redes sociales.

## Datos clave
- **Proyecto:** `full-pipeline` dentro del plugin de habilidades de marketing.
- **Tecnologías/Tools:** WebSearch, WebFetch, Read, Grep, Glob, Write, Edit, Bash.
- **Flujo de trabajo:** 1) Verificación de configuración (onboarding), 2) Confirmación de alcance, 3) Investigación de competidores, 4) Reutilización de contenido, 5) Generación de breves visuales (según plataforma), 6) Punto de control obligatorio con aprobación humana, 7) Publicación vía webhook.
- **Rutas críticas:** `${CLAUDE_PLUGIN_ROOT}/references/brand-voice.md` para configuración y estado; `state/posts/<date>-<platform-slug>.md` para guardar borradores si no hay aprobación.
- **Comandos clave:** `printenv CLAUDE_PLUGIN_ROOT`, uso de `content-calendar` para gestionar filas con estado "Ready for Approval".

## Etiquetas
#marketing #automatización #flujo-trabajo #aprobación-humana

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\marketing-skill-claude-marketing-skill-builder-uzp891\skills\full-pipeline\SKILL.md`
