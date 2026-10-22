---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/software-development/spike/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define el protocolo "spike" para validar ideas mediante experimentos descartables antes de construir soluciones definitivas. Su objetivo es reducir riesgos explorando la viabilidad técnica a través de un ciclo iterativo de descomposición, investigación y construcción rápida.

## Datos clave
- **Proyecto**: Skill `spike` del sistema GSD (Get-Shit-Done), versión 1.0.0.
- **Metodología**: Ciclo `decompose → research → build → verdict`.
- **Descomposición**: Crear una tabla con 2-5 preguntas de viabilidad independientes, ordenadas por riesgo (mayor primero).
- **Tipos de spikes**: `standard` (una aproximación) y `comparison` (múltiples enfoques para la misma pregunta).
- **Herramientas sugeridas**: `web_search`, `web_extract`, `terminal`, `read_file`.
- **Entorno de construcción**: Directorios aislados (`spikes/001-nombre/`) con archivos `README.md` y código mínimo.
- **Salida preferida**: CLI ejecutable o HTML minimalista para feedback tangible.
- **Restricciones**: Evitar Docker, bundlers o gestión compleja de dependencias; hardcodear configuraciones.

## Etiquetas
#spike #prototipado #validación #desarrollo-rápido #gsd

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\software-development\spike\SKILL.md`
