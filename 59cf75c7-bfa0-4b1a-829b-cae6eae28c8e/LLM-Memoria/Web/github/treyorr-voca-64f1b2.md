---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://github.com/treyorr/voca"
tema: "React Server Signals"
tags: [web]
---
# treyorr/voca

## Resumen
Voca es un servidor de señalización de voz WebRTC de alto rendimiento escrito en Rust, diseñado para ser autohospedable y sin estado. Facilita salas efímeras de chat de voz puramente peer-to-peer donde el audio nunca toca el servidor, garantizando privacidad y velocidad instantánea mediante cifrado DTLS-SRTP.

## Datos clave
- **Características principales**: Sin persistencia de datos, sin autenticación obligatoria, salas efímeras y cifrado auditivo.
- **SDKs disponibles**: `@treyorr/voca-client` (núcleo), `@treyorr/voca-react` y `@treyorr/voca-svelte`.
- **Instalación rápida**: `bun install @treyorr/voca-client` o las variantes para React/Svelte.
- **Endpoints API destacados**: `POST /api/room` (crear sala), `GET /ws/{id}` (señalización WebSocket).
- **Desarrollo local**: Requiere ejecutar el servidor de señalización en Rust y la interfaz web separadamente, o usar `mise run dev`.
- **Licencia**: MIT.

## Etiquetas
#WebRTC #Rust #Autohospedable #ChatDeVoz #OpenSource

Fuente: https://github.com/treyorr/voca
