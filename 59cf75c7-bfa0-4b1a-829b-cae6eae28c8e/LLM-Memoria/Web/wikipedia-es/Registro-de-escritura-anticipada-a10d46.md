---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://es.wikipedia.org/wiki/Registro_de_escritura_anticipada"
tema: "PostgreSQL Write-Ahead Logging"
tags: [web]
---
# Registro de escritura anticipada

## Resumen
El registro de escritura anticipada (WAL) es una técnica informática que garantiza la atomicidad y durabilidad en bases de datos escribiendo cambios primero en un log antes de aplicarlos al almacenamiento principal. Esta arquitectura permite reconstruir el estado del sistema tras fallos, ya sea por pérdida de energía o errores de software, asegurando la integridad de los datos.

## Datos clave
- **Funciones principales**: Garantiza durabilidad y atomicidad (propiedades ACID), permite recuperación ante fallos y actualizaciones in situ.
- **Mecanismo de funcionamiento**: Las operaciones se registran en un archivo de disco antes de modificar las páginas en memoria o base de datos; incluye información para deshacer y rehacer cambios.
- **Gestión del registro**: Tras cierto número de operaciones, los cambios se aplican a la base de datos y el registro se borra (punto de control).
- **Algoritmos y variantes**: ARIES es un algoritmo popular basado en WAL; los sistemas de archivos modernos usan una variante llamada "llevar un diario" para metadatos.

## Etiquetas
#basesdedatos #WAL #recuperaciondesastres #ACID #ARIES

Fuente: https://es.wikipedia.org/wiki/Registro_de_escritura_anticipada
