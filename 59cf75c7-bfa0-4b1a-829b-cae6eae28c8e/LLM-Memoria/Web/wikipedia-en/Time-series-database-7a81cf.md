---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Time_series_database"
tema: "Temporal Workflow Aggregations"
tags: [web]
---
# Time series database

## Resumen
Una base de datos de series temporales (TSDB) es un sistema especializado diseñado para manejar eficientemente secuencias de datos indexados cronológicamente. A diferencia de las bases de datos relacionales, estas optimizan el almacenamiento mediante compresión avanzada y automatizan la gestión del ciclo de vida de los datos, eliminando particiones históricas antiguas. Están ideales para cargas de trabajo "append-only" que requieren alta velocidad de escritura y consultas rápidas en ventanas temporales específicas.

## Datos clave
*   **Conceptos:** Series temporales (datos secuenciales por tiempo), compresión especializada (codificación delta, Gorilla), carga de trabajo "append-only".
*   **Aplicaciones:** Monitoreo industrial, IoT, redes ciber-físicas, datos financieros (ticks) y gestión de redes eléctricas.
*   **Características técnicas:** Alta tasa de ingestión, baja latencia en consultas de rango, agregaciones temporales multidimensionales usando metadatos tipo clave-valor.
*   **Diferencias vs SQL:** No requieren restricciones relacionales complejas; eliminan datos históricos en lugar de retenerlos indefinidamente.

## Etiquetas
#basesdedatos #series temporales #IoT #monitoreo #optimización

Fuente: https://en.wikipedia.org/wiki/Time_series_database
