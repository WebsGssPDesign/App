---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2312.15350v1"
tema: "Helm Charts Management"
tags: [web]
---
# Why Not Mitigate Vulnerabilities in Helm Charts?

## Resumen
Este estudio analiza la prevalencia de vulnerabilidades en 11.035 diagramas Helm (Charts), revelando que la complejidad del Chart se correlaciona directamente con el número de fallos de seguridad. Aunque existen estrategias de mitigación identificadas, la falta de incentivos para los mantenedores y las limitaciones de la automatización dificultan su implementación efectiva en este ecosistema.

## Datos clave
- **Muestra**: 11.035 Helm Charts afectados por 10.982 vulnerabilidades corregibles.
- **Gravedad**: Las vulnerabilidades tienen una mediana de alta severidad y son fácilmente explotables.
- **Hallazgo principal**: Los Charts oficiales no contienen menos vulnerabilidades que los no oficiales.
- **Estrategias identificadas**: 11 estrategias de mitigación agrupadas en tres categorías.
- **Limitaciones**: La automatización tiene baja adopción debido a falsos positivos y la complejidad manual para rastrear el impacto.
- **Recomendación final**: Se propone un modelo de responsabilidad compartida para aumentar la seguridad.

## Etiquetas
#seguridad #kubernetes #helmcharts #vulnerabilidades #devops

Fuente: http://arxiv.org/abs/2312.15350v1
