---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Tokio_%28software%29"
tema: "Rust Async Runtime"
tags: [web]
---
# Tokio (software)

## Resumen
Tokio es una biblioteca de software en Rust que ofrece un runtime y funciones para operaciones de entrada/salida asíncronas, facilitando la concurrencia. Desarrollada inicialmente como marco de aplicaciones de red, permite gestionar múltiples tareas sin bloquear el hilo principal mediante un programador de trabajo robado multihilo.

## Datos clave
- **Lenguaje**: Rust.
- **Desarrollador original**: Carl Lerche (agosto 2016).
- **Runtime**: Utiliza `#[tokio::main]` para inicialización y `tokio::spawn` para tareas asíncronas en un pool de hilos que multiplica la ejecución.
- **Sincronización**: Incluye primitivas como bloqueos, semáforos y canales funcionales fuera del contexto del runtime.
- **Hilos bloqueantes**: Permite operaciones síncronas (ej. sistema de archivos) mediante `tokio::task::spawn_blocking`.
- **Soporte de sistemas**: Usa llamadas al sistema como epoll (Linux), kqueue (FreeBSD) y IOCP (Windows); soporta io_uring vía `tokio-uring`.
- **Usuarios destacados**: Equipos de Discord, AWS Lambda y el runtime Deno.

## Etiquetas
#Rust #Tokio #ProgramaciónAsíncrona #SoftwareLibre #Concurrencia

Fuente: https://en.wikipedia.org/wiki/Tokio_%28software%29
