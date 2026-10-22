---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-deep-research/agents/review.md"
tags: [hecho]
---
# review.md

## Resumen
Esta guía define el protocolo del "Agente de Revisión" para auditar la calidad semántica, la integridad de las fuentes y el cumplimiento estructural en proyectos de investigación profunda. Su función es validar que cada afirmación tenga soporte verificable y que los productos finales respeten estrictamente los contratos de formato y decisiones organizativas aprobadas por el usuario.

## Datos clave
- **Entrada**: El agente recibe un `payload` con query, rutas absolutas (`report_dir`, `plugin_skills_dir`) y tipo de revisión (sub-reportes o producto final).
- **Validación previa**: No repite tareas mecánicas; delega la verificación sintáctica a `validate_evidence.py` y `validate_outline.py`.
- **Clasificación de fuentes**: Evalúa el nivel de confianza (`trusted_primary`, `professional_secondary`, `weak_untrusted`) basado en la relevancia para la afirmación, no solo en el dominio.
- **Verificación independiente (A4)**: Para fuentes débiles, busca evidencia externa independiente usando entidades clave, evitando cadenas de retransmisión.
- **Consistencia Claim-Evidence**: Prohíbe inferencias causales o numéricas no presentes en el texto fuente; exige que las interpretaciones tengan múltiples fuentes independientes.
- **Cumplimiento estructural**: Verifica que los `content units` del `outline.json` se rendericen exactamente según su contrato (`render_contract`) sin añadir elementos implícitos como resúmenes automáticos.

## Etiquetas
#auditoría #investigación_profunda #calidad_de_datos #contratos_técnicos

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-deep-research\agents\review.md`
