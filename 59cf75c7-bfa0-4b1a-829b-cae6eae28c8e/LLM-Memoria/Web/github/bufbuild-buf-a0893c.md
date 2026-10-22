---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/bufbuild/buf"
tema: "gRPC Protocols"
tags: [web]
---
# bufbuild/buf

## Resumen
Buf es una herramienta moderna para gestionar Protocol Buffers que reemplaza el uso tradicional de `protoc`, ofreciendo un entorno de trabajo más robusto y seguro. Proporciona capacidades avanzadas como detección de cambios rotos, gestión de dependencias y generación de código centralizada sin necesidad de scripts complejos.

## Datos clave
- **Comandos principales**: `buf build` (compilación), `buf lint` (verificación de estilo), `buf breaking` (detección de incompatibilidades), `buf generate` (generación de código).
- **Configuración**: Se define en archivos `buf.yaml` y `buf.gen.yaml`.
- **Funcionalidad clave**: Detección de cambios rotos (`FILE`, `SOURCE`, `WIRE`) antes de fusionar código.
- **Gestión de dependencias**: Uso de módulos declarados y archivos bloqueantes (`buf.lock`).
- **Generación de código**: Soporte para plugins remotos (hosteados en BSR) o locales, eliminando la necesidad de instalar binarios en cada máquina.

## Etiquetas
#ProtocolBuffers #Buf #DevTools #CodeGeneration

Fuente: https://github.com/bufbuild/buf
