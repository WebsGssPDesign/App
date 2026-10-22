---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2604.16511v1"
tema: "PostgreSQL Query Rewrite"
tags: [web]
---
# SQL Query Engine: A Self-Healing LLM Pipeline for Natural Language to PostgreSQL Translation

## Resumen
SQL Query Engine es un servicio de código abierto que traduce preguntas en lenguaje natural a consultas validadas de PostgreSQL mediante una pipeline de LLMs de dos etapas. El sistema incluye un bucle autocrítico para corregir errores de ejecución y mecanismos para evitar regresiones, manteniendo conexiones de solo lectura.

## Datos clave
- **Arquitectura**: Pipeline de LLM en dos fases (introspección de esquema y generación SQL, seguido de ejecución y corrección).
- **Parser multiestrategia**: Extrae SQL de JSON, bloques de código o texto crudo sin APIs estructuradas.
- **Autocuración**: Diagnóstico iterativo usando códigos SQLSTATE completos y mensajes de diagnóstico de PostgreSQL ante fallos o resultados vacíos.
- **Prevención de regresiones**: "Early-accept" para consultas exitosas inmediatas y seguimiento del "best-result" en reintentos.
- **Infraestructura**: Contexto de esquema en caché por sesión (Redis), eventos de progreso vía Pub/Sub/SSE, endpoint compatible con OpenAI.
- **Resultados**: +9.3pp de precisión con Llama 4 Scout 17B; 49.0% de precisión en el benchmark BIRD con GPT-OSS-120B.

## Etiquetas
#SQL #PostgreSQL #LLM #Autocorrección #OpenSource

Fuente: http://arxiv.org/abs/2604.16511v1
