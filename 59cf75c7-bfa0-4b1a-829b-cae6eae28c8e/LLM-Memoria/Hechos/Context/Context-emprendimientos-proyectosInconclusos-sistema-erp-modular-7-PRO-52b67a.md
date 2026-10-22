---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/proyectosInconclusos/sistema-erp-modular (7)/PRODUCTION_ARCHITECTURE.md"
tags: [hecho]
---
# PRODUCTION_ARCHITECTURE.md

## Resumen
Este documento describe la arquitectura de producción para un sistema ERP modular con IA, diseñado para operar 24/7 en un HomeLab. Detalla una topología basada en microservicios que integra bases de datos vectoriales y colas de tareas para garantizar resiliencia y escalabilidad local. Su objetivo es guiar la migración desde un prototipo in-memory a una infraestructura robusta utilizando hardware específico.

## Datos clave
- **Proyecto**: Sistema ERP Inteligente Multicanal con IA Cognitiva.
- **Hardware**: AMD Ryzen 5 5600G, NVIDIA RTX 3060 (12GB), 16GB RAM.
- **Tecnologías**: Traefik (proxy), n8n (workflows), MinIO (S3), PostgreSQL 16 + pgvector, Redis Streams, BullMQ, Ollama (Qwen 2.5 Coder).
- **Componentes**: ERP Core (Express/TypeScript), Event Service (idiempotencia), AI Agent Runtime, Local AI Engine.
- **Observabilidad**: Prometheus, Grafana, Loki.

## Etiquetas
#arquitectura #microservicios #homeLab #erp #ia

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\proyectosInconclusos\sistema-erp-modular (7)\PRODUCTION_ARCHITECTURE.md`
