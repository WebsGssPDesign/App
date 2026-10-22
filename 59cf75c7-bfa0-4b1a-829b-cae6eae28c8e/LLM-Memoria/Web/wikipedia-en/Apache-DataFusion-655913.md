---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Apache_DataFusion"
tema: "PostgreSQL Query Pushdown"
tags: [web]
---
# Apache DataFusion

## Resumen
Apache DataFusion es un motor de consultas analíticas abierto y extensible escrito en Rust que se basa en el formato de memoria columnar Apache Arrow. Diseñado para ser integrado como librería dentro de aplicaciones, ofrece interfaces SQL y DataFrame junto con un optimizador basado en reglas y ejecución multihilo. Desde su origen en 2017 hasta convertirse en proyecto principal de la Fundación Apache en 2024, ha sido adoptado por diversos productos analíticos.

## Datos clave
- **Tecnología**: Escrito en Rust, usa formato columnar Apache Arrow para evitar sobrecarga de serialización.
- **Interfaces**: Proporciona acceso vía SQL y API DataFrame para construcción programática de consultas.
- **Ejecución**: Motor vectorizado multihilo que procesa datos en lotes por columnas, no fila a fila.
- **Formatos nativos**: Lee Apache Parquet, CSV, JSON, Avro e IPC Arrow sin conversión previa.
- **Adopción**: Utilizado por Cloudflare (Log Explorer), Palantir Lightweight Pipelines y InfluxDB 3.0.
- **Historial**: Creado en 2017, donado a Apache Arrow en 2019, proyecto de nivel superior desde abril de 2024.

## Etiquetas
#ApacheDataFusion #Rust #MotorDeConsultas #ApacheArrow #BigData

Fuente: https://en.wikipedia.org/wiki/Apache_DataFusion
