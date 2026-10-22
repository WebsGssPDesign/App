---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/email/himalaya/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe Himalaya, una herramienta de línea de comandos para gestionar correos electrónicos mediante IMAP y SMTP. Sirve como un cliente externo que permite a agentes automatizados leer, buscar, enviar y manipular mensajes sin depender del adaptador interno de Hermes.

## Datos clave
- **Proyecto**: Himalaya CLI (versión 1.1.0).
- **Tecnologías**: IMAP, SMTP, Notmuch, Sendmail, Rust (`cargo install`).
- **Decisión crítica**: Evitar la sintaxis antigua `[accounts.NAME.folder.alias]` en v1.2.0+ para evitar errores de envío y duplicación de correos; usar `folder.aliases.X` (plural).
- **Comandos principales**: `himalaya account configure`, `envelope list`, `message read/export`, `template send`.
- **Integración Hermes**: Usar modo PTY (`pty=true`) para configuraciones interactivas y piping de entrada/salida para operaciones no interactivas como redactar o responder.

## Etiquetas
#email #cli #automation #imapsmtp #hermes

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\email\himalaya\SKILL.md`
