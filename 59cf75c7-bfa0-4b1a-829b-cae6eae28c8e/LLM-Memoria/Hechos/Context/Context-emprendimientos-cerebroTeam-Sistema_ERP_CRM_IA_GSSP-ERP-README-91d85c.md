---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/cerebroTeam/Sistema_ERP_CRM_IA_GSSP/ERP/README.md"
tags: [hecho]
---
# README.md

## Resumen
Este documento describe el despliegue y operación de un asistente IA local basado en RAG (Retrieval-Augmented Generation) diseñado para el mercado minorista GSSP. El sistema combina fuentes de datos curadas con descubrimiento autónomo vía búsqueda web, utilizando modelos de lenguaje abiertos ejecutados completamente offline para garantizar privacidad y seguridad.

## Datos clave
- **Modelo**: Qwen2.5-7B-Instruct (formato GGUF Q4_K_M) ejecutado en LM Studio (puerto 1234).
- **Motor de búsqueda**: SearXNG desplegado vía Docker para descubrimiento autónomo.
- **Base de datos vectorial**: ChromaDB con separación entre fuentes "curated" y "discovered".
- **Flujo de trabajo**: `research_job.py` (fuentes fijas) + `discovery_job.py` (búsqueda por temas).
- **Automatización**: `scheduler.py` o tareas programadas en Windows para ejecución periódica.
- **Seguridad**: Filtros de inyección (`injection_guard.py`) y bloqueo de menciones a proveedores (`guardrail_filter.py`).
- **API**: Servidor expuesto en puerto 8000 accesible vía Tailscale/ZeroTier.

## Etiquetas
#RAG #IALocal #GSSP #OpenSource #Python

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\cerebroTeam\Sistema_ERP_CRM_IA_GSSP\ERP\README.md`
