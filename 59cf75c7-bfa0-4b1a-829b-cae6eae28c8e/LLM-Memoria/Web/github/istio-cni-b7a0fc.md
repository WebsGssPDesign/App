---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/istio/cni"
tema: "Kubernetes Istio Sidecar"
tags: [web]
---
# istio/cni

## Resumen
Este repositorio describe el plugin CNI de Istio, diseñado para configurar las reglas iptables en los pods de Kubernetes y redirigir todo su tráfico hacia los sidecars proxy. Su implementación elimina la necesidad de contenedores iniciales con privilegios `NET_ADMIN`, simplificando la seguridad del clúster. Actualmente se ha fusionado al repositorio principal de Istio, aunque este texto sirve como referencia histórica.

## Datos clave
- **Función:** Configura iptables en el espacio de nombres (netns) del pod para redirigir tráfico IPv4 a `istio-proxy`.
- **Ventaja de seguridad:** Sustituye al contenedor inyectado `istio-init` que requería privilegios `NET_ADMIN`.
- **Estado:** Repositorio obsoleto; cambios principales deben hacerse en `istio.io/istio/cni`, salvo backports a ramas <= 1.6.
- **Comando de instalación:** Se utiliza Helm con variables como `--set istio_cni.enabled=true` y parámetros de imagen (`hub`, `tag`).
- **Parámetro clave:** `excludeNamespaces` (por defecto `[istio-system]`) para excluir ciertos pods del redireccionamiento.
- **Compatibilidad:** Funciona en entornos que usan CNI, con soporte verificado en GKE y Red Hat OpenShift.

## Etiquetas
#Istio #Kubernetes #CNI #SidecarProxy #Seguridad

Fuente: https://github.com/istio/cni
