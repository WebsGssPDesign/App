---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/monoio-rs/monoio"
tema: "Rust Async Runtime"
tags: [web]
---
# monoio-rs/monoio

## Resumen
Monoio es un runtime asíncrono para Rust basado en `io_uring`, diseñado específicamente con un modelo de "un hilo por núcleo". A diferencia de Tokio, no depende de otro runtime y elimina la necesidad de que las tareas sean `Send` o `Sync`, optimizando el rendimiento para servidores de alta concurrencia.

## Datos clave
- **Modelo de ejecución:** Un hilo por núcleo (thread-per-core).
- **Drivers de E/S:** Soporta `io_uring` en Linux 5.6+, `epoll` y `kqueue` en macOS.
- **Requisitos:** Rust 1.75+; requiere configuración adecuada de `memlock`.
- **Ventaja principal:** Mayor rendimiento que Tokio al evitar la migración de datos entre hilos, ideal para cargas de trabajo atadas a I/O (ej. balanceadores).
- **Limitaciones:** No soporta todas las plataformas; puede degradarse si la carga es muy desequilibrada.

## Etiquetas
#Rust #AsyncRuntime #io_uring #HighPerformance #Networking

Fuente: https://github.com/monoio-rs/monoio
