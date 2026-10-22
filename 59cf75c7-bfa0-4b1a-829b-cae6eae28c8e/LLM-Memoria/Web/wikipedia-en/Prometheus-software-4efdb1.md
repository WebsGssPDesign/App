---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Prometheus_%28software%29"
tema: "Prometheus Remote Write"
tags: [web]
---
# Prometheus (software)

## Resumen
Prometheus es una aplicación de software libre para monitoreo y alertas basada en Go, diseñada para recopilar métricas en tiempo real mediante un modelo de extracción HTTP. Desarrollado originalmente en SoundCloud y adoptado por la CNCF, utiliza un lenguaje propio (PromQL) y se suele emparejar con Grafana para visualización.

## Datos clave
- **Origen:** Desarrollado en SoundCloud en 2012; aceptado por la CNCF en 2016.
- **Modelo de datos:** Métricas organizadas como pares clave-valor (labels) para alta dimensionalidad.
- **Mecanismo de recolección:** Modelo "pull" donde el servidor consulta periódicamente a los exportadores.
- **Lenguaje de consultas:** PromQL, con funciones temporales como `rate()` y tipos de métricas (Counter, Gauge, Histogram, Summary).
- **Componentes principales:** Prometheus Server, Alertmanager (gestión de alertas) y Grafana (dashboards).
- **Almacenamiento:** Base de datos de series temporales local combinando memoria y archivos persistentes con índice invertido.
- **Interoperabilidad:** Soporta protocolos como Graphite, StatsD, SNMP y JMX; formato estandarizado OpenMetrics.

## Etiquetas
#Prometheus #Monitoreo #DevOps #Infraestructura #CNCF

Fuente: https://en.wikipedia.org/wiki/Prometheus_%28software%29
