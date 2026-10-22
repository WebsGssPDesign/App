---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/ravichandra-eluri/otel-k8s-controller"
tema: "OpenTelemetry Sampling Strategies"
tags: [web]
---
# ravichandra-eluri/otel-k8s-controller

## Resumen
Este proyecto es un operador nativo de Kubernetes diseñado para gestionar despliegues del OpenTelemetry Collector mediante una CRD personalizada. Su objetivo principal es facilitar la configuración de pipelines de observabilidad en entornos cloud-native, incluyendo redes de borde con conectividad intermitente. Ofrece características avanzadas como estrategias de muestreo y mecanismos de almacenamiento y reenvío (store-and-forward) para garantizar la integridad de los datos de telemetría incluso cuando el backend está inaccesible.

## Datos clave
- **Tecnologías**: Construido con `controller-runtime` y Operator SDK.
- **Protocolos**: Soporta gRPC (puerto 4317) y HTTP (puerto 4318).
- **Estrategias de muestreo**: Head-based, tail-based (con políticas de latencia/error), siempre-on o siempre-off.
- **Store-and-Forward (SAF)**: Buffera spans en disco (`file_storage`) si el exportador no está disponible y los reenvía al reconectarse; crítico para entornos GDC Edge.
- **Recurso CRD**: `OTelCollector` (apiVersion: `otel.chandradevgo.io/v1alpha1`).
- **Campos importantes de la CRD**: `spec.replicas`, `spec.exporterEndpoint`, `spec.sampling.strategy`, `spec.storeAndForward.enabled`.
- **Estado expuesto**: `phase`, `readyReplicas`, `exporterReachable`, `bufferedSpanCount`.

## Etiquetas
#OpenTelemetry #KubernetesOperator #Observabilidad #Store-and-Forward #GDCEdge

Fuente: https://github.com/ravichandra-eluri/otel-k8s-controller
