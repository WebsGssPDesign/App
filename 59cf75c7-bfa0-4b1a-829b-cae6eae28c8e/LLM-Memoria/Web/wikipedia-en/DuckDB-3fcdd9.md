---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/DuckDB"
tema: "Kafka Schema Registry"
tags: [web]
---
# DuckDB

## Resumen
DuckDB es una base de datos relacional de columnas de código abierto diseñada específicamente para cargas de trabajo analíticas (OLAP) en lugar de transaccionales (OLTP). A diferencia de sistemas tradicionales, opera dentro del proceso anfitrión sin dependencias externas y utiliza un motor de procesamiento vectorizado para lograr alta velocidad.

## Datos clave
- **Arquitectura**: Motor de consulta vectorizado; ejecución in-proceso (sin cliente-servidor tradicional).
- **Requisitos**: Compilable únicamente con C++17; cero dependencias externas.
- **Formato de almacenamiento**: Archivo único que soporta escaneos eficientes, actualizaciones masivas y eliminaciones.
- **Compatibilidad**: Soporte para WebAssembly (ejecución en navegador) y múltiples lenguajes (Python, R, etc.).
- **Extensiones principales**: httpfs (acceso remoto), spatial (geoespacial), iceberg, delta, ducklake.
- **Adopción corporativa**: Utilizado por Facebook, Google y Airbnb; adquirido por Amazon AWS en agosto de 2026.
- **Licencia**: MIT, garantizada para siempre por la DuckDB Foundation sin fines de lucro.

## Etiquetas
#DuckDB #BaseDeDatos #OLAP #OpenSource #BigData

Fuente: https://en.wikipedia.org/wiki/DuckDB
