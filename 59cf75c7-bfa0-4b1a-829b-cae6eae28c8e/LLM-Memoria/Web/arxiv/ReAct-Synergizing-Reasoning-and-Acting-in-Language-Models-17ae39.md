---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2210.03629v3"
tema: "React Server Actions"
tags: [web]
---
# ReAct: Synergizing Reasoning and Acting in Language Models

## Resumen
Este artículo presenta ReAct, un enfoque que combina la generación de trazas de razonamiento y acciones específicas para tareas en modelos de lenguaje grandes (LLMs). Al intercalar estos dos procesos, el modelo puede consultar fuentes externas como bases de conocimiento o entornos, mejorando su capacidad para resolver problemas complejos con mayor interpretabilidad y fiabilidad.

## Datos clave
- **Conceptos**: Razonamiento (chain-of-thought) y Actuación (generación de planes de acción).
- **Ventajas**: Reduce la alucinación y la propagación de errores; mejora la interpretabilidad humana.
- **Resultados en benchmarks**:
  - HotpotQA y Fever: Consulta a la API de Wikipedia para verificar hechos.
  - ALFWorld: Superó métodos de imitación/aprendizado por refuerzo con una tasa de éxito absoluta del 34%.
  - WebShop: Superó los métodos basales con una mejora del 10% en tasa de éxito.
- **Requisitos**: Funciona eficazmente con solo uno o dos ejemplos in-contexto.

## Etiquetas
#LLM #Razonamiento #Actuación #IA

Fuente: http://arxiv.org/abs/2210.03629v3
