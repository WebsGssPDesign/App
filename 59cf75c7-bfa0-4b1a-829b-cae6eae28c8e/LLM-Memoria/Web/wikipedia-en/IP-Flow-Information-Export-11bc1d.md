---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/IP_Flow_Information_Export"
tema: "OpenTelemetry Exporters"
tags: [web]
---
# IP Flow Information Export

## Resumen
El Protocolo de Exportación de Información de Flujo de IP (IPFIX) es un estándar abierto del IETF diseñado para exportar datos de tráfico de red desde dispositivos como routers hacia sistemas centralizados. Surge como alternativa universal a tecnologías propietarias previas, permitiendo la medición, facturación y gestión de redes mediante la definición estricta del formato de los flujos de información.

## Datos clave
- **RFCs principales**: 3917 (requisitos iniciales), 7011–7015 (especificaciones básicas).
- **Base tecnológica**: Cisco NetFlow Versión 9.
- **Componentes**: *Exporter* (envía datos) y *Collector* (recibe datos); ambos pueden tener relaciones muchos-a-muchos.
- **Mecanismo de datos**: Uso de *Templates* para definir la estructura de los mensajes antes de enviar el conjunto de datos real.
- **Capa de transporte**: Prefiere SCTP, pero soporta TCP y UDP.
- **Concepto de flujo**: Conjunto de paquetes en un intervalo temporal con propiedades comunes (misma fuente, destino y protocolo).

## Etiquetas
#IPFIX #Redes #NetFlow #IETF #GestiónDeRedes

Fuente: https://en.wikipedia.org/wiki/IP_Flow_Information_Export
