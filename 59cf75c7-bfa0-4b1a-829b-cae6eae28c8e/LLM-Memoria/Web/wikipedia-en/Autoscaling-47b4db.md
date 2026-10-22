---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Autoscaling"
tema: "Kubernetes Cluster Autoscaler"
tags: [web]
---
# Autoscaling

## Resumen
El autoscaling es una técnica de computación en la nube que ajusta automáticamente el número de servidores activos basándose en la carga actual del sistema. Este método optimiza costos al reducir recursos durante periodos de baja demanda y garantiza disponibilidad ante picos repentinos de tráfico, evitando tanto el desperdicio como las interrupciones por falta de capacidad.

## Datos clave
- **Definición**: Ajuste dinámico de recursos computacionales (número de servidores) según la carga.
- **Ventajas principales**: Reducción de costos eléctricos y de licencias en la nube; mayor disponibilidad (uptime); reemplazo automático de instancias no saludables o fallidas por hardware/red.
- **Comparativa vs. escalado estático**: El autoscaling responde a patrones reales de uso, mientras que el escalado fijo puede causar caídas si hay tráfico inesperado en horarios con baja actividad programada.
- **Implementaciones mencionadas**: Lanzamiento inicial de EC2 por AWS (2006); integración nativa de autoscaling en AWS desde mayo de 2009; soporte añadido por Microsoft Azure (junio 2013) y Google Cloud Platform (noviembre 2014).
- **Caso de uso destacado**: Netflix utiliza escalado agresivo hacia arriba y cauteloso hacia abajo para mantener disponibilidad ante demandas variables.

## Etiquetas
#autoscaling #cloudcomputing #aws #costoptimization #highavailability

Fuente: https://en.wikipedia.org/wiki/Autoscaling
