---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://github.com/damienbod/angular-auth-oidc-client"
tema: "OAuth2 Flows"
tags: [web]
---
# damienbod/angular-auth-oidc-client

## Resumen
Esta librería de Angular facilita la implementación segura de autenticación con estándares modernos de OpenID Connect y OAuth2. Ofrece soporte para flujos de código, tokens de refresco e implícitos, validando firmas de tokens mediante criptografía web. Incluye herramientas de instalación automática y documentación completa para configurar proveedores de identidad.

## Datos clave
- **Comandos de instalación**: `ng add angular-auth-oidc-client`, `npm install angular-auth-oidc-client`.
- **Configuración principal**: Requiere definir `authority`, `clientId`, `scope` (incluyendo `offline_access`) y `responseType`.
- **Flujos soportados**: Code Flow con PKCE, Implicit Flow, gestión de sesiones y revocación de tokens (RFC7009).
- **Validación de seguridad**: Verificación de firmas `id_token` usando algoritmos RS256/PS256/ES256/EdDSA.
- **Método crítico**: `checkAuth()` debe llamarse en el componente raíz para procesar redirecciones del servidor.

## Etiquetas
#Angular #OpenIDConnect #OAuth2 #SeguridadWeb #Autenticación

Fuente: https://github.com/damienbod/angular-auth-oidc-client
