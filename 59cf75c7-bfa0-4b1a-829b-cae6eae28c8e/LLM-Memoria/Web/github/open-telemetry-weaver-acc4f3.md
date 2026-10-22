---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://github.com/open-telemetry/weaver"
tema: "OpenTelemetry Semantic Conventions"
tags: [web]
---
# open-telemetry/weaver

## Resumen
OpenTelemetry Weaver es una herramienta diseñada para facilitar el desarrollo, validación y despliegue de convenciones semánticas en telemetría. Su objetivo principal es implementar un enfoque de "observabilidad por diseño", tratando los señales de observabilidad como APIs públicas que requieren estándares de calidad rigurosos. Esto permite generar código consistentemente y detectar errores antes de llegar a producción.

## Datos clave
- **Conceptos**: Observabilidad por diseño, convenciones semánticas, telemetría esquematizada (métricas, trazas, logs).
- **Funcionalidades principales**: Validación de sintaxis y reglas personalizadas, resolución de dependencias del registro, comparación de versiones de esquemas.
- **Generación de código**: Producción de artefactos como código Go o documentación Markdown a partir de esquemas definidos.
- **Validación en vivo (Live-checking)**: Verificación de telemetría emitida contra un esquema específico durante la ejecución.
- **Instalación**: Disponible mediante binarios precompilados, Docker (`docker pull otel/weaver`) o compilación desde fuente con Rust/Cargo.
- **Criptografía**: Usa Rustls por defecto; soporta proveedores personalizados como AWS-LC, OpenSSL y SymCrypt mediante flags de compilación.

## Etiquetas
#OpenTelemetry #Observabilidad #DevOps #Instrumentación #SchemaValidation

Fuente: https://github.com/open-telemetry/weaver
