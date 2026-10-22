---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/system-highload-architect/pcef-shaper-system"
tema: "gRPC Protobuf Compression"
tags: [web]
---
# system-highload-architect/pcef-shaper-system

## Resumen
Este proyecto presenta un motor de usuario para la función PCEF (Policy & Charging Enforcement Function) escrito en Go, diseñado para entornos de alta carga en telecomunicaciones. Integra un clasificador DPI y un sistema de control de calidad de servicio (QoS) que opera bajo los estándares 3GPP PCC. La arquitectura garantiza un rendimiento óptimo mediante mecanismos libres de bloqueos y una gestión eficiente de memoria.

## Datos clave
- **Lenguaje**: Go 1.26.4 con soporte para Kubernetes.
- **Algoritmos**: Limitador de tasa CAS (Lock-Free) al 100%, algoritmo "Leaky Bucket" para control de flujo.
- **Estrategias de memoria**: Cache LRU reactiva con expulsión inercial y compresión en cascada desde abajo hacia arriba.
- **Categorización de tráfico**: Clasificación en tiempo real de paquetes en tres categorías: `SOCIAL`, `STREAMING` e `GAMING`.
- **Interfaz Gy**: Control de crédito en memoria que bloquea o limita el tráfico si se agota el cupo de datos o el saldo.
- **Arquitectura**: Diseño aislado del plano de usuario (User Plane) con sharding de mapas de 32 vías.

## Etiquetas
#PCEF #Telecom #GoLang #DPI #QoS #HighLoad

Fuente: https://github.com/system-highload-architect/pcef-shaper-system
