---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-deep-research/agents/scout.md"
tags: [hecho]
---
# scout.md

## Resumen
Este documento define el contrato operativo para un agente de "reconocimiento" (Scout) dentro de un sistema de investigación profunda. Su función es mapear preliminarmente un tema de estudio, identificando entidades, controversias y vacíos sin generar respuestas finales ni planes detallados, sirviendo exclusivamente como base para la planificación posterior en modo "heavy".

## Datos clave
- **Rol único**: Generación de mapas preliminares (entidades, subdominios, consensos, disputas) sin escribir conclusiones.
- **Entradas fijas**: `mode=heavy`, `language` y `format` provistos por el payload; no se pueden modificar ni redefinir.
- **Jerarquía de incertidumbre**: Clasificación estricta en `user_confirmations_needed` (bloqueo), `critical_unknowns` (resolubles) y `coverage_boundary` (límites del escaneo).
- **Límites de extracción**: El scraping solo busca variables de planificación (URLs, alcance), prohibiéndose extraer datos, argumentos o citas como respuestas.
- **Métricas de éxito**: Cumplimiento de umbrales específicos por campo (ej. ≥5 entidades, ≥3 subdominios) y declaración explícita de límites en `coverage_boundary`.

## Etiquetas
#IA #Investigación #AgenteScout #Planificación

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-deep-research\agents\scout.md`
