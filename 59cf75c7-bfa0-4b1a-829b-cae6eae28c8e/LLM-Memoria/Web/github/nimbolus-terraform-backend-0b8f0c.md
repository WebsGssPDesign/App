---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://github.com/nimbolus/terraform-backend"
tema: "Terraform State Locking"
tags: [web]
---
# nimbolus/terraform-backend

## Resumen
Este proyecto es un servidor de backend para Terraform que implementa la API HTTP oficial, permitiendo gestionar estados con módulos intercambiables para autenticación, almacenamiento y cifrado. Aunque está en desarrollo temprano, ofrece soporte nativo para autenticación básica y JWT, junto con múltiples opciones de almacenamiento como S3 o Postgres.

## Datos clave
- **Autenticación**: HTTP Basic Auth, JSON Web Tokens (JWT).
- **Almacenamiento**: Sistema de archivos local, Amazon S3, PostgreSQL.
- **Bloqueo de estado**: Mapa local, Redis, PostgreSQL.
- **Cifrado (KMS)**: Clave AES local, HashiCorp Vault Key/Value, HashiCorp Vault Transit.
- **Comando de ejecución**: `LOG_LEVEL=debug go run cmd/terraform-backend.go`.
- **Puerto por defecto**: 8080 (`LISTEN_ADDR`).
- **Configuración Terraform**: Uso del bloque `backend "http"` con dirección y credenciales.

## Etiquetas
#Terraform #DevOps #InfraestructuraComoCodigo #Backend

Fuente: https://github.com/nimbolus/terraform-backend
