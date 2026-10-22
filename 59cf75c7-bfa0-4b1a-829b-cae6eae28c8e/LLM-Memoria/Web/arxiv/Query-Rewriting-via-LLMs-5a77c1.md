---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2502.12918v4"
tema: "PostgreSQL Query Rewrite"
tags: [web]
---
# Query Rewriting via LLMs

## Resumen
El artículo presenta el sistema LITHE, una herramienta que utiliza modelos de lenguaje grandes (LLMs) para reescribir consultas SQL complejas y lentas con el objetivo de mejorar su rendimiento. A diferencia de las reglas tradicionales o los optimizadores nativos, LITHE combina prompts especializados, eliminación de redundancias y guías basadas en probabilidades de tokens para generar equivalentes más eficientes.

## Datos clave
- **Sistema implementado:** LITHE.
- **Métodos principales:** Suite de prompts básicos, prompts sensibles a la base de datos (eliminación de redundancia y reglas de selectividad) y rutas de reescritura guiadas por probabilidad de tokens del LLM.
- **Verificación:** Uso de herramientas lógicas y estadísticas para detectar violaciones semánticas antes de que el DBA considere la consulta.
- **Resultado en TPC-DS (PostgreSQL):** Mejora media geométrica del tiempo de ejecución de 13.2x sobre el optimizador nativo, comparado con solo 4.9x de las técnicas actuales (SOTA).

## Etiquetas
#SQL #Optimización #LLM #BasesDeDatos #Rendimiento

Fuente: http://arxiv.org/abs/2502.12918v4
