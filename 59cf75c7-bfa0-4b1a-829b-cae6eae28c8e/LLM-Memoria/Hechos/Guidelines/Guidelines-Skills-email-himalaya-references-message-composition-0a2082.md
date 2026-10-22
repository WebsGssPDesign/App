---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/email/himalaya/references/message-composition.md"
tags: [hecho]
---
# message-composition.md

## Resumen
Este documento describe el lenguaje MML (MIME Meta Language) utilizado por Himalaya para compilar mensajes de correo electrónico XML en formato MIME. Explica la estructura básica de correos, sintaxis para partes múltiples (texto/HTML), adjuntos e imágenes incrustadas, y proporciona comandos CLI para redactar, responder y enviar mensajes.

## Datos clave
- **Proyecto**: Himalaya
- **Tecnologías**: MML (XML-based syntax), MIME
- **Comandos CLI importantes**: `himalaya message write`, `himalaya message reply <id>`, `himalaya message forward <id>`
- **Sintaxis clave**: `<#multipart type=alternative/mixed/related>`, `<#part filename="..." name="...">`
- **Flujo de trabajo**: Los comandos abren el editor `$EDITOR` con una plantilla; guardar y salir envía el correo.
- **Comando de inspección**: `himalaya message export --full` para ver la estructura MIME cruda.

## Etiquetas
#email #mml #himalaya #cli

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\email\himalaya\references\message-composition.md`
