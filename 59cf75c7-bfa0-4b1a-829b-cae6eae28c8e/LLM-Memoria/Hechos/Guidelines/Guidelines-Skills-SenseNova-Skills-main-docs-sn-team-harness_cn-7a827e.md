---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/docs/sn-team-harness_cn.md"
tags: [hecho]
---
# sn-team-harness_cn.md

## Resumen
Este documento describe SenseNova Team Harness, un marco de trabajo auto-alojado para que humanos y agentes locales compartan contexto y proyectos. Su función es facilitar la colaboración mediante una arquitectura donde los agentes se ejecutan localmente en las computadoras de los miembros del equipo, gestionando tareas, recursos y resultados versionados sin depender de un runtime centralizado.

## Datos clave
- **Tecnologías**: Node.js 24, npm, SQLite (implícito).
- **Rutas de instalación**: `git clone`, `npm ci`, `npm run dev`.
- **Comandos de producción**: `npm run build` seguido de `NODE_ENV=production npm start`.
- **Conceptos principales**: Workspace, Project, Conversation, Agent, WorkItem, Resource, Artifact.
- **Flujo crítico**: Crear workspace -> Invitar miembros -> Vincular Agent a Local Computer -> Ejecutar tareas locales -> Gestionar conflictos de escritura (retry/discard/force).
- **Advertencia de seguridad**: El proyecto no incluye autenticación ni TLS por defecto; requiere configuración manual antes del uso en producción.

## Etiquetas
#auto-alojado #agentes-locales #colaboracion #nodejs #seguridad

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\docs\sn-team-harness_cn.md`
