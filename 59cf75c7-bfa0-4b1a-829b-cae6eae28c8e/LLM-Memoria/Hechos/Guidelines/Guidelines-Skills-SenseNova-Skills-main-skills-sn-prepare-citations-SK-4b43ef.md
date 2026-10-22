---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-prepare-citations/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe el script `sn-prepare-citations`, diseñado para procesar informes finales de investigación profunda. Su función principal es normalizar las referencias, eliminar duplicados y generar una lista bibliográfica ordenada en un archivo Markdown listo para publicación.

## Datos clave
- **Proyecto**: sn-deep-research (versión v2).
- **Tecnologías**: Python 3 (`scripts/prepare_citations.py`).
- **Entradas principales**: `stitched.md` (informe consolidado), archivos `d*.evidence.json` (metadatos de fuentes) y opcionalmente `outline.json`.
- **Lógica crítica**: Normaliza URLs para deduplicar, reemplaza marcadores como `[^source_id]` por `[N]`, detecta fugas de IDs de afirmaciones (`claim-id leakage`) y genera un archivo JSON estructurado con errores.
- **Flujo de control**: Si existen citas huérfanas o fugas de IDs no resueltas, el script impide la entrega del informe para su corrección previa.

## Etiquetas
#sn-deep-research #gestión-de-citas #automatización-python #investigación-académica

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-prepare-citations\SKILL.md`
