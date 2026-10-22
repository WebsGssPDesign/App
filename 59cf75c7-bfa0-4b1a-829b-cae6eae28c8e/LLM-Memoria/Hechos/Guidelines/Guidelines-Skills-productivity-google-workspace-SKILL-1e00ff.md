---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/productivity/google-workspace/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe la configuración y uso de la habilidad "Google Workspace" para interactuar con servicios como Gmail, Calendar y Drive mediante el CLI `gws` o Python. Su función principal es guiar al usuario en un flujo de configuración no interactivo para establecer credenciales OAuth2 seguras y autorizadas.

## Datos clave
- **Proyecto**: Hermes Agent (Nous Research).
- **Tecnologías**: Google OAuth2, gws CLI, Python client wrapper.
- **Archivos requeridos**: `google_token.json` y `google_client_secret.json`.
- **Pasos de configuración**:
  1. Definir la variable `GSETUP` apuntando a `scripts/setup.py`.
  2. Ejecutar `$GSETUP --check` para verificar estado.
  3. Consultar al usuario sobre los servicios necesarios (email, calendar, etc.) y si usan Advanced Protection.
  4. Crear credenciales OAuth2 en Google Cloud Console (Desktop app) y descargar el JSON.
  5. Ejecutar `$GSETUP --client-secret <ruta>` con la ruta del archivo de cliente.
  6. Obtener URL de autorización: `$GSETUP --auth-url --services <lista>`.
  7. Intercambiar código por token: `$GSETUP --auth-code "<código_o_url>"`.

## Etiquetas
#GoogleWorkspace #OAuth2 #HermesAgent #ProductivityTools

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\productivity\google-workspace\SKILL.md`
