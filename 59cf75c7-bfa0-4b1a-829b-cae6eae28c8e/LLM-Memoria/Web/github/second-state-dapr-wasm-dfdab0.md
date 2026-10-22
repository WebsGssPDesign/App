---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/second-state/dapr-wasm"
tema: "Dapr Sidecar"
tags: [web]
---
# second-state/dapr-wasm

## Resumen
Este proyecto demuestra cómo ejecutar funciones WebAssembly escritas en Rust como microservicios sidecar dentro de la plataforma Dapr utilizando el runtime WasmEdge, ofreciendo una alternativa más ligera y segura que los contenedores tradicionales. El ejemplo incluye tres servicios: conversión a escala de grises, clasificación de imágenes con TensorFlow y registro de eventos en MySQL.

## Datos clave
- **Tecnologías**: Dapr (sidecar), WasmEdge (runtime), Rust (lenguaje), WebAssembly (formato).
- **Ventajas**: Mejor seguridad, mayor rendimiento y menor huella de memoria comparado con contenedores Linux o VMs.
- **Comandos principales**: `cargo build --target wasm32-wasi`, `wasmedge compile`, `dapr run`.
- **Servicios incluidos**: `image-api-grayscale` (procesamiento), `image-api-classify` (IA/TensorFlow), `events-service` (persistencia en MySQL).
- **Configuración**: Requiere instalación de Dapr CLI, WasmEdge y una base de datos (MySQL/MariaDB/TiDB) con credenciales en `config/secrets.json`.

## Etiquetas
#WebAssembly #Dapr #WasmEdge #Rust #Microservicios

Fuente: https://github.com/second-state/dapr-wasm
