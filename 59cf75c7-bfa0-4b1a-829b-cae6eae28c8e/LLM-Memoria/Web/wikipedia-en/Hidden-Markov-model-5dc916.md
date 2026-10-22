---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Hidden_Markov_model"
tema: "Temporal Workflow Observability"
tags: [web]
---
# Hidden Markov model

## Resumen
Un modelo de Markov oculto (HMM) es un sistema probabilístico donde las observaciones visibles dependen de un proceso subyacente no observable. El objetivo principal es inferir el estado del proceso oculto analizando la secuencia de datos observables, bajo la premisa de que el estado actual condiciona independientemente a los eventos pasados.

## Datos clave
- **Proceso oculto (X)**: Secuencia de estados latentes no directamente medibles.
- **Proceso observable (Y)**: Resultados visibles cuya distribución depende exclusivamente del estado X en ese instante.
- **Independencia condicional**: Dado el estado actual $X_n$, la observación $Y_n$ es independiente de todos los estados anteriores ($X_1, \dots, X_{n-1}$).
- **Algoritmos de estimación**: Máxima verosimilitud y algoritmo de Baum-Welch para cadenas lineales.
- **Aplicaciones**: Reconocimiento de voz, bioinformática, procesamiento de señales, finanzas y mecánica estadística.

#modelado #probabilidad #aprendizaje_automático #series_temporales

Fuente: https://en.wikipedia.org/wiki/Hidden_Markov_model
