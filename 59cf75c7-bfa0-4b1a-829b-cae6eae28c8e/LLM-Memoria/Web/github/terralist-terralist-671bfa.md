---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/terralist/terralist"
tema: "Terraform Provider Registry"
tags: [web]
---
# terralist/terralist

## Resumen
Terralist es un registro privado y autoalojado para módulos y proveedores de Terraform y OpenTofu que implementa los protocolos oficiales de HashiCorp. Ofrece una interfaz web, control de acceso basado en roles (RBAC) y soporte para múltiples proveedores de almacenamiento y autenticación OAuth.

## Datos clave
- **Funcionalidad principal**: Registro privado para módulos y proveedores con gestión vía REST API y dashboard web.
- **Autenticación**: Soporte para GitHub, GitLab, BitBucket y cualquier proveedor OIDC-compatible.
- **Control de acceso (RBAC)**: Roles integrados (`admin`, `readonly`, `anonymous`) y políticas personalizadas usando Casbin.
- **Almacenamiento**: AWS S3, Azure Blob, Google Cloud Storage, sistema de archivos local o modo proxy.
- **Monitoreo**: Métricas Prometheus para uploads, descargas, uso de claves API y latencia HTTP.
- **Instalación**: Binario único compilado en Go sin dependencias externas; puerto por defecto 5758.

## Etiquetas
#Terraform #OpenTofu #DevOps #InfraestructuraComoCodigo #RegistroPrivado

Fuente: https://github.com/terralist/terralist
