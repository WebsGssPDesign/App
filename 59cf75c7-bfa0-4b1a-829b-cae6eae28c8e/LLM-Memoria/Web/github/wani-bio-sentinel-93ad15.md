---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/wani-bio/sentinel"
tema: "Terraform Sentinel Custom Rules"
tags: [web]
---
# wani-bio/sentinel

## Resumen
Sentinel AI es una plataforma de inteligencia artificial basada en la nube, diseñada para identificar y gestionar el riesgo de impago en hipotecas mediante un enfoque serverless. El sistema calcula puntuaciones de riesgo, protege los datos personales de los prestatarios y utiliza modelos de IA generativa para crear estrategias personalizadas de intervención financiera.

## Datos clave
- **Arquitectura:** AWS Serverless (Lambda, DynamoDB, API Gateway).
- **Motor de IA:** Amazon Bedrock con Claude 3 Haiku para generar estrategias de refinanciación.
- **Seguridad:** Encriptación por defecto en DynamoDB y gestión de secretos vía AWS Secrets Manager.
- **Infraestructura como Código (IaC):** Terraform modularizado.
- **CI/CD:** GitHub Actions para pruebas, escaneo de seguridad y despliegue automático.
- **Frontend:** React + Vite con diseño responsivo.
- **Pasos de despliegue:** Inicializar Terraform (`terraform init`), planificar (`terraform plan`) y aplicar cambios (`terraform apply`).

## Etiquetas
#AWS #Serverless #InteligenciaArtificial #Finanzas #DevOps

Fuente: https://github.com/wani-bio/sentinel
