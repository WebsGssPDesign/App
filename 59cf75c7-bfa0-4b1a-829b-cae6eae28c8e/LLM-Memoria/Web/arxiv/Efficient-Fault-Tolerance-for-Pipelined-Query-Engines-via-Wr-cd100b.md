---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2403.08062v1"
tema: "PostgreSQL Write-Ahead Logging"
tags: [web]
---
# Efficient Fault Tolerance for Pipelined Query Engines via Write-ahead Lineage

## Resumen
El artículo presenta "write-ahead lineage", una técnica de recuperación ante fallos para motores de consultas en pipeline que combina la reejecución basada en linaje de Apache Spark con registros de escritura anticipada (write-ahead logging). A diferencia de los enfoques tradicionales, esta metodología registra el linaje dinámicamente durante la ejecución y solo almacena datos de tamaño kilobyte, evitando el alto costo de persistir salidas intermedias.

## Datos clave
- **Write-ahead lineage**: Técnica que combina reejecución basada en linaje con logging de escritura anticipada para recuperación eficiente.
- **Quokka**: Motor de consultas distribuidos y en pipeline donde se implementó la técnica propuesta.
- **Eficiencia**: Persiste solo KB-sized lineages frente a MB-sized intermediate outputs, minimizando el sobrecarga normal.
- **Recuperación rápida**: Las tareas consumen salidas intermedias con linaje persistente, evitando rollbacks globales y permitiendo recuperación paralela de tareas perdidas en diferentes etapas.
- **Rendimiento**: Quokka es aproximadamente 2 veces más rápido que SparkSQL en el benchmark TPC-H con un rendimiento similar en recuperación de fallos.

## Etiquetas
#fault_tolerance #query_engines #write_ahead_log #distributed_systems #spark #quokka

Fuente: http://arxiv.org/abs/2403.08062v1
