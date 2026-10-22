---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://github.com/cloudposse/terraform-aws-tfstate-backend"
tema: "Terraform State Locking"
tags: [web]
---
# cloudposse/terraform-aws-tfstate-backend

## Resumen
Este módulo de Terraform provisiona un bucket S3 y una tabla DynamoDB para gestionar el archivo de estado `terraform.tfstate`. Su objetivo principal es asegurar la integridad del estado mediante encriptación, versionado y bloqueo contra modificaciones concurrentes.

## Datos clave
- **Recursos creados**: Bucket S3 (con encriptación y versioning) y tabla DynamoDB (para bloqueos).
- **Comandos de uso**: `terraform init`, `terraform apply -auto-approve` y `terraform init -force-copy`.
- **Archivos generados**: Crea automáticamente un archivo `backend.tf` para definir la configuración del backend.
- **Limitaciones**: No puede aplicar cambios a la función `mfa_delete`; requiere credenciales raíz con MFA.
- **Requisitos de permisos**: Los usuarios IAM deben tener derechos para crear buckets S3 y tablas DynamoDB.

## Etiquetas
#Terraform #AWS #InfraestructuraComoCodigo #Seguridad #S3

Fuente: https://github.com/cloudposse/terraform-aws-tfstate-backend
