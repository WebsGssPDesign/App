---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/SiWarlock/AI-System-Of-Work-Assistant-Agent"
tema: "Temporal Workflow Isolation"
tags: [web]
---
# SiWarlock/AI-System-Of-Work-Assistant-Agent

## Resumen
Este proyecto es un sistema operativo personal auto-alojado y local-first para Mac, diseñado como una capa de control gobernable sobre repositorios Markdown compatibles con Obsidian. Su arquitectura prioriza la seguridad mediante validaciones estrictas de datos candidatos antes de escribir cualquier información y mantiene el aislamiento entre diferentes áreas de trabajo (laboral, negocio personal, vida personal). Actualmente se encuentra en fase temprana de desarrollo como base técnica para un asistente autónomo que coordina tareas sin comprometer la propiedad de los datos del usuario.

## Datos clave
- **Principios de seguridad**: "One writer" (`KnowledgeWriter` es el único escritor autónomo), validación JSON-Schema obligatoria para todos los outputs de modelos, y veto a la salida de datos laborales sensibles hacia proveedores en la nube sin autorización explícita.
- **Infraestructura tecnológica**: Electron (UI), TypeScript estricto, Node 22, pnpm + Turbo monorepo, SQLite/Postgres (Drizzle) y Temporal para flujos de trabajo duraderos.
- **Gestión del conocimiento**: Uso de repositorios Git por espacio de trabajo y un índice híbrido llamado "GBrain" derivado de los Markdown; macOS Keychain para gestión de secretos.
- **Aislamiento**: Tres espacios de trabajo aislados (Employer Work, Personal Business, Personal Life) conectados solo mediante una capa de coordinación global sanitizada (GCL).

## Etiquetas
#InteligenciaArtificialLocal #AutomatizaciónPersonal #SeguridadInformática #Obsidian #Electron

Fuente: https://github.com/SiWarlock/AI-System-Of-Work-Assistant-Agent
