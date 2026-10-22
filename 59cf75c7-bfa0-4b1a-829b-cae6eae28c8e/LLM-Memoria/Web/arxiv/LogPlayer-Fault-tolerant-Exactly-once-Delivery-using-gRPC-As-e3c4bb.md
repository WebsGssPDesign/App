---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/1911.11286v1"
tema: "gRPC Bidirectional Streaming"
tags: [web]
---
# LogPlayer: Fault-tolerant Exactly-once Delivery using gRPC Asynchronous Streaming

## Resumen
LogPlayer es un componente diseñado para entregar mutaciones transaccionales de un registro (WAL) a shards de almacenamiento trasero con tolerancia a fallos y garantía de entrega exactamente una vez. El sistema utiliza gRPC para streaming asíncrono y ha sido verificado formalmente mediante TLA+ para asegurar la entrega ordenada incluso ante fallos. Las pruebas experimentales demuestran latencias inferiores al milisegundo, superando significativamente en eficiencia a Apache Kafka para este propósito específico.

## Datos clave
- **Componente**: LogPlayer (entrega de WAL).
- **Protocolo**: gRPC streaming asíncrono.
- **Verificación**: TLA+ (garantiza entrega ordenada y exactamente una vez).
- **Rendimiento**: Latencia sub-milisegundo.
- **Comparativa**: Más eficiente que Apache Kafka para sistemas WAL con garantía de exactitud.

## Etiquetas
#LogPlayer #gRPC #WAL #DistribuciónDeDatos #AltaDisponibilidad

Fuente: http://arxiv.org/abs/1911.11286v1
