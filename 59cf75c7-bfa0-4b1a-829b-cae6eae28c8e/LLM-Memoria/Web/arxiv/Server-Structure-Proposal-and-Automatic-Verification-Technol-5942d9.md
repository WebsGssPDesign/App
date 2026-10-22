---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/1611.09569v2"
tema: "gRPC Server Streaming"
tags: [web]
---
# Server Structure Proposal and Automatic Verification Technology on IaaS Cloud of Plural Type Servers

## Resumen
Este artículo propone una metodología para diseñar estructuras de servidores óptimas en entornos IaaS que integran servidores baremetal, contenedores Docker y máquinas virtuales KVM. La solución se basa en mediciones cuantitativas de rendimiento y automatiza tanto la generación de plantillas de configuración como la verificación de requisitos de desempeño.

## Datos clave
- **Tipos de servidor analizados**: Baremetal, contenedores (Docker), Máquinas Virtuales (KVM/OpenStack).
- **Herramientas de medición**: OpenStack con variación del número de servidores virtuales.
- **Entrada del sistema**: Plantilla abstracta de OpenStack Heat y requisitos funcionales/performance.
- **Salida del sistema**: Plantilla concreta con especificaciones detalladas del servidor.
- **Funcionalidad principal**: Verificación automática de rendimiento en entornos provisionados según la plantilla generada.

## Etiquetas
#IaaS #CloudComputing #ServerOptimization #Docker #OpenStack

Fuente: http://arxiv.org/abs/1611.09569v2
