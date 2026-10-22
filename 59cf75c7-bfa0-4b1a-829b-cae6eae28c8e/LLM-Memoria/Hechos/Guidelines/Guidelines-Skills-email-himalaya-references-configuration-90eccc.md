---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/email/himalaya/references/configuration.md"
tags: [hecho]
---
# configuration.md

## Resumen
Este documento detalla la configuración del archivo `config.toml` para el cliente de correo Himalaya, estableciendo conexiones IMAP/SMTP para proveedores como Gmail e iCloud. Su función principal es guiar al usuario en la definición de cuentas, autenticación segura y mapeo de carpetas para evitar errores comunes como el envío duplicado de correos.

## Datos clave
- **Ubicación del archivo**: `~/.config/himalaya/config.toml`.
- **Autenticación recomendada**: Usar comandos (`backend.auth.cmd`) o keyrings en lugar de contraseñas en texto plano para mayor seguridad.
- **Gmail crítico**: Es obligatorio usar las rutas de carpetas específicas (ej. `[Gmail]/Sent Mail`) bajo `folder.aliases` para evitar fallos al guardar como enviados y duplicar correos.
- **Comandos útiles**: `himalaya account configure <account>` para almacenar contraseñas; `himalaya --account <nombre> ...` para cambiar entre cuentas.
- **OAuth2**: Soporte para autenticación moderna mediante tokens rotativos.

## Etiquetas
#configuración #email #himalaya #seguridad

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\email\himalaya\references\configuration.md`
