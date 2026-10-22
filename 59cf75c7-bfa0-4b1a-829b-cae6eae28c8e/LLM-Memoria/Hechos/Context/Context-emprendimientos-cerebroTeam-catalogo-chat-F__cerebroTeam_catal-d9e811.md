---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/cerebroTeam/catalogo-chat/F__cerebroTeam_catalogo-chat_SETUP.md"
tags: [hecho]
---
# F__cerebroTeam_catalogo-chat_SETUP.md

## Resumen
Este documento guía la configuración completa de un sistema de chat impulsado por IA, integrando PostgreSQL para almacenamiento, LM Studio como motor de inferencia y una aplicación web desarrollada con Node.js y React. Su objetivo es permitir el despliegue local paso a paso del backend, frontend y base de datos, facilitando tanto la instalación manual como el uso de un script automatizado.

## Datos clave
- **Servicios requeridos**: PostgreSQL 18.4 (puerto 5433), LM Studio (puerto 1234, modelo `qwen2.5-coder-3b`), Node.js 16+.
- **Base de datos**: Creación y migración automática en la base `ia` con tablas para conversaciones, mensajes y productos.
- **Backend**: Servidor Express en puerto 3000 que conecta con LM Studio vía API y PostgreSQL.
- **Frontend**: Aplicación React/Vite en puerto 5173 que consume el backend localmente.
- **Comandos principales**: `npm install`, `npm run dev` (backend y frontend), `START.bat` (atajo rápido Windows).
- **Verificación**: Endpoints de salud (`/api/health`) y pruebas manuales de conexión entre componentes.

## Etiquetas
#setup #chat-ia #postgresql #nodejs #react

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\cerebroTeam\catalogo-chat\F__cerebroTeam_catalogo-chat_SETUP.md`
