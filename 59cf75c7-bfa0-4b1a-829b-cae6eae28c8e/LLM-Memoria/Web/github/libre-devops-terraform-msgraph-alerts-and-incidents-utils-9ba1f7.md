---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/libre-devops/terraform-msgraph-alerts-and-incidents-utils"
tema: "Terraform Sentinel Custom Rules"
tags: [web]
---
# libre-devops/terraform-msgraph-alerts-and-incidents-utils

## Resumen
Este módulo de Terraform gestiona incidentes y alertas de Microsoft Defender a través de la API de Microsoft Graph, permitiendo su clasificación, actualización y gestión de reglas personalizadas. Aunque el núcleo está documentado, la creación directa de incidentes se considera experimental hasta que sea validada en un entorno con licencia E5.

## Datos clave
- **Funciones principales**: Actualizar (PATCH) incidentes y alertas, añadir comentarios (POST), gestionar reglas de detección personalizadas y crear alertas manuales.
- **Requisitos de licencia**: Se requiere una licencia de Microsoft Defender o E5 con consentimiento de administrador.
- **Permisos mínimos**: `SecurityIncident.ReadWrite.All`, `SecurityAlert.ReadWrite.All` y `CustomDetection.ReadWrite.All`.
- **Estado experimental**: La creación directa de incidentes (`incidents`) es inestable; no debe usarse en producción sin validación previa.
- **Versión de Terraform**: >= 1.9.0 y < 2.0.0.

## Etiquetas
#Terraform #MicrosoftGraph #DevOps #Security #Defender

Fuente: https://github.com/libre-devops/terraform-msgraph-alerts-and-incidents-utils
