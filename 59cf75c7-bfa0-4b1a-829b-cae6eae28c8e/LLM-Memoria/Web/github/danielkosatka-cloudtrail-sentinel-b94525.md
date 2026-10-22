---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/danielkosatka/cloudtrail-sentinel"
tema: "Terraform Sentinel Rules"
tags: [web]
---
# danielkosatka/cloudtrail-sentinel

## Resumen
CloudTrail Sentinel es una tubería de detección para registros AWS CloudTrail que normaliza eventos y los evalúa contra reglas de seguridad mapeadas a MITRE ATT&CK. El proyecto permite visualizar alertas en un panel local utilizando DuckDB, priorizando la ejecución offline sin necesidad de credenciales inmediatas. Actualmente se encuentra en fase 1 con seis reglas implementadas en YAML para identificar comportamientos maliciosos específicos.

## Datos clave
- **Componentes**: Ingesta (boto3/lectura local), Normalización a esquema ECS, Motor de detección (YAML), Almacenamiento DuckDB, Dashboard Streamlit.
- **Reglas implementadas**: Uso de cuenta raíz, Login sin MFA, CloudTrail deshabilitado, GuardDuty apagado, Política admin adjunta, Actividad en región no aprobada.
- **Reglas planificadas**: S3 expuesto públicamente, Fuerza bruta en consola.
- **Ventajas de diseño**: Uso de DuckDB por ser embebido y sin configuración; reglas como YAML para facilitar la edición ("detection-as-code"); logs de muestra incluidos para uso offline.

## Etiquetas
#AWS #CloudSecurity #MITREATT&CK #Docker #Python

Fuente: https://github.com/danielkosatka/cloudtrail-sentinel
