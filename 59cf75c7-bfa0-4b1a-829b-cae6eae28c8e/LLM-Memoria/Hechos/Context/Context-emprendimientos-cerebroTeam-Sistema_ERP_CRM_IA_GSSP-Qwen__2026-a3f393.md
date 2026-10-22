---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/cerebroTeam/Sistema_ERP_CRM_IA_GSSP/Qwen__20260616_m34ri76la.txt"
tags: [hecho]
---
# Qwen__20260616_m34ri76la.txt

## Resumen
Este documento describe la arquitectura de un sistema híbrido para una IA que integra conocimiento local, general y en tiempo real. Su función es responder preguntas consultando primero documentos internos específicos y, si no encuentra la respuesta, recurriendo a su entrenamiento base o buscando información actualizada en internet.

## Datos clave
- **Proyecto**: Sistema ERP CRM IA GSSP (cerebroTeam).
- **Tecnologías**: ChromaDB para almacenamiento local, Llama 3.2 como modelo de lenguaje, DuckDuckGo para búsqueda web.
- **Capas lógicas**: 
    1. Base de conocimiento local (644 documentos) con alta confianza.
    2. Conocimiento general del modelo de entrenamiento.
    3. Búsqueda web en tiempo real para información actualizada.
- **Flujo de decisión**: Evaluar relevancia en local → Si no, usar conocimiento general → Si requiere actualización, buscar en web.

## Etiquetas
#arquitectura_IA #RAG #LLM #búsqueda_web

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\cerebroTeam\Sistema_ERP_CRM_IA_GSSP\Qwen__20260616_m34ri76la.txt`
