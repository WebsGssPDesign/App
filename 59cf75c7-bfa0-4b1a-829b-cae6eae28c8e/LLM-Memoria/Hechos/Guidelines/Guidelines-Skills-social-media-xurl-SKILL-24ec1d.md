---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/social-media/xurl/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía documenta la configuración y uso de `xurl`, la línea de comandos oficial de X (Twitter) para gestionar publicaciones, búsquedas, mensajes directos y acceso a la API v2. Su función principal es permitir a los usuarios automatizar tareas en la plataforma social de forma segura, evitando el manejo directo de credenciales dentro del contexto de agentes o LLMs.

## Datos clave
- **Herramienta**: `xurl` (reemplaza al antiguo `xitter`).
- **Instalación**: Soporta scripts shell, Homebrew (`brew install --cask xdevplatform/tap/xurl`), npm y Go.
- **Configuración obligatoria fuera del agente**: El usuario debe registrar la aplicación en el portal de desarrolladores, añadir credenciales con `xurl auth apps add` y autenticar con OAuth 2.0 (`xurl auth oauth2`) manualmente.
- **Seguridad crítica**: Prohibido usar flags como `--bearer-token` o `--verbose`; nunca pegar tokens en chat. Los secretos se guardan en `~/.xurl`.
- **Pitfall Docker**: En entornos Hermes, la variable `HOME` debe ser `/opt/data/home` para que los subprocesos encuentren las credenciales.
- **Comandos rápidos**: `xurl post`, `xurl search`, `xurl timeline`, `xurl whoami`.

## Etiquetas
#xurl #twitter-api #seguridad #automatización #cli

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\social-media\xurl\SKILL.md`
