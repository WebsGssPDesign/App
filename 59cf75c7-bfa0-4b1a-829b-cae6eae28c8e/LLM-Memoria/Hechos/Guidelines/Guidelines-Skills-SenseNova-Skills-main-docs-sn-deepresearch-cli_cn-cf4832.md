---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/docs/sn-deepresearch-cli_cn.md"
tags: [hecho]
---
# sn-deepresearch-cli_cn.md

## Resumen
Este documento describe el uso de la CLI independiente `sn-deepresearch-cli` para ejecutar investigaciones profundas con seguimiento en tiempo real y capacidad de recuperación. Permite generar informes formales o breves utilizando diversos agentes (Hermes, Codex, Claude Code, OpenClaw) y soporta múltiples formatos de salida como Markdown, PDF o DOCX.

## Datos clave
- **Proyecto**: `sensenova-skills-deepresearch` (npm global).
- **Requisitos**: Node.js 22+, Python 3.10+, npm; herramientas opcionales: Pandoc y Typst.
- **Comandos principales**:
    - Instalación: `npm install --global sensenova-skills-deepresearch`.
    - Inicio rápido (CLI): `deepresearch "<query>" --mode quick ...`
    - Inicio avanzado (Web): `deepresearch web "<query>" --mode normal|heavy ... --port <puerto>`.
- **Gestión deHarness**: Verificar estado con `deepresearch doctor --harness openclaw --json`; restaurar ejecuciones interrumpidas con `deepresearch resume <run-id>`.
- **Configuración**: Credenciales de búsqueda en `~/.deepresearch-cli/search/.env`.

## Etiquetas
#SenseNova #CLI #InvestigaciónProfunda #Automatización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\docs\sn-deepresearch-cli_cn.md`
