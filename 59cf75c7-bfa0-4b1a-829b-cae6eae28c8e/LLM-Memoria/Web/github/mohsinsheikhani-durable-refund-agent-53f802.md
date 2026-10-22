---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/mohsinsheikhani/durable-refund-agent"
tema: "Temporal Workflow Idempotency"
tags: [web]
---
# mohsinsheikhani/durable-refund-agent

## Resumen
Este repositorio presenta un agente de reembolso impulsado por LLM diseñado para operar en producción con seguridad financiera, utilizando Temporal para la ejecución durable y LangGraph para el flujo de trabajo. El proyecto demuestra cómo construir sistemas que sobrevivan a fallos técnicos como reinicios o duplicación de pagos mediante mecanismos de idempotencia y aprobaciones humanas integradas.

## Datos clave
- **Tecnologías:** Python 3.14, Temporal (ejecución durable), LangGraph 1.x, LiteLLM, OpenAI `gpt-4o-mini`, Langfuse, OpenTelemetry.
- **Patrones de seguridad:** Claves de idempotencia únicas (`workflow_id:activity_id`), ejecución "al menos una vez" convertida en "exactamente una vez", registro contable append-only (JSONL).
- **Control humano:** Puerta de aprobación con espera de hasta 48 horas que persiste tras reinicios del worker.
- **Resultados probados:** Inyección de fallos confirma que múltiples ejecuciones no duplican el pago; trazas en Langfuse son reproducibles y únicas a pesar de los replays.
- **Gobernanza:** La lógica de políticas reside en archivos separados (`policy.py`) para auditoría, no en prompts.

## Etiquetas
#agentesLLM #Temporal #LangGraph #idempotencia #FinTech #producción

Fuente: https://github.com/mohsinsheikhani/durable-refund-agent
