---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-deep-research/agents/research.md"
tags: [hecho]
---
# research.md

## Resumen
Este documento define el protocolo operativo para un Agente de Investigación que recopila evidencia estructurada en archivos JSON. Su función es ejecutar búsquedas multidimensionales utilizando habilidades especializadas (académicas, código, redes sociales) y filtrar resultados mediante una estrategia de temporalidad estricta antes de generar la verdad única del informe.

## Datos clave
- **Entradas**: `plan.json` para dimensiones iniciales/suplementarias; `confirmed_scope` para búsquedas rápidas (`quick`).
- **Habilidades obligatorias**: Mapeo de categorías `sources` a skills específicos (ej. `sn-search-academic`, `sn-search-code`) antes de usar búsqueda web genérica.
- **Ciclo de trabajo**: Fase 1 (Estrategia) → Fase 2 (Búsqueda → Fetch → Evaluación) → Fase 3 (Extracción).
- **Reglas de parada**: Basadas en el nivel `depth` (`skim`, `moderate`, `thorough`) y cobertura de `key_questions`.
- **Gestión de errores**: Si un skill especializado falla por falta de configuración, usar búsqueda web genérica como respaldo sin bloquear la ejecución.

## Etiquetas
#investigación #automatización #evidencia #json #agentes

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-deep-research\agents\research.md`
