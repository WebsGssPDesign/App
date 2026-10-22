---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/cerebroTeam/catalogo-chat/F__cerebroTeam_catalogo-chat_SUMMARY.md"
tags: [hecho]
---
# F__cerebroTeam_catalogo-chat_SUMMARY.md

## Resumen
Este documento detalla una aplicación web completa de chat con IA local, diseñada para funcionar sin dependencias externas. Integra un backend en Node.js con RAG y embeddings vectoriales, conectándose a un modelo local vía LM Studio y almacenando datos en PostgreSQL. El frontend, desarrollado con React y CSS puro, permite la interacción en tiempo real mediante streaming.

## Datos clave
- **Proyecto**: Aplicación de chat IA para catálogo (cerebroTeam).
- **Tecnologías**: Node.js/Express, React/Vite, PostgreSQL 18.4 (pgvector), LM Studio.
- **Rutas y Endpoints**: `/api/chat` (POST streaming), `/api/conversations` (GET/POST/DELETE).
- **Comandos de inicio**: `START.bat` (automático) o ejecución manual en puertos 3000 (backend) y 5173 (frontend).
- **Componentes críticos**: `services/rag.js` (búsqueda contextual), `hooks/useChat.js`, `config.js`.
- **Personalización**: Modificación de variables CSS en `reset.css` para temas y edición del prompt sistema en `rag.js`.

## Etiquetas
#IA #React #NodeJS #RAG #PostgreSQL

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\cerebroTeam\catalogo-chat\F__cerebroTeam_catalogo-chat_SUMMARY.md`
