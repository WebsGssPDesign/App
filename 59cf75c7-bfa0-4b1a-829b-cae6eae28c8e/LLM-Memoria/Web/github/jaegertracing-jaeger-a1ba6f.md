---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://github.com/jaegertracing/jaeger"
tema: "Tracing OpenTelemetry"
tags: [web]
---
# jaegertracing/jaeger

## Resumen
Jaeger es una plataforma de trazado distribuido creada por Uber y alojada bajo la Cloud Native Computing Foundation (CNCF). La versión 2.0 ya está disponible e incluye un comando rápido para ejecutar el sistema completo con Docker en segundos, facilitando tanto pruebas locales como despliegues de producción mediante componentes modulares.

## Datos clave
- **Comandos**: `docker run --rm --name jaeger -p 16686:16686 ... jaegertracing/jaeger:latest` para iniciar el modo all-in-one.
- **Puertos**: UI en 16686, OTLP gRPC en 4317 y HTTP en 4318.
- **Acceso**: Interfaz web disponible en `http://localhost:16686`.
- **Política de compatibilidad**: Las opciones configuradas obsoletas tienen un periodo de gracia de al menos 3 meses o dos saltos de versión menor antes de su eliminación definitiva.
- **Soporte Go**: Desde la liberación de una nueva versión menor `N`, el soporte para `N-1` se elimina y `N` se convierte en la versión mínima requerida.

## Etiquetas
#Jaeger #TrazadoDistribuido #CNCF #OpenTelemetry #DevOps

Fuente: https://github.com/jaegertracing/jaeger
