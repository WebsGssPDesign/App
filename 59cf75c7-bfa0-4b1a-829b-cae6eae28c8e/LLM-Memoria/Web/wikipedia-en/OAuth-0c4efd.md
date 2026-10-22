---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/OAuth"
tema: "OAuth2 Flows"
tags: [web]
---
# OAuth

## Resumen
OAuth es un estándar abierto para la delegación de acceso que permite a los usuarios conceder a aplicaciones terceros el acceso seguro a sus datos sin compartir contraseñas. Diseñado para funcionar con HTTP, facilita que servidores de autorización emitan tokens de acceso aprobados por los dueños de los recursos. La versión 2.0 es la actual estándar predominante, aunque se encuentra en desarrollo una versión 2.1 para consolidar mejores prácticas y seguridad.

## Datos clave
- **Versiones principales**: OAuth 1.0 (RFC 5849) y OAuth 2.0 (RFC 6749). La 2.0 no es compatible hacia atrás con la 1.0.
- **Mecanismo central**: Uso de "tokens de acceso" (access tokens) emitidos por un servidor de autorización tras el consentimiento del dueño del recurso.
- **Tipos de concesión (grant types)**: Authorization Code, Proof Key for Code Exchange (PKCE), Client Credentials, Device Code, Refresh Token y Resource Owner Password Credentials (ROPC).
- **Seguridad**: Vulnerabilidades históricas incluyen "session fixation" en v1.0 y ataques como "Open Redirector", "Covert Redirect" o "AS Mix-Up Attack". Se recomienda el uso de PKCE para prevenir inyecciones de código.
- **Adopción**: Utilizado por grandes empresas como Google, Meta, Microsoft y Amazon; Twitter requirió su uso obligatorio desde agosto de 2010.

## Etiquetas
#OAuth #Ciberseguridad #Autenticación #APIs #Tokens

Fuente: https://en.wikipedia.org/wiki/OAuth
