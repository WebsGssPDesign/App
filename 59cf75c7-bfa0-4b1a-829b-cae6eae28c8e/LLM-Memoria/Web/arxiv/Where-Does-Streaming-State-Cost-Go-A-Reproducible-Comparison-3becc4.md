---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2609.28779v1"
tema: "Kafka Schema Registry"
tags: [web]
---
# Where Does Streaming State Cost Go? A Reproducible Comparison of Flink and Kafka Streams on Kafka

## Resumen
Este estudio compara de forma reproducible a Apache Flink y Kafka Streams en pipelines de Kafka con consistencia exactamente una vez, analizando cómo sus distintas arquitecturas de gestión de estado afectan el rendimiento y la recuperación ante fallos. Aunque ambos motores garantizan la exactitud del procesamiento, muestran diferencias significativas en latencia y robustez dependiendo de si las cargas de trabajo son stateless o windowed.

## Datos clave
- **Arquitectura Flink**: Gestiona estado mediante checkpoints en almacenamiento externo.
- **Arquitectura Kafka Streams**: Recupera estado local releyendo changelogs del broker.
- **Latencia (workloads)**: 4-6 ms para stateless; 4.3-6.2 segundos para windowed.
- **Mediana p99**: 1.97s (stateless) vs 5.68-9.92s (windowed).
- **Sensibilidad a configuración**: Aumentar el intervalo de durabilidad de 1,000 ms a 10,000 ms alteró drásticamente la distribución de latencia en ambos sistemas.
- **Recuperación ante fallos**: Flink completó con éxito 5/5 pruebas de fallo (matar JVM o pérdida de volumen local), mientras que Kafka Streams falló en todas las pruebas de muerte de JVM (0/5) y solo logró 1/5 en pérdidas de volumen local.
- **Conclusión**: La corrección exactamente una vez es necesaria pero insuficiente; se requiere medir holísticamente latencia, completitud y comportamiento de recuperación.

## Etiquetas
#ApacheFlink #KafkaStreams #StreamingState #LatencyAnalysis #FaultTolerance

Fuente: http://arxiv.org/abs/2609.28779v1
