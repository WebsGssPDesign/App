---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/AI_observability"
tema: "OpenTelemetry Semantic Conventions"
tags: [web]
---
# AI observability

## Resumen
La observabilidad de IA es la práctica de recopilar y analizar telemetría (registros, métricas y rastros) para comprender el comportamiento y rendimiento de sistemas basados en modelos de aprendizaje automático, especialmente LLMs. A diferencia del monitoreo tradicional que se basa en umbrales predefinidos, busca proporcionar contexto para entender por qué ocurren anomalías no anticipadas, como respuestas inexactas o inseguras, incluso cuando la infraestructura parece saludable.

## Datos clave
- **Diferencia con el monitoreo**: El monitoreo usa métricas predeterminadas y alertas; la observabilidad permite investigar comportamientos inesperados correlacionando señales diversas.
- **Concepto de deriva (concept drift)**: Cambios en el comportamiento del modelo a lo largo del tiempo que deben rastrearse.
- **Dimensiones específicas**: Entradas/salidas, costo/uso de recursos, rendimiento, calidad de salida (incluyendo alucinaciones), comportamiento temporal y seguridad/política.
- **Técnicas principales**: Rastreo extremo a extremo, registro estructurado, detección de anomalías, monitoreo sintético con prompts de prueba y evaluación automatizada ("LLM-as-a-judge").
- **Sistemas basados en agentes**: Requieren señales adicionales para registrar pasos intermedios de razonamiento, llamadas a herramientas externas y cadenas de generación mejoradas con recuperación.

## Etiquetas
#IA #Observabilidad #MachineLearning #LLMs #MLOps

Fuente: https://en.wikipedia.org/wiki/AI_observability
