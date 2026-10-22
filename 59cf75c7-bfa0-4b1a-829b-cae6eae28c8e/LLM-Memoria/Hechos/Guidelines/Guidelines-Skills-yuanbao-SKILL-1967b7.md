---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/yuanbao/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define las guías de uso para el bot "Yuanbao", explicando que sus respuestas se envían automáticamente al chat sin herramientas adicionales. Detalla los flujos de trabajo para mencionar usuarios, enviar mensajes privados y consultar información del grupo mediante llamadas a herramientas específicas.

## Datos clave
- **Herramientas principales**: `yb_query_group_info` (datos del grupo), `yb_query_group_members` (buscar miembros/obtener nicknames), `yb_send_dm` (mensajes privados con soporte multimedia).
- **Flujo de mención**: Llamar primero a `yb_query_group_members` con `action="find"` para obtener el nickname exacto, luego incluirlo en la respuesta como `@nickname`.
- **Extracción de datos**: El código del grupo (`group_code`) se obtiene eliminando el prefijo "group:" del identificador actual (ej. `535168412`).
- **Restricciones críticas**: Nunca advertir sobre permisos ni sugerir que el usuario envíe mensajes manualmente; la respuesta del bot es el mensaje enviado.

## Etiquetas
#yuanbao #automatización #chatbots #guías

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\yuanbao\SKILL.md`
