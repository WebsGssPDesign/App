---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2610.22264v1"
tema: "OpenTelemetry Scope Span Context Propagation"
tags: [web]
---
# SCOPE: Semantic Bounded Credit Optimization for Prompt Engineering in Text-to-image Generation

## Resumen
SCOPE es un método de optimización basado en aprendizaje por refuerzo que mejora la generación imagen-texto alineando los pesos de actualización con estructuras semánticas coherentes, como objetos y atributos. A diferencia de métodos existentes que aplican señales individuales a subpalabras, SCOPE agrupa cambios dentro de estas unidades semánticas para derivar coeficientes compartidos sin necesidad de recompensas separadas ni nuevos renders de imágenes.

## Datos clave
- **Método**: Group Relative Policy Optimization (GRPO).
- **Funcionamiento**: Genera conjuntamente un prompt mejorado y su partición semántica; pool cambios en probabilidades log dentro de cada tramo para coeficientes compartidos.
- **Ventajas**: No requiere recompensas por tramos ni renders adicionales de imágenes.
- **Resultados**: Ganancias relativas promedio del 9,48% en GeneVal y 7,62% en T2I-CompBench frente a GRPO estándar.
- **Modelos evaluados**: Qwen-Image, SD3, FLUX.1-dev.

## Etiquetas
#aprendizaje_por_refuerzo #ingenería_de_prompts #generación_imagen #SCOPE #GRPO

Fuente: http://arxiv.org/abs/2610.22264v1
