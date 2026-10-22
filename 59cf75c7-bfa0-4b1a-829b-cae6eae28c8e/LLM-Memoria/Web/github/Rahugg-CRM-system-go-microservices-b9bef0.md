---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/Rahugg/CRM-system-go-microservices"
tema: "gRPC Deadlines Management"
tags: [web]
---
# Rahugg/CRM-system-go-microservices

## Resumen
Este proyecto es un sistema de gestión de relaciones con clientes (CRM) desarrollado en Go utilizando una arquitectura de microservicios. La aplicación permite gestionar tareas, roles de usuario, oportunidades de venta y feedback mediante servicios modulares como autenticación y núcleo CRM.

## Datos clave
- **Tecnologías:** Golang, Gin framework, gRPC, PostgreSQL, Redis, Kafka, Docker, Prometheus, Grafana.
- **Funcionalidades principales:** Asignación de plazos, gestión de contactos y roles, administración de ventas y feedback.
- **Características técnicas:** Concurrencia (Graceful Shutdown), caché en memoria con Redis, procesamiento de streaming con Kafka, autenticación JWT y documentación Swagger.
- **Estructura:** Separación clara en servicios (`auth`, `crm_core`) con lógica encapsulada en capas de controlador, servicio y repositorio.

## Etiquetas
#CRM #GoMicroservices #Golang #gRPC #PostgreSQL #Kafka

Fuente: https://github.com/Rahugg/CRM-system-go-microservices
