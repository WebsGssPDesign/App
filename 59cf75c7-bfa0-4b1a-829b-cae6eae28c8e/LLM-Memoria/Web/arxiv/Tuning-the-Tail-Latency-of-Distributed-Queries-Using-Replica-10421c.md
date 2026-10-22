---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2212.10387v1"
tema: "Dapr State Replication"
tags: [web]
---
# Tuning the Tail Latency of Distributed Queries Using Replication

## Resumen
Este artículo aborda la latencia en consultas de grafos distribuidas, donde los saltos entre servidores son un cuello de botella. Propone un modelo de trabajo y heurísticas para replicar datos remotamente, eliminando estos saltos mientras se minimiza el costo de almacenamiento. La evaluación demuestra que este enfoque permite ajustar finamente la latencia encontrando puntos óptimos en el diseño del sistema.

## Datos clave
- **Problema**: Latencia alta en consultas distribuidas debido a los saltos (hops) entre servidores.
- **Solución**: Replicación selectiva de datos remotos para evitar trayectos inter-servidor.
- **Contribuciones principales**: Modelo de trabajo para causalidad de acceso, familia de heurísticas y condiciones suficientes de corrección.
- **Resultado**: Capacidad de afinar la latencia de cola (tail latency) y encontrar equilibrios óptimos entre rendimiento y costo de replicación.

## Etiquetas
#grafos #latencia #replicacion #basesdedatosdistribuidas #optimizacion

Fuente: http://arxiv.org/abs/2212.10387v1
