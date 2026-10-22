---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/pion/webrtc"
tema: "WebAssembly Streaming"
tags: [web]
---
# pion/webrtc

## Resumen
Pion WebRTC es una implementación pura en Go de la API estándar WebRTC, diseñada para facilitar el desarrollo de aplicaciones multimedia sin dependencias externas complejas. La versión 4.0.0 introduce mejoras significativas y cambios rotundos respecto a versiones anteriores, manteniendo compatibilidad con las especificaciones oficiales del W3C.

## Datos clave
- **Idioma**: Implementación nativa en Go (sin Cgo para la mayoría de funciones).
- **Versión actual**: v4.0.0 (requiere importar explícitamente `/v4`).
- **Protocolos soportados**: ICE, STUN, TURN (UDP/TCP/DTLS/TLS), mDNS.
- **Códigos de códec**: Opus, PCM, H264, VP8, VP9.
- **Características principales**: DataChannels (ordenados/perdidos), renegotiation, Plan-B y Unified Plan.
- **Requisito obligatorio**: Uso de Go Modules (`export GO111MODULE=on`).
- **Licencia**: MIT.

## Etiquetas
#WebRTC #GoLang #VideoStreaming #AudioProcessing #OpenSource

Fuente: https://github.com/pion/webrtc
