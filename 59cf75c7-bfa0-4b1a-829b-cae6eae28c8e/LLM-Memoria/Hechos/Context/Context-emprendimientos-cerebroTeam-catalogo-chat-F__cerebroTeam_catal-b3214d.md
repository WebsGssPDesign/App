---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/cerebroTeam/catalogo-chat/F__cerebroTeam_catalogo-chat_README.md"
tags: [hecho]
---
# F__cerebroTeam_catalogo-chat_README.md

## Resumen
Este documento describe una aplicación web completa de chat impulsada por IA que ejecuta modelos locales mediante LM Studio, gestionando datos en PostgreSQL y una interfaz React. Su función principal es permitir la interacción con un modelo de lenguaje local utilizando técnicas RAG para búsqueda contextual y streaming de respuestas en tiempo real.

## Datos clave
- **Tecnologías**: Node.js (Backend Express), React + Vite (Frontend), PostgreSQL 18.4 con pgvector, LM Studio.
- **Puertos críticos**: Backend 3000, Frontend 5173, PostgreSQL 5433, LM Studio 1234.
- **Flujo RAG**: Generación de embeddings → Búsqueda en BD → Construcción de prompt → Streaming vía Server-Sent Events (SSE).
- **Comandos esenciales**: `npm install`, `node scripts/migrate.js`, `psql -h localhost -p 5433 -U postgres`.
- **Endpoints principales**: POST `/api/chat` (con streaming), GET/POST/DELETE `/api/conversations`.

## Etiquetas
#IA #React #PostgreSQL #LMStudio #RAG

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\cerebroTeam\catalogo-chat\F__cerebroTeam_catalogo-chat_README.md`
