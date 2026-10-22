---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/hashicorp/policy-library-pcidss-policy-set-for-aws-terraform"
tema: "Terraform Sentinel Compliance"
tags: [web]
---
# hashicorp/policy-library-pcidss-policy-set-for-aws-terraform

## Resumen
Este repositorio ofrece una biblioteca de políticas Sentinel preescritas listas para usar, diseñadas específicamente para ayudar a las organizaciones que manejan datos de tarjetas de pago a cumplir con los estándares PCI DSS en entornos AWS. HashiCorp proporciona estas herramientas para agilizar la gestión de cumplimiento y seguridad sin necesidad de desarrollarlas desde cero, integrándose directamente con HCP Terraform y Terraform Enterprise.

## Datos clave
- **Propósito**: Cumplimiento continuo de controles PCI DSS en infraestructura AWS.
- **Plataformas compatibles**: HCP Terraform y Terraform Enterprise (TFE).
- **Requisitos mínimos**: Versión v202312-1 o superior de HCP/TFE y Sentinel 0.26.x+.
- **Niveles de aplicación**: Por defecto `advisory`, modificable a `soft-mandatory` o `hard-mandatory`.
- **Métodos de implementación**: Uso del Terraform Registry o clonación directa del repositorio público GitHub.
- **Personalización**: Se recomienda editar el archivo `sentinel.hcl` para ajustar políticas específicas antes de aplicar la configuración.

## Etiquetas
#PCI-DSS #Terraform #Sentinel #AWS #Compliance #HashiCorp

Fuente: https://github.com/hashicorp/policy-library-pcidss-policy-set-for-aws-terraform
