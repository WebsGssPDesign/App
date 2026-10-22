---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/pgdogdev/pgdog"
tema: "PostgreSQL Connection Pooling"
tags: [web]
---
# pgdogdev/pgdog

## Resumen
PgDog es un proxy de código abierto escrito en Rust diseñado para escalar PostgreSQL mediante agrupación de conexiones, balanceo de carga y particionamiento de bases de datos. La herramienta permite gestionar miles de conexiones en hardware estándar y ofrece una arquitectura que soporta tanto lectura como escritura a través de un único punto de conexión.

## Datos clave
- **Tecnología**: Escrito en Rust para alto rendimiento y seguridad.
- **Funcionalidades principales**: Pooling de transacciones, balanceo de carga (round robin, aleatorio, menor actividad) y sharding automático.
- **Instalación rápida**: Soporta Kubernetes (Helm), AWS (EKS/ECS con Terraform) y Docker Compose.
- **Configuración**: Requiere dos archivos (`pgdog.toml` para hosts/sharding y `users.toml` para credenciales).
- **Balanceo inteligente**: Utiliza un parser nativo de PostgreSQL para distinguir entre consultas de lectura (enviadas a réplicas) y escritura (enviadas al primario), permitiendo un único endpoint.
- **Salud del sistema**: Incluye checks de salud en tiempo real que eliminan nodos fallidos automáticamente.

## Etiquetas
#PostgreSQL #BasesDeDatos #DevOps #Rust #Escalabilidad

Fuente: https://github.com/pgdogdev/pgdog
