---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://github.com/hashicorp/terraform-sentinel-policies"
tema: "Terraform Sentinel"
tags: [web]
---
# hashicorp/terraform-sentinel-policies

## Resumen
Este repositorio contiene políticas de ejemplo de tercera generación para Sentinel, diseñadas para integrarse con Terraform Cloud y Enterprise. El contenido está programado para migrarse próximamente al Registro de Terraform y soporta proveedores como AWS, Azure y GCP.

## Datos clave
- **Compatibilidad**: Requiere Terraform 0.12 o superior y Sentinel v2 imports (tfplan/v2, tfstate/v2, etc.).
- **Versión del Runtime**: Funciona con Terraform Cloud/Enterprise desde la versión 202011-1 (incluye Sentinel 0.16.0).
- **Módulos de funciones**: Utiliza módulos (`tfplan-functions`, `tfstate-functions`) para definir funciones parametrizadas sin repetir código en las políticas principales.
- **Características de reporte**: Todas las violaciones se reportan simultáneamente y muestran la dirección completa del recurso (ej: `module.<A>.<type>.<name>`).
- **Función recursiva**: `evaluate_attribute` permite evaluar atributos anidados profundamente en los recursos.
- **Estructura**: Incluye archivos de configuración de Policy Set para facilitar la integración vía VCS.

## Etiquetas
#Terraform #Sentinel #InfraestructuraComoCodigo #Seguridad #AWS #Azure

Fuente: https://github.com/hashicorp/terraform-sentinel-policies
