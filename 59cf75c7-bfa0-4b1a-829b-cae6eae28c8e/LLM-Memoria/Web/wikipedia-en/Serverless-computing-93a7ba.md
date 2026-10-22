---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Serverless_computing"
tema: "OpenTelemetry Resource Detection"
tags: [web]
---
# Serverless computing

## Resumen
El cómputo serverless es un modelo en la nube donde los proveedores gestionan la infraestructura, permitiendo a los desarrolladores enfocarse únicamente en el código. Aunque elimina la gestión de servidores, traslada parte de la complejidad operativa al equipo de desarrollo y requiere una mentalidad específica para abordar desafíos como la observabilidad y la seguridad.

## Datos clave
- **Definición**: Modelo donde se usa capacidad de nube sin aprovisionar ni gestionar recursos (ISO/IEC 22123-2).
- **Componentes**: Incluye FaaS (Function as a Service), servicios gestionados, herramientas y marcos de trabajo.
- **Desafíos principales**:
    - *Observabilidad*: Dificultad para rastrear flujos en entornos distribuidos; soluciones como AWS X-Ray o OpenTelemetry ayudan.
    - *Seguridad*: Vulnerable a ataques tradicionales y específicos (ej. "denial of wallet").
    - *Vendor lock-in*: Alta dependencia del proveedor debido a la abstracción, dificultando la migración.
- **Anti-patrón**: "Grain of sand" (componentes excesivamente pequeños) y "Lambda pinball" (invocaciones en cadena fragmentadas).
- **HPC**: Puede no ser ideal para cargas de trabajo que requieren recursos sostenidos, pero escala bien para tareas paralelizables.

## Etiquetas
#cómputo_serverless #cloud_computing #FaaS #DevOps #seguridad_nube

Fuente: https://en.wikipedia.org/wiki/Serverless_computing
