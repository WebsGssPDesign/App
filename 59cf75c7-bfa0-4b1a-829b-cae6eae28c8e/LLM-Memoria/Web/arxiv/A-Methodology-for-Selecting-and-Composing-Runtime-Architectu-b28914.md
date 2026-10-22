---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2605.20173v2"
tema: "Rust Async Runtime Patterns"
tags: [web]
---
# A Methodology for Selecting and Composing Runtime Architecture Patterns for Production LLM Agents

## Resumen
Este artículo propone el "límite estocástico-determinístico" (SDB) como elemento central para diseñar agentes de LLM en producción, definiéndolo como un contrato entre la salida del modelo y las acciones del sistema. Se presenta un catálogo de seis patrones de arquitectura que organizan este límite según los roles de coordinación, estado y control, junto con una metodología de cinco pasos para su selección.

## Datos clave
- **Límite estocástico-determinístico (SDB):** Contrato de cuatro partes (proponente, verificador, paso de compromiso y señal de rechazo).
- **Patrones de arquitectura:** Delegación jerárquica, dispersión-recolección más saga, secuenciación impulsada por eventos, máquina de estados compartida, supervisor con puerta y humano en el bucle.
- **Modo de fallo "divergencia de reproducción":** Ocurre cuando consumidores basados en LLM generan salidas diferentes al consumir un registro de eventos determinista tras cambios en la versión del modelo o el prompt.
- **Implementación:** Un agente de renovación de contratos con contrato de 90 días.

## Etiquetas
#arquitectura_llm #agentes_autónomos #ingreso_de_escalada #patrones_de_diseño

Fuente: http://arxiv.org/abs/2605.20173v2
