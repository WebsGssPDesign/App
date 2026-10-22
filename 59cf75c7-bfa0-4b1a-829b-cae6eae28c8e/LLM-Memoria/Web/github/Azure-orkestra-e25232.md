---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://github.com/Azure/orkestra"
tema: "Helm Charts Management"
tags: [web]
---
# Azure/orkestra

## Resumen
Orkestra es una plataforma nativa de la nube diseñada para la orquestación de liberaciones y el gestión del ciclo de vida (LCM) de grupos relacionados de Helm releases y sus subcharts. Funciona construyendo sobre tecnologías CNCF como Argo Workflows y Flux Helm Controller, permitiendo definir flujos de trabajo complejos basados en grafos de dependencia (DAG).

## Datos clave
- **Propósito:** Orquestación fina de helm charts interdependientes y sus dependencias.
- **Tecnologías base:** Helm, Argo Workflows, Flux Helm Controller, Chartmuseum, Keptn.
- **Unidad de despliegue:** Definición de flujo de trabajo con tipo de recurso personalizado que modela relaciones entre releases.
- **Estructura:** El `ApplicationGroup` agrupa releases mediante secuencias o subcharts ejecutados como releases propias dentro de pasos del workflow.
- **Control:** Permite definir condiciones evaluadas al inicio; si fallan, el workflow completo se aborta.
- **Visualización:** Dashboards integrados para Argo Workflows y Keptn (éxito/fallo).

## Etiquetas
#DevOps #Helm #Kubernetes #Orkestra #ArgoWorkflows #FluxCD #CloudNative

Fuente: https://github.com/Azure/orkestra
