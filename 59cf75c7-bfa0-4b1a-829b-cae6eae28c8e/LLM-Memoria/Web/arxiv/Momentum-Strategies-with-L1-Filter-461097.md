---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/1403.4069v1"
tema: "OpenTelemetry Sampling Strategies"
tags: [web]
---
# Momentum Strategies with L1 Filter

## Resumen
Este artículo explora la implementación de filtros L1 para analizar señales financieras ruidosas, descomponiéndolas en tendencias lineales o pasos mediante un problema de mínimos cuadrados restringidos. El método utiliza un parámetro de regularización estimado por validación cruzada para identificar cambios locales y globales dentro de las series temporales. Se aplican estos conceptos a estrategias de momentum, aprovechando la configuración de tendencias para modelar procesos con propiedades de retorno a la media.

## Datos clave
- Filtro L1: Genera señales filtradas compuestas por tendencias rectas o pasos.
- Parámetro de regularización (λ): Determina el número de rupturas en la tendencia y se estima mediante validación cruzada.
- Escalas temporales: Diferenciación entre tendencias a largo plazo (globales) y cortas (locales).
- Modelo financiero: Combina tendencias globales con propiedades de retorno a la media.
- Aplicación principal: Estrategias de momentum basadas en configuraciones de tendencia detectadas por el filtro.

## Etiquetas
#finanzas #series-temporales #momentum #filtro-L1 #análisis-técnico

Fuente: http://arxiv.org/abs/1403.4069v1
