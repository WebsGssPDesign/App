---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/haritron/CRON_JOB"
tema: "Temporal Cloud Native Observability"
tags: [web]
---
# haritron/CRON_JOB

## Resumen
CRON_JOB es una plataforma de observabilidad nativa en la nube diseñada para monitorizar y analizar scripts de cron, automatizaciones y pipelines de fondo en tiempo real. El sistema actúa como un entorno seguro que captura telemetría de alta resolución y utiliza inteligencia artificial (Gemini) para generar análisis de causa raíz y guías de remediación automáticamente.

## Datos clave
- **Tecnologías**: React 19, Fastify, PostgreSQL/SQLite, Apache Kafka, Redis, Temporal, Kubernetes.
- **Integración AI**: Gemini 2.5 Flash API para narrativas diagnósticas de SRE.
- **Seguridad**: Sandbox con `shell=False`, listas permitidas de comandos y autenticación JWT.
- **Resiliencia**: Adaptadores de respaldo (mocks) que permiten ejecución offline si fallan servicios como Temporal, Redis o Kafka.
- **Comandos principales**: `docker-compose up -d` para infraestructura real; `npm run dev` para desarrollo local.
- **Credenciales de prueba**: Email: `sre@government.gov`, Contraseña: `password123`.

## Etiquetas
#Observabilidad #SRE #Kubernetes #AI_Diagnostics #DevOps

Fuente: https://github.com/haritron/CRON_JOB
