---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/babarot/stein"
tema: "Terraform Sentinel Rules"
tags: [web]
---
# babarot/stein

## Resumen
Stein es una herramienta de linting diseñada para archivos de configuración, permitiendo definir conjuntos de reglas personalizadas basados en el concepto de "Policy as Code". El proyecto soporta actualmente los formatos JSON, YAML y HCL, inspirándose fuertemente en HashiCorp Sentinel. Aunque es útil para validar infraestructura como código, se recomienda usar frameworks alternativos como OPA a partir de febrero de 2021, salvo que el usuario tenga preferencia específica por HCL.

## Datos clave
- **Soporte de formatos:** JSON, YAML y HCL.
- **Concepto central:** Policy as Code (definir políticas como código).
- **Inspiración principal:** HashiCorp Sentinel.
- **Contexto de uso:** Validar configuraciones de infraestructura (ej. Kubernetes) antes del despliegue.
- **Recomendación actual:** Usar `opa/conftest` en lugar de Stein para la mayoría de casos, excepto para entusiastas de HCL.

## Etiquetas
#herramientas-devops #linting #policy-as-code #configuracion #infrastructure

Fuente: https://github.com/babarot/stein
