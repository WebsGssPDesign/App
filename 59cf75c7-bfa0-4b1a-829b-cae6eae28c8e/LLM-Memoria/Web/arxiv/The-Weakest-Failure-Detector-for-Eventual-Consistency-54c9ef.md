---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/1505.03469v1"
tema: "Dapr State Replication Eventual Consistency"
tags: [web]
---
# The Weakest Failure Detector for Eventual Consistency

## Resumen
Este artículo demuestra que el detecto de fallos Ω es tanto necesario como suficiente para implementar servicios replicados eventualmente consistentes en entornos de paso de mensajes, eliminando la necesidad del detecto Σ requerido para la consistencia fuerte. El trabajo establece por primera vez la diferencia computacional exacta entre garantizar consistencia inmediata y eventual bajo cualquier suposición sobre fallos.

## Datos clave
- Ω: Detecto de fallos necesario y suficiente para consistencia eventual en entornos de paso de mensajes con mayoría de procesos correctos.
- Σ: Detecto de fallos (quorum) adicional requerido exclusivamente para garantizar consistencia fuerte.
- Diferencia computacional: Implementar máquinas de estado replicadas consistentes requiere Ω + Σ, mientras que las eventualmente consistentes solo requieren Ω.

## Etiquetas
#consistencia_eventual #fallos_distribuidos #replicación #Ω_detector

Fuente: http://arxiv.org/abs/1505.03469v1
