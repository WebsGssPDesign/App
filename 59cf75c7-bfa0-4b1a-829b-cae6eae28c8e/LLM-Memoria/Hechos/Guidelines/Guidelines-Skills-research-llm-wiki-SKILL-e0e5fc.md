---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/research/llm-wiki/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define el protocolo para construir y mantener una base de conocimientos persistente basada en archivos Markdown interconectados, alternativa al RAG tradicional. Su función es permitir que un agente sintetice información curada por humanos, organizándola en capas estructuradas (fuentes crudas, entidades/conceptos y esquema) para facilitar la consulta y el análisis continuo sin perder contexto.

## Datos clave
- **Proyecto**: Karpathy's LLM Wiki (versión 2.1.0).
- **Tecnologías**: Markdown puro, enlaces cruzados `[[wikilinks]]`, YAML frontmatter.
- **Rutas críticas**: `$WIKI_PATH` (por defecto `~/wiki`), estructura con carpetas `raw/`, `entities/`, `concepts/`.
- **Archivos obligatorios**: `SCHEMA.md` (reglas de dominio), `index.md` (catálogo), `log.md` (registro cronológico).
- **Pasos de inicialización**: Determinar ruta, crear estructura, definir dominio, escribir `SCHEMA.md`, `index.md` y `log.md`.
- **Flujo de trabajo**: El humano ingesta fuentes a `raw/`; el agente crea páginas en capas 2 y mantiene consistencia.
- **Comandos de orientación**: Leer `SCHEMA.md`, `index.md` y los últimos 30 líneas de `log.md` antes de cualquier acción.

## Etiquetas
#bases-de-conocimiento #markdown #agente-inteligente #investigación #organización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\research\llm-wiki\SKILL.md`
