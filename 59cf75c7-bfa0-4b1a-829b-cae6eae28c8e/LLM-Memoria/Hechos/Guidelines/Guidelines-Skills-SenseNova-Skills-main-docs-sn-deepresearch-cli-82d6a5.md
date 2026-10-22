---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/docs/sn-deepresearch-cli.md"
tags: [hecho]
---
# sn-deepresearch-cli.md

## Resumen
Este documento describe la instalación y operación de `sn-deepresearch-cli`, una herramienta independiente para realizar investigaciones multi-fuente con seguimiento de progreso y generación de informes. Sirve como punto de entrada alternativo al controlador integrado, permitiendo la selección explícita de orquestadores (Harness) y el monitoreo detallado de las ejecuciones.

## Datos clave
- **Requisitos**: Node.js 22+, Python 3.10+, npm, Pandoc (DOCX) y Typst (PDF).
- **Instalación**: `npm install --global sensenova-skills-deepresearch`.
- **Configuración de fuentes**: `deepresearch sources init` e inicialización bajo `~/.deepresearch-cli/search/.env`.
- **Orquestadores soportados**: Hermes, Codex, Claude Code y OpenClaw (requiere prueba de escritura previa).
- **Ejecución rápida**: Usa el comando directo con modo `quick` para consultas cortas.
- **Ejecución normal/pesada**: Requiere servidor web (`deepresearch web`) en un puerto local para monitoreo continuo.
- **Recuperación**: Uso de `deepresearch resume <run-id>` para continuar ejecuciones interrumpidas sin borrar el directorio original.

## Etiquetas
#SenseNova #CLI #InvestigaciónAutomatizada #OpenSource

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\docs\sn-deepresearch-cli.md`
