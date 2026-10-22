---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/childrentime/gotsx"
tema: "React Server Components Islands"
tags: [web]
---
# childrentime/gotsx

## Resumen
Gotsx es un framework full-stack que traduce código TSX a Go nativo sin depender de Node.js ni motores JS. Convierte componentes del servidor en funciones Go y las "islas" interactivas del cliente en señales, permitiendo una compilación directa a un único binario con alto rendimiento.

## Datos clave
- **Arquitectura:** Compilador TSX -> Go (sin virtual DOM ni runtime de React).
- **Rendimiento:** ~15 µs por página de 50 items y ~20k solicitudes/segundo en servidor GitHub Actions.
- **Tamaño:** Binario único, ~21 MB RSS, 9 KB JS comprimido para carga inicial.
- **Comandos principales:** `gotsx new <nombre>` (esqueleto), `gotsx dev` (desarrollo con recarga en vivo), `go build -o <bin> .` (producción).
- **Características:** Streaming SSR, sistema de diseño compartido, soporte para agentes de código vía `AGENTS.md`.

## Etiquetas
#Go #React #Compilación #FullStack #Rendimiento

Fuente: https://github.com/childrentime/gotsx
