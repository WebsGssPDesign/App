---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/proyectosInconclusos/Nueva carpeta/ia/README.md"
tags: [hecho]
---
# README.md

## Resumen
Esta nota documenta una aplicación web local que permite chatear con un modelo de IA ejecutado en el dispositivo del usuario, utilizando LM Studio y PostgreSQL para persistir el historial. El sistema ofrece una interfaz moderna sin autenticación y funciona completamente offline mediante tecnologías Node.js y React.

## Datos clave
- **Proyecto**: Aplicación de chat local con IA (sin login).
- **Tecnologías**: Node.js/Express, React, PostgreSQL 18.4 (con pgvector), LM Studio.
- **Modelo IA**: `qwen2.5-coder-3b-claude_opus_4.6-distilled`.
- **Rutas y comandos**:
  - Inicializar DB: `cd server && npm run init-db`
  - Instalar dependencias: `npm install` (en directorios `/server` y `/client`)
  - Ejecutar backend: `npm start` o `npm run dev`
  - Ejecutar frontend: `npm run dev`
- **Endpoints principales**: `POST /api/chat/message`, `GET /api/chat/history/:sessionId`.
- **Configuración crítica**: Puerto de PostgreSQL (5433), puerto LM Studio (1234) y puerto del servidor (3000).

## Etiquetas
#IA #LocalDev #NodeJS #React #PostgreSQL

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\proyectosInconclusos\Nueva carpeta\ia\README.md`
