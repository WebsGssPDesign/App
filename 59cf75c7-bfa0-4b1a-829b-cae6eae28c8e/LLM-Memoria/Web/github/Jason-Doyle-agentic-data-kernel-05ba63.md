---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/Jason-Doyle/agentic-data-kernel"
tema: "Temporal External Workflows"
tags: [web]
---
# Jason-Doyle/agentic-data-kernel

## Resumen
El Agentic Data Kernel es una capa de persistencia diseñada específicamente para aplicaciones impulsadas por agentes, gestionando conocimiento temporal, flujos de trabajo duraderos y linaje causal sobre SQLite o PostgreSQL. Su objetivo principal es estandarizar patrones complejos de auditoría y recuperación que los agentes suelen tener que reinventar mediante código personalizado en bases de datos convencionales.

## Datos clave
- **Soporte:** Funciona sobre SQLite (desarrollo local) y PostgreSQL (producción).
- **Escenario demostrativo:** Reduce la tasa de error de un servicio SRE del 42% al 3% mediante reconciliación durable y rollback autorizado.
- **Eficiencia comparativa:** En pruebas deterministas, el kernel requiere 0 líneas de código propias para la lógica de negocio frente a 317 en una aplicación convencional, aunque utiliza más tablas (18 vs 8) y mayor espacio en disco.
- **Rastreo causal (`explain`):** Permite trazar explícitamente el linaje entre decisiones, políticas, hipótesis y efectos externos, incluyendo intentos de entrega y resolución de conflictos.
- **Licencia:** Apache-2.0.

## Etiquetas
#agentic-data-kernel #persistencia-de-agentes #linaje-causal #sre #postgresql #sqlite

Fuente: https://github.com/Jason-Doyle/agentic-data-kernel
