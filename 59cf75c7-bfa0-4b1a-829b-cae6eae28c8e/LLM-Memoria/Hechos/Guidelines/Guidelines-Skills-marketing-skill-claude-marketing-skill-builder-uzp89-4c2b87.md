---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/marketing-skill-claude-marketing-skill-builder-uzp891/skills/content-repurposer/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía define una habilidad de IA para transformar un solo contenido fuente (artículos, notas o URLs) en tres formatos nativos: publicación de LinkedIn, hilo de Twitter/X y resumen para newsletter. Su objetivo es mantener la fidelidad factual y el tono de marca mientras adapta la estructura a cada canal específico.

## Datos clave
- **Proyecto**: `content-repurposer` dentro del conjunto de habilidades de marketing.
- **Herramientas permitidas**: Read, Grep, Glob, WebFetch, Write.
- **Flujo de trabajo crítico**:
  1. Verificar configuración en `${CLAUDE_PLUGIN_ROOT}/references/brand-voice.md`. Si no existe o está desconfigurada, pausar y preguntar al usuario sobre el tono, audiencia y formato por defecto antes de guardar las respuestas.
  2. Identificar el contenido fuente (texto pegado, archivo, URL o búsqueda en `README*`, `CHANGELOG*`, `docs/**/*.md`).
  3. Extraer tesis central y datos sin inventar nada nuevo.
  4. Redactar los tres formatos aplicando restricciones de palabras prohibidas del archivo de voz de marca.
- **Estructura de salida obligatoria**:
  - LinkedIn: Gancho independiente, párrafos cortos, CTA suave y 3–5 hashtags.
  - Twitter/X: Hilo numerado (1/, 2/...), primer tweet como gancho, límite de 280 caracteres por tweet, CTA en el último.
  - Newsletter: Línea de asunto sugerida, intro breve, viñetas y enlace único al final.

## Etiquetas
#marketing #repurposing #social-media #content-strategy

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\marketing-skill-claude-marketing-skill-builder-uzp891\skills\content-repurposer\SKILL.md`
