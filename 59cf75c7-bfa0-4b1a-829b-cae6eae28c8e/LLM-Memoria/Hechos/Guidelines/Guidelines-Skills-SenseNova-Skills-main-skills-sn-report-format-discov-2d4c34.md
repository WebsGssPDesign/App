---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-report-format-discovery/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define una habilidad para determinar el formato de entrega de un informe de investigación basándose en las necesidades del usuario. Su función es generar un identificador breve (como "report" o "paper") que se usa solo en la memoria contextual actual, sin crear archivos ni esquemas formales.

## Datos clave
- **Nombre de la habilidad**: `sn-report-format-discovery`
- **Entradas principales**: La consulta original (`query`), el idioma solicitado y cualquier formato explícito indicado por el usuario.
- **Lógica de decisión**: Priorizar la elección del usuario; si no hay indicación, inferir según la tarea principal o usar "report" como valor predeterminado.
- **Restricciones críticas**: No generar archivos JSON ni esquemas (schema), no buscar normas externas y no modificar el alcance o las preguntas de investigación originales.
- **Salida requerida**: Una única línea con el formato `format: <string>`.

## Etiquetas
#gestión-de-formatos #investigación-inteligente #guías-técnicas

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-report-format-discovery\SKILL.md`
