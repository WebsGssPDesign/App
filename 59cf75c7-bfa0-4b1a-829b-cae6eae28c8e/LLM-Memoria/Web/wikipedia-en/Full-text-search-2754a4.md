---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Full-text_search"
tema: "PostgreSQL Full-Text Search"
tags: [web]
---
# Full-text search

## Resumen
La búsqueda de texto completo es una técnica que examina el contenido literal de documentos para encontrar coincidencias con consultas de usuario, diferenciándose de las búsquedas basadas en metadatos. Para manejar grandes volúmenes de datos, los motores dividen el proceso en dos fases: la creación de un índice (concordancia) y la ejecución de la búsqueda contra ese índice.

## Datos clave
- **Serial scanning**: Estrategia para pocos documentos que escanea cada archivo directamente con cada consulta (ej. `grep`).
- **Indexing vs. Searching**: Fase de construcción del índice seguido de consultas rápidas sobre el mismo.
- **Stop words**: Palabras comunes omitidas durante el indexado por aportar poco valor (ej. "the", "and").
- **Stemming**: Reducción de palabras a su forma base para mejorar la recuperación (ej. "drives" -> "drive").
- **Precisión vs. Recall**: La precisión mide resultados relevantes devueltos; el recall mide relevancia total encontrada. Existe una compensación entre ambos.
- **False positives**: Resultados irrelevantes causados por ambigüedad del lenguaje, mitigables con clustering (ej. algoritmos bayesianos).
- **Síntomas y problemas**: Fallos al no encontrar términos exactos o sinónimos; solución mediante índices de términos relacionados.
- **Herramientas de consulta**: Búsqueda booleana (`AND`, `NOT`, `OR`), búsqueda restringida por campo y expansión de consultas con palabras clave.

## Etiquetas
#búsqueda_de_texto #indexación #recuperación_de_información #algoritmos_de_búsqueda #precisión_y_recall

Fuente: https://en.wikipedia.org/wiki/Full-text_search
