---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-deep-research/agents/perspective.md"
tags: [hecho]
---
# perspective.md

## Resumen
Este documento define el contrato de ejecución y flujo de trabajo para un "Agente de Perspectiva" en un sistema de investigación profunda. Su función es auditar la cobertura de evidencia en dimensiones específicas contra coordenadas lentes predefinidas, identificando brechas de información sin inventar datos ni conclusiones no verificadas.

## Datos clave
- **Proyecto**: SenseNova-Skills (módulo de deep research).
- **Entradas**: `plan.json` (configuración del lente), evidencia JSON y query original.
- **Salida**: Markdown en `{report_dir}/sub_reports/d{N}.perspectives/{lens_id}.md`.
- **Reglas críticas**: No fabricar resultados si las herramientas fallan; distinguir entre "contexto de escritura" (no concluyente) y "requisitos de investigación" (datos faltantes).
- **Flujo**: Leer plan/evidencia -> Evaluar cobertura -> Buscar exploratorio (solo como pista) -> Generar feedback estructurado.

## Etiquetas
#SenseNova #DeepResearch #AgentesIA #AuditoríaDeEvidencia

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-deep-research\agents\perspective.md`
