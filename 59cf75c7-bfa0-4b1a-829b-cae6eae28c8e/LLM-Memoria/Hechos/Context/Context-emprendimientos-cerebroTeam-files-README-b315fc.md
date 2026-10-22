---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/cerebroTeam/files/README.md"
tags: [hecho]
---
# README.md

## Resumen
Este documento describe la implementación de un asistente IA local basado en RAG (Retrieval-Augmented Generation) para el negocio GSSP Mini Market. El sistema utiliza Qwen2.5-7B-Instruct y ChromaDB para investigar fuentes web definidas por el usuario, responder preguntas con contexto actualizado y operar completamente offline sin costos de nube.

## Datos clave
- **Modelo**: Qwen2.5-7B-Instruct (formato GGUF Q4_K_M) ejecutado en LM Studio (puerto 1234).
- **Base de datos vectorial**: ChromaDB para almacenamiento y consulta con deduplicación.
- **Flujo de trabajo**: `research_job.py` descarga y vectoriza fuentes; `rag_chat.py` gestiona consultas; `scheduler.py` automatiza el ciclo.
- **API**: Servidor expuesto en puerto 8000 vía `uvicorn`, accesible localmente o mediante Tailscale/ZeroTier.
- **Configuración crítica**: Verificar dominio en `config.py` y gestionar fuentes en `source_registry.py`.
- **Seguridad**: `guardrail_filter.py` bloquea menciones al proveedor antes de responder a clientes.

## Etiquetas
#RAG #IALocal #GSSP #ChromaDB #OpenSource

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\cerebroTeam\files\README.md`
