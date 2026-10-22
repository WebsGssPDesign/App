---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/sophie-nguyenthuthuy/distributed-query-planner"
tema: "PostgreSQL Query Pushdown"
tags: [web]
---
# sophie-nguyenthuthuy/distributed-query-planner

## Resumen
Este proyecto presenta un optimizador de consultas federadas capaz de reescribir planes de consulta para distribuir filtros nativamente entre motores como MongoDB, Parquet y PostgreSQL. El sistema selecciona la configuración más eficiente mediante un modelo de costos calibrado con muestreo estadístico sobre los datos.

## Datos clave
- **Capacidad principal**: Empuje de predicados (predicate pushdown) a múltiples motores de almacenamiento heterogéneos.
- **Predicados soportados**: Comparisons, IN, BETWEEN, LIKE, IS NULL, AND, OR y NOT (con limitaciones en Parquet para OR/NOT).
- **Modelo de costos**: Se basa en estadísticas de tablas (conteo de filas, histogramas) para estimar CPU, E/S y volumen de datos.
- **Instalación**: Requiere `pip install -e ".[dev]"` e instaladores opcionales específicos (`pyarrow`, `pymongo`, `psycopg2-binary`).
- **API principal**: Uso de `FederatedOptimizer`, `Catalog` y `StatsRegistry` para construir y ejecutar planes.

## Etiquetas
#optimización #consultas_federadas #mongodb #parquet #postgresql

Fuente: https://github.com/sophie-nguyenthuthuy/distributed-query-planner
