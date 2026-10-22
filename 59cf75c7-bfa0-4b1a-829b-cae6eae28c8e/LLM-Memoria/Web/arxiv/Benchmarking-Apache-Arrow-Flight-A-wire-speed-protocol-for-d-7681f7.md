---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2204.03032v2"
tema: "Apache Arrow Flight RPC"
tags: [web]
---
# Benchmarking Apache Arrow Flight -- A wire-speed protocol for data transfer, querying and microservices

## Resumen
El protocolo Apache Arrow Flight, construido sobre gRPC, optimiza la transferencia de datos estructurados entre sistemas reduciendo drásticamente el tiempo de serialización. Este documento presenta resultados de pruebas de rendimiento que demuestran su alta velocidad y escalabilidad en entornos de big data y microservicios.

## Datos clave
- **Velocidad máxima:** Hasta 6000 MB/s para operaciones DoGet() y 4800 MB/s para DoPut().
- **Uso de ancho de banda:** Puede aprovechar hasta el 95% del ancho de banda en nodos con interconexión Mellanox ConnectX-3 o Connect-IB.
- **Escalabilidad:** Utiliza eficientemente hasta la mitad de los núcleos del sistema para comunicación bidireccional.
- **Comparativa de rendimiento:** En sistemas como Dremio, es 20 veces más rápido que turbodbc y 30 veces más rápido que ODBC.

## Etiquetas
#ApacheArrow #DataTransfer #BigData #PerformanceBenchmarking #gRPC

Fuente: http://arxiv.org/abs/2204.03032v2
