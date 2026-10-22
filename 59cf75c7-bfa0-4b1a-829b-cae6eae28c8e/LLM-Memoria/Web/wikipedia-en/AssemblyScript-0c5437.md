---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/AssemblyScript"
tema: "WebAssembly Streaming"
tags: [web]
---
# AssemblyScript

## Resumen
AssemblyScript es un lenguaje de programación basado en TypeScript diseñado específicamente para ser compilado estáticamente a WebAssembly. Su sintaxis familiar reduce la curva de aprendizaje para desarrolladores de JavaScript, permitiendo obtener rendimiento nativo en navegadores y entornos no web mediante WASI sin abandonar las herramientas del ecosistema JS.

## Datos clave
- **Lenguaje base**: TypeScript con tipos estáticos explícitos (subconjunto).
- **Compilador principal**: `asc` (basado en Binaryen), disponible vía npm.
- **Rendimiento**: Compilación ahead-of-time para ejecución nativa o nivel máquina.
- **Características**: Soporte directo a intrínsecas de bajo nivel (SIMD, clz, ctz, popcnt).
- **Ecosistema WASI**: Permite ejecutar código fuera del navegador en entornos como Wasmtime y Wasmer.
- **Adopción**: Más de 29.000 proyectos en GitHub al mayo de 2025; ~50.000 descargas semanales de `asc`.
- **Uso práctico**: Webpack lo usa para acelerar funciones hash (xxhash, md4) eliminando dependencias nativas.

## Etiquetas
#AssemblyScript #WebAssembly #TypeScript #CompilaciónEstática #DesarrolloWeb

Fuente: https://en.wikipedia.org/wiki/AssemblyScript
