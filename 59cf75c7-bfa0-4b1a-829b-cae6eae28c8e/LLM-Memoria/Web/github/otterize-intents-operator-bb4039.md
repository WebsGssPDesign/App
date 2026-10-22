---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/otterize/intents-operator"
tema: "Kubernetes NetworkPolicies"
tags: [web]
---
# otterize/intents-operator

## Resumen
El operador de intenciones de Otterize automatiza la gestión de políticas de red y permisos en Kubernetes para AWS, GCP y Azure mediante un formato declarativo basado en recursos personalizados. Este sistema permite definir las intenciones de acceso de los clientes a servidores específicos, generando automáticamente las reglas necesarias sin intervención manual continua.

## Datos clave
- **Recurso personalizado**: `ClientIntents` (especie `k8s.otterize.com/v1alpha3`) para declarar accesos entre servicios.
- **Políticas de red**: Crea políticas `Ingress` etiquetando pods con `can-access-<target>` y `has-identity=<target>`.
- **Integraciones cloud**: Gestiona roles IAM en AWS, identidades gestionadas en Azure y cuentas de servicio en Google Cloud junto al operador de credenciales.
- **Kafka**: Genera automáticamente ACLs y mTLS para control de acceso.
- **Ejemplo YAML**: Uso de `apiVersion: k8s.otterize.com/v1alpha3` con especificaciones de servicios y llamadas (tipo `kafka`, `aws`, `azure`).

## Etiquetas
#Kubernetes #SeguridadDeRed #IAMCloud #AutomatizaciónDevOps #Otterize

Fuente: https://github.com/otterize/intents-operator
