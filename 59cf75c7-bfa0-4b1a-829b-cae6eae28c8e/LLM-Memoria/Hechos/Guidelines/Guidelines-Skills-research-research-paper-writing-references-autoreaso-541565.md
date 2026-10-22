---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/research/research-paper-writing/references/autoreason-methodology.md"
tags: [hecho]
---
# autoreason-methodology.md

## Resumen
Este documento detalla la metodología "Autoreason", un enfoque de refinamiento iterativo para mejorar salidas de modelos LLM en tareas subjetivas o complejas. Sirve como guía práctica para seleccionar estrategias óptimas según el modelo y el tipo de tarea, evitando degradación progresiva mediante un bucle estructurado con roles aislados (Critic, Author, Synthesizer).

## Datos clave
- **Selección estratégica**: Úsalo en modelos de nivel medio (ej. Haiku 3.5) para tareas subjetivas; evita en modelos débiles (degradación) o fronterizos no restringidos (deriva sintética).
- **Arquitectura del bucle**: Roles aislados: Critic (identifica problemas), Author B (revisa), Synthesizer (fusiona lo mejor), Judge Panel (evalúa ciegamente).
- **Parámetros críticos**: Convergencia $k=2$ (evita costos excesivos de $k=3$); Temperatura Autor 0.7-0.8; Juez 0.3.
- **Configuración avanzada**: 3 jueces por paso, 7 para la evaluación final; Max tokens 4096 (8192 para papers).
- **Prompting**: Uso obligatorio de Chain-of-thought en jueges para acelerar convergencia y empate conservador (incumbente gana si no es claramente peor).

## Etiquetas
#autoreason #llm-refinement #methodology #prompt-engineering

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\research\research-paper-writing\references\autoreason-methodology.md`
