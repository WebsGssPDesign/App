---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/docs/sn-deep-research_cn.md"
tags: [hecho]
---
# sn-deep-research_cn.md

## Resumen
Este documento describe la arquitectura unificada de `sn-deep-research`, que integra procesos previos de planificación, investigación y redacción en un único controlador. Permite ejecutar estudios profundos mediante tres modos (rápido, normal o pesado) utilizando múltiples agentes especializados y fuentes de búsqueda específicas como académicas, código o redes sociales.

## Datos clave
- **Entradas**: `/skill sn-deep-research` para uso integrado o `sn-deepresearch-cli` para línea de comandos independiente.
- **Modos de operación**: `quick` (un agente), `normal` (planificación + síntesis) y `heavy` (breve, revisión exhaustiva y ensamblaje).
- **Agentes principales**: `scout.md`, `plan.md`, `research.md`, `review.md`, `report-writer.md`.
- **Validadores críticos**: Scripts como `validate_briefing.py` y `validate_evidence.py` actúan como puertas de entrada obligatorias.
- **Fuentes de búsqueda**: Incluye módulos para académicos (`sn-search-academic`), código, finanzas y redes sociales chinas/angloparlantes.
- **Configuración**: Requiere variables de entorno en `.env` (ej. claves API) sin incluir credenciales reales en el payload o logs.

## Etiquetas
#SenseNova #InvestigaciónProfunda #AgentesIA #DocumentaciónTécnica

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\docs\sn-deep-research_cn.md`
