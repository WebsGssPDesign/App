---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://es.wikipedia.org/wiki/Arquitectura_dirigida_por_eventos"
tema: "Temporal Event Sourcing"
tags: [web]
---
# Arquitectura dirigida por eventos

## Resumen
La arquitectura dirigida por eventos (EDA) es un paradigma de software basado en la producción y detección de eventos, definidos como cambios significativos de estado. Este enfoque conecta componentes débilmente acoplados mediante emisores, consumidores y canales, permitiendo una alta escalabilidad, tolerancia a fallos y resiliencia en sistemas distribuidos complejos.

## Datos clave
- **Definición**: Evento = cambio significativo de estado; Notificación del evento = mensaje asíncrono que informa sobre el cambio.
- **Componentes principales**: Emisores (detectan y transfieren), Consumidores (reaccionan al evento) y Canales (conductos de transmisión).
- **Ventajas**: Escalabilidad horizontal, alta disponibilidad (copias del estado), resiliencia frente a fallos, desacoplamiento total entre productores y consumidores.
- **Estructura del evento**: Compuesto por encabezado (tipo, nombre, marca de tiempo) y cuerpo o carga útil (descripción del cambio).
- **Relación con SOA**: Complementa la arquitectura orientada a servicios mediante activadores basados en eventos entrantes.

## Etiquetas
#ArquitecturaDeSoftware #EDA #Eventos #Escalabilidad #DesarrolloDistribuido

Fuente: https://es.wikipedia.org/wiki/Arquitectura_dirigida_por_eventos
