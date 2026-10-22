---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/adohe-zz/kube2haproxy"
tema: "Kubernetes Service Discovery"
tags: [web]
---
# adohe-zz/kube2haproxy

## Resumen
kube2haproxy es un proceso daemon escrito en Golang que automatiza la configuración de HAProxy y Keepalived para servicios desplegados en Kubernetes, asegurando alta disponibilidad. El sistema monitorea cambios en los recursos del clúster y actualiza las configuraciones de forma controlada sin dependencias adicionales.

## Datos clave
- **Funcionalidad principal**: Descubrimiento automático de servicios y configuración dinámica de HAProxy (con soporte para failover IP) y Keepalived.
- **Integración**: Se conecta con Prometheus para el monitoreo de métricas.
- **Lenguaje**: Desarrollado en Golang.
- **Mecanismo**: Observa `kube-apiserver` por cambios en servicios y endpoints, aplicando recargas limitadas por tasa (rate limited).
- **Comandos de construcción**: `git clone`, `godep go build -o kube-haproxy main.go`.
- **Parámetros importantes**: `--haproxy-template-file`, `--keepalived-template-file` para personalizar configuraciones; `--kubeconfig` para autenticación.

## Etiquetas
#Kubernetes #HAProxy #Keepalived #AltaDisponibilidad #DevOps

Fuente: https://github.com/adohe-zz/kube2haproxy
