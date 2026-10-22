---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://es.wikipedia.org/wiki/Autoescalado"
tema: "Kubernetes Vertical Pod Autoscaler"
tags: [web]
---
# Autoescalado

## Resumen
El autoescalado es una técnica de computación en la nube que ajusta automáticamente el número de servidores activos según la demanda actual, optimizando recursos frente a picos de tráfico impredecibles. A diferencia del escalado fijo basado en estimaciones horarias, este método reacciona en tiempo real para evitar saturación o inactividad innecesaria.

## Datos clave
- **Mecanismo**: Aumenta o disminuye servidores según la carga total activa.
- **Ventajas principales**: Ahorro de costos (facturación por uso), eficiencia energética y protección contra fallos de hardware mediante reemplazo automático.
- **Plataformas implementadas**: AWS (EC2, ECS desde 2016), Microsoft Azure (desde 2013), Google Cloud Platform (desde 2014).
- **Casos de uso destacados**: Facebook redujo un 27% su consumo energético en horas valle; Netflix lo usa para manejar alta variabilidad.
- **Métricas comunes**: Utilización de CPU y memoria; Kubernetes escala pods basándose en estas métricas.

## Etiquetas
#autoescalado #cloudcomputing #aws #azure #kubernetes #optimizacion

Fuente: https://es.wikipedia.org/wiki/Autoescalado
