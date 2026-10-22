---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/SpillwaveSolutions/mastering-postgresql-agent-skill"
tema: "PostgreSQL JSONB Indexing"
tags: [web]
---
# SpillwaveSolutions/mastering-postgresql-agent-skill

## Resumen
Este repositorio documenta el desarrollo avanzado de PostgreSQL para Python, enfocándose en búsquedas de texto completo, similitud vectorial con pgvector y optimización mediante índices JSONB. Incluye guías prácticas para la instalación en diversos entornos de agentes de IA y despliegue en la nube (AWS, GCP, Azure).

## Datos clave
- **Tecnologías**: PostgreSQL, Python (psycopg2, asyncpg, SQLAlchemy), pgvector, ParadeDB.
- **Índices**: GIN para texto completo y JSONB; HNSW e IVFFlat para vectores.
- **Instalación**: Uso del instalador universal `skilz` con opciones de agente (Claude Code, Gemini, OpenAI Codex) o proyecto (`--project`).
- **Comandos**: `pip install skilz`, `skilz install -g <URL>`, `skilz install --agent <nombre>`.
- **Estructura**: Archivos de configuración Docker, scripts Python para búsqueda y operaciones masivas, plantillas SQL.

## Etiquetas
#PostgreSQL #Python #pgvector #BúsquedaVectorial #DespliegueEnLaNube

Fuente: https://github.com/SpillwaveSolutions/mastering-postgresql-agent-skill
