---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/cerebroTeam/files2/README.md"
tags: [hecho]
---
# README.md

## Resumen
Este documento describe la implementación de un asistente IA local basado en RAG (Retrieval-Augmented Generation) para el negocio GSSP Mini Market. El sistema combina fuentes de conocimiento curadas con descubrimiento automático de contenido vía búsqueda, utilizando modelos open source y ejecutándose completamente offline.

## Datos clave
- **Modelo LLM**: Qwen2.5-7B-Instruct (formato GGUF Q4_K_M) ejecutado localmente en LM Studio (puerto 1234).
- **Motor de búsqueda propio**: SearXNG desplegado con Docker para el descubrimiento autónomo de temas.
- **Base de datos vectorial**: ChromaDB para almacenar y consultar fragmentos de texto, separando fuentes "curated" de las "discovered".
- **Flujo de trabajo**: `research_job.py` procesa URLs fijas; `discovery_job.py` explora internet por temas definidos en `discovery_topics.py`.
- **Seguridad**: Incluye filtros (`guardrail_filter.py`, `injection_guard.py`) para evitar menciones a proveedores y bloquear inyecciones de instrucciones antes de responder al cliente.
- **Automatización**: El script `scheduler.py` orquesta tareas periódicas, o se pueden configurar tareas programadas en Windows para mayor robustez.
- **API**: Servidor expuesto en puerto 8000 vía `uvicorn`, accesible localmente (ej. con Tailscale) para integración con WhatsApp o web.

## Etiquetas
#RAG #IALocal #GSSP #Python #OpenSource

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\cerebroTeam\files2\README.md`
