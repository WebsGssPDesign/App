---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2004.00372v1"
tema: "Kubernetes Istio"
tags: [web]
---
# Impact of etcd Deployment on Kubernetes, Istio, and Application Performance

## Resumen
Este estudio analiza cómo la configuración de almacenamiento de etcd afecta el rendimiento de Kubernetes y las aplicaciones que ejecuta, especialmente cuando se integra con Istio. Los resultados demuestran que el uso de disco RAM para etcd mejora significativamente la orquestación en comparación con el disco de red. El trabajo propone un marco experimental reproducible para evaluar rigurosamente estas interacciones complejas.

## Datos clave
- **Variables de prueba**: Ubicación de almacenamiento de etcd (disco de red vs. disco RAM).
- **Componentes afectados**: Kubernetes, Istio (malla de servicios), rendimiento de aplicaciones.
- **Hallazgo principal**: La elección del backend de almacenamiento de etcd tiene un impacto directo y grande en la capacidad de orquestación de Kubernetes.
- **Herramienta desarrollada**: Un marco experimental para garantizar pruebas repetibles y reproducibles, con el conjunto de datos disponible públicamente.

## Etiquetas
#Kubernetes #etcd #Istio #Rendimiento #Infraestructura

Fuente: http://arxiv.org/abs/2004.00372v1
