---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/mikekenneth/duckdb_streamlit_arrow_flight"
tema: "Apache Arrow Flight RPC"
tags: [web]
---
# mikekenneth/duckdb_streamlit_arrow_flight

## Resumen
Este proyecto permite ejecutar consultas SQL en una instancia remota de DuckDB a través de Apache Arrow Flight RPC. Los resultados se pueden explorar y descargar directamente mediante una interfaz web creada con Streamlit, facilitando el análisis de datos sin necesidad de instalar dependencias locales complejas.

## Datos clave
- **Requisitos**: `pip install -r requirements.txt`.
- **Configuración (.env)**: Variables para host (`SERVER_FLIGHT_HOST`), puerto (`8815`), tipo de almacenamiento (actualmente solo `local`) y ruta del archivo DuckDB (`data/duck.db`).
- **Comandos de inicio**: `python apps/server/server.py` para el servidor Flight y `streamlit run apps/client/web.py` para la interfaz cliente.
- **Interfaz web**: Accesible en `http://localhost:8501`.
- **Funcionalidad actual**: Ejecución remota de consultas; el almacenamiento S3 y MinIO están marcados como no implementados.

## Etiquetas
#DuckDB #ApacheArrowFlight #Streamlit #SQL #DataEngineering

Fuente: https://github.com/mikekenneth/duckdb_streamlit_arrow_flight
