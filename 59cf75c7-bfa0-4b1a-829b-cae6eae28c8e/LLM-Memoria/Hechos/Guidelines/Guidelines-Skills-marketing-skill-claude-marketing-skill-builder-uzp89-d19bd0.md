---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/marketing-skill-claude-marketing-skill-builder-uzp891/state/outreach-log.md"
tags: [hecho]
---
# outreach-log.md

## Resumen
Este archivo actúa como registro diario y lista de supresión permanente para la campaña de email marketing, sirviendo como única fuente de verdad para evitar duplicados y gestionar contactos. Permite rastrear el estado de cada prospecto desde el borrador hasta la respuesta o el rebote, integrando detecciones automáticas del buzón de Gmail.

## Datos clave
- **Proyecto:** Sistema de prospección "Vibe Prospecting" (módulo `email-outreach`).
- **Tecnologías:** Integración con Gmail MCP para sincronización de bandeja de entrada y detección automática de respuestas/rebotes.
- **Reglas de identidad:** Prioridad en orden: Email > LinkedIn > Nombre + Empresa.
- **Estados críticos:** `Unsubscribed`, `Bounced` y `Replied` son supresiones permanentes; `Skipped-Duplicate` para evitar duplicados dentro de la ventana de 90 días.
- **Separación de deberes:** El sistema solo puede marcar como `Drafted`, `Ready for Approval` o `Skipped-Duplicate`. El estado `Approved` requiere intervención humana explícita tras revisar el correo en vivo.
- **Formato:** Tabla Markdown donde los pipes (`|`) deben escaparse como `\|` y cada celda debe ser una sola línea.

## Etiquetas
#email-marketing #gestion-de-contactos #automatizacion-gmail #supresion-lista

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\marketing-skill-claude-marketing-skill-builder-uzp891\state\outreach-log.md`
