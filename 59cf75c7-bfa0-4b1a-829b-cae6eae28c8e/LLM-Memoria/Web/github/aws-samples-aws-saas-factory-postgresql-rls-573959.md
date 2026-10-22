---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/aws-samples/aws-saas-factory-postgresql-rls"
tema: "PostgreSQL Row Level Security"
tags: [web]
---
# aws-samples/aws-saas-factory-postgresql-rls

## Resumen
Este proyecto de la AWS SaaS Factory demuestra cómo implementar aislamiento de datos multitenant utilizando políticas de seguridad a nivel de fila (RLS) en PostgreSQL. A través de una plantilla CloudFormation, se orquesta un entorno completo que incluye VPC, RDS, contenedores ECS y aplicaciones Spring Boot para gestionar usuarios por inquilino sin acceso cruzado no autorizado.

## Datos clave
- **Tecnología**: PostgreSQL Row Level Security (RLS), Spring Boot, Docker, AWS Fargate.
- **Infraestructura**: VPC con subnets públicas/privas en 2 zonas, NAT Gateway, EC2 bastion host.
- **Servicios gestionados**: RDS PostgreSQL, ECR, ECS, CodeBuild, CodePipeline, CloudWatch Logs.
- **Seguridad**: Contraseñas almacenadas en AWS Systems Manager, grupos de seguridad restringidos.
- **Flujo**: El usuario final inicia sesión como un inquilino específico; las políticas RLS bloquean el acceso a datos de otros inquilinos automáticamente.

## Etiquetas
#AWS #PostgreSQL #RLS #MultiTenant #DevOps #CloudFormation

Fuente: https://github.com/aws-samples/aws-saas-factory-postgresql-rls
