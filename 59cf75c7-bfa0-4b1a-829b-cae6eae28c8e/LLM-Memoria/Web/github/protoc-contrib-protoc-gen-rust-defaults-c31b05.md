---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/protoc-contrib/protoc-gen-rust-defaults"
tema: "gRPC Protobuf Oneof Messages"
tags: [web]
---
# protoc-contrib/protoc-gen-rust-defaults

## Resumen
Este proyecto es un complemento para `protoc` que genera métodos `set_defaults()` en Rust para mensajes generados con la biblioteca `buffa`. Permite definir valores por defecto una sola vez en el esquema Protobuf, facilitando la compatibilidad entre servicios escritos en Go y Rust. El plugin inspecciona las anotaciones del archivo `.proto` y emite código Rust que rellena los campos solo si están sin establecer (unset).

## Datos clave
- **Funcionalidad principal**: Generación de `pub fn set_defaults(&mut self)` para tipos de mensaje.
- **Anotaciones soportadas**:
  - `(protoc.contrib.defaults.value)`: Establece valores para escalares, wrappers y enums.
  - `(protoc.contrib.defaults.oneof)`: Configura el brazo predeterminado de un oneof.
  - `(protoc.contrib.defaults.message)`: Inicializa o recursiva llama a `set_defaults` en mensajes anidados (`initialize`, `recurse`).
- **Tipos de valores**: Soporta escalares, duraciones (formato Prometheus), timestamps y tipos de mensaje.
- **Lógica de "unset"**: Depende del tipo de campo en `buffa`; por ejemplo, un `Option<T>` es unset si es `None`, mientras que un escalar es unset si tiene el valor cero.
- **Salida**: Genera archivos `<package>.defaults.rs` con bloques `impl`.

## Etiquetas
#rust #protobuf #buffer #default-values #buffa

Fuente: https://github.com/protoc-contrib/protoc-gen-rust-defaults
