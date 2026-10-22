---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/kedacore/http-add-on"
tema: "Kubernetes KEDA Autoscaling"
tags: [web]
---
# kedacore/http-add-on

## Resumen
Este proyecto es un complemento para KEDA que permite escalar automáticamente servidores HTTP en Kubernetes basándose en el tráfico entrante, incluyendo la capacidad de reducir las réplicas a cero. Aunque KEDA no incluye este escalador nativo debido a la complejidad de definir eventos HTTP y medir peticiones sin integrar controladores de entrada, esta solución ofrece componentes aislados para facilitar dicha tarea. Actualmente se encuentra en estado beta con una versión 1.0 planeada.

## Datos clave
- **Funcionalidad principal**: Escalado automático de cargas de trabajo HTTP hacia arriba y abajo según el tráfico recibido.
- **Estado del proyecto**: Beta (mantenido activamente por la comunidad KEDA).
- **Integración**: Requiere componentes adicionales para medir peticiones, a diferencia de los escaladores nativos que usan APIs directas.
- **Alternativa comercial**: Se menciona Kedify HTTP Scaler como opción con soporte comercial.
- **Certificaciones**: Proyecto graduado por la Cloud Native Computing Foundation (CNCF) y sigue las mejores prácticas OpenSSF.

## Etiquetas
#Kubernetes #Autoescalado #HTTP #KEDA #CloudNative

Fuente: https://github.com/kedacore/http-add-on
