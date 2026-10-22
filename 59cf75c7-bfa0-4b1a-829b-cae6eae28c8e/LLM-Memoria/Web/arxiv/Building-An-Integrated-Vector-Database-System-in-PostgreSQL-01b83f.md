---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2608.15994v1"
tema: "PostgreSQL Indexes"
tags: [web]
---
# Building An Integrated Vector Database System in PostgreSQL

## Resumen
Este documento presenta PostgreSQL-V 2.0, un sistema de base de datos vectorial integrado que resuelve las limitaciones de la versión anterior (1.0) al soportar concurrencia, recuperación rápida tras fallos y replicación física. Estas mejoras permiten una búsqueda vectorial dentro de PostgreSQL con un rendimiento cercano a las librerías nativas sin sacrificar compatibilidad SQL.

## Datos clave
- **Concurrencia**: Soporte para múltiples conexiones simultáneas; logró hasta 36.4x más throughput que la versión 1.0 al atender 32 clientes concurrentes.
- **Recuperación de fallos**: El tiempo de recuperación se mantiene cercano a los 20 ms, independientemente del tamaño total del índice (a diferencia de la versión 1.0 donde crecía a escala de segundos).
- **Replicación física**: Extiende la replicación al índice desacoplado, preservando la consistencia en nodos standby sin sobrecargar el nodo primario.
- **Limitaciones de v1.0 superadas**: Concurrencia (antes solo una conexión), crecimiento del tiempo de recuperación y falta de soporte para replicación física.

## Etiquetas
#PostgreSQL #VectorDatabase #BigData #SQL #Indexing

Fuente: http://arxiv.org/abs/2608.15994v1
