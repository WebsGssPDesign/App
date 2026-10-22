---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/apple/imessage/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define las directrices para utilizar la herramienta `imsg` en macOS, permitiendo a los agentes enviar y recibir mensajes de texto e iMessage a través de la aplicación Mensajes. Su función principal es automatizar la gestión de conversaciones individuales, incluyendo el envío de archivos y la consulta del historial, bajo estrictas reglas de seguridad para evitar envíos no autorizados o masivos.

## Datos clave
- **Proyecto**: Herramienta `imsg` (CLI) para macOS.
- **Tecnologías**: macOS, Messages.app, Homebrew (`steipete/tap/imsg`).
- **Permisos críticos**: Acceso completo al disco y permisos de automatización en la configuración del sistema.
- **Comandos principales**: `imsg chats` (listar), `imsg history` (ver historial), `imsg send` (enviar texto/archivos), `imsg watch` (monitoreo).
- **Opciones de servicio**: `--service imessage`, `--service sms`, `--service auto`.
- **Flujo de trabajo seguro**: Buscar chat → Confirmar destinatario y contenido con el usuario → Enviar.
- **Restricciones**: No soporta grupos, ni Telegram/Discord/WhatsApp; requiere confirmación explícita antes de enviar a números desconocidos.

## Etiquetas
#macOS #iMessage #Automatización #Seguridad #CLI

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\apple\imessage\SKILL.md`
