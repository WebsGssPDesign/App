---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2610.04881v1"
tema: "Temporal Batch Activity Patterns"
tags: [web]
---
# Energy-performance tradeoffs in server farms with batch services and setup times

## Resumen
El artículo propone un modelo de colas con políticas de agrupamiento (batching) para centros de datos que busca equilibrar el ahorro energético al apagar servidores inactivos con la mantención del rendimiento del sistema. Se analiza específicamente un sistema M/M/c/SET--BATCH, considerando variantes donde los servidores esperan antes de apagarse o donde el tamaño del lote es dinámico. Los resultados demuestran que esta estrategia mejora el desempeño, especialmente cuando se permite tiempo de inactividad previo al apagado y cuando la variabilidad en los tiempos de configuración es alta.

## Datos clave
- Modelo analizado: M/M/c/SET--BATCH (cola multi-servidor con servicio por lotes fijos y tiempos de configuración).
- Estrategia principal: Procesamiento simultáneo de un conjunto de trabajos para minimizar consumo mientras se mantiene rendimiento aceptable.
- Hallazgo crítico: El modelo rinde mejor cuando el tiempo de configuración tiene un mayor coeficiente de variación.
- Variantes estudiadas: Sistemas con retraso en el apagado de servidores inactivos y lotes de tamaño dinámico.
- Metodología: Análisis analítico de probabilidades en estado estable complementado con simulaciones para comparar distribuciones de tiempos de configuración.

## Etiquetas
#centros_de_datos #optimizacion_energetica #colas_y_simulacion #batch_processing #gestion_servidores

Fuente: http://arxiv.org/abs/2610.04881v1
