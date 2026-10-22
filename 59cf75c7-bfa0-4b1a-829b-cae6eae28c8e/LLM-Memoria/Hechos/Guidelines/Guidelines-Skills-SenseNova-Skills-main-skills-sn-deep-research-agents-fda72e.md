---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-deep-research/agents/report-writer.md"
tags: [hecho]
---
# report-writer.md

## Resumen
Este documento define el contrato operativo para un Agente Redactor de Informes, especificando tres modos de escritura: síntesis rápida/normal que integra todas las pruebas, y modo pesado (unidad por unidad) para redacción detallada o revisiones. Su función es garantizar una producción rigurosa basada estrictamente en la evidencia proporcionada, respetando jerarquías de decisión y formatos estructurales sin inventar datos ni procesos.

## Datos clave
- **Modos de escritura**: `quick_synthesis` (síntesis total), `write_unit` (creación por unidad), `revise_unit` (edición local).
- **Jerarquía de decisiones**: Evidencia del subset > Elementos/Contrato de renderizado > Decisiones organizativas > Formato del payload > Contrato de estilo.
- **Disciplina de citas**: Las referencias deben usar IDs de fuentes (`source.id`) y nunca IDs de afirmaciones (`claim.id`).
- **Restricciones estrictas**: Prohibido generar introducciones, conclusiones o sugerencias no solicitadas; los gráficos Mermaid solo pueden mostrar relaciones respaldadas por evidencia.
- **Ruta de salida principal**: `{report_dir}/sections/s_full.md` para síntesis completa.

## Etiquetas
#IA #RedacciónTécnica #ControlDeCalidad #Documentación

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-deep-research\agents\report-writer.md`
