---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/marketing-skill-claude-marketing-skill-builder-uzp891/skills/content-calendar/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía define una habilidad de IA para generar calendarios de contenido social en lotes (semanales o mensuales) que eviten la repetición de temas y se guarden como borradores pendientes de aprobación humana. Su función principal es transformar solicitudes genéricas en un plan detallado, etiquetado por plataforma y fecha, listo para ser procesado posteriormente por herramientas de publicación.

## Datos clave
- **Proyecto:** `marketing-skill-claude-marketing-skill-builder`.
- **Tecnologías/Plugins:** Uso de `Read`, `Write`, `WebSearch` y variables de entorno como `CLAUDE_PLUGIN_ROOT`.
- **Flujo de trabajo:** Verificación del estado de configuración (`brand-voice.md`) antes de generar contenido.
- **Lógica de calendario:** Lectura del archivo `state/content-calendar.md` para evitar duplicar temas recientes (últimos 10–15 registros).
- **Validación específica por plataforma:**
    - Reddit/Product Hunt/Hacker News: Requiere investigación activa por slot.
    - Discord/Slack/Telegram: Necesita confirmación inmediata de reglas comunitarias y permisos administrativos antes de redactar.
    - Dev.to: Debe especificarse la identidad (cuenta personal u organización) y las etiquetas.
- **Restricciones:** El sistema nunca publica automáticamente; solo crea filas para aprobación manual.

## Etiquetas
#calendario-de-contenido #marketing-social #automatización #gestión-de-proyectos

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\marketing-skill-claude-marketing-skill-builder-uzp891\skills\content-calendar\SKILL.md`
