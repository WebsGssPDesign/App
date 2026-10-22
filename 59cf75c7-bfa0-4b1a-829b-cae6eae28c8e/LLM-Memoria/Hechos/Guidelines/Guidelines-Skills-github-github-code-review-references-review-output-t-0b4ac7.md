---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/github/github-code-review/references/review-output-template.md"
tags: [hecho]
---
# review-output-template.md

## Resumen
Este documento define una plantilla estandarizada para generar comentarios de revisión de código en solicitudes de extracción (PR). Su objetivo es estructurar la retroalimentación por niveles de severidad, facilitando la identificación rápida de errores críticos y mejorando la claridad de las decisiones de fusión.

## Datos clave
- **Estructura del reporte**: Incluye secciones para Veredicto, Resumen del PR, Críticos (bloqueantes), Advertencias, Sugerencias y Refuerzos positivos ("Looks Good").
- **Guía de severidad**: Establece cuatro niveles: 🔴 Crítico (vulnerabilidades, fallos), ⚠️ Advertencia (bugs no críticos, falta de tests), 💡 Sugerencia (estilo, refactorización) y ✅ Looks Good.
- **Lógica del veredicto**: "Approved" solo si no hay ítems críticos o advertencias; "Changes Requested" si existen bloqueantes; "Reviewed" para observaciones informativas.
- **Comentarios en línea**: Requieren prefijo de icono de severidad seguido de la descripción y, opcionalmente, una sugerencia de corrección.
- **Revisión local**: Permite adaptar el formato omitiendo los metadatos del PR para enviar mensajes directos al usuario antes del push.

## Etiquetas
#revisión-de-código #plantillas #calidad-del-código #github

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\github\github-code-review\references\review-output-template.md`
