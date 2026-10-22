---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/docs/sn-team-harness.md"
tags: [hecho]
---
# sn-team-harness.md

## Resumen
Este documento describe SenseNova Team Harness, un marco de colaboración auto-alojado que permite a personas y agentes locales compartir contexto, proyectos y artefactos versionados. Su función principal es facilitar la gestión del ciclo de vida del trabajo mediante una estructura organizada de espacios de trabajo, tareas y recursos, sin reemplazar el tiempo de ejecución de los agentes.

## Datos clave
- **Proyecto**: SenseNova Team Harness (auto-alojado).
- **Tecnologías**: Node.js 24, npm, SQLite, Git.
- **Rutas y comandos**: `git clone`, `npm ci`, `npm run dev` (desarrollo) o `NODE_ENV=production npm start`.
- **Conceptos principales**: Workspace (fuente de verdad), Project, Agent, WorkItem, Resource, Artifact, Local Computer.
- **Flujo básico**: Creación de workspace y proyectos, vinculación de agentes a computadoras locales, ejecución de tareas y revisión de artefactos con control de concurrencia.
- **Seguridad**: Requiere autenticación, TLS y rotación de secretos antes del despliegue; no incluir credenciales ni archivos `.env` en el repositorio.

## Etiquetas
#SenseNova #AutoAlojado #ColaboracionIA #NodeJS #GestionDeProyectos

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\docs\sn-team-harness.md`
