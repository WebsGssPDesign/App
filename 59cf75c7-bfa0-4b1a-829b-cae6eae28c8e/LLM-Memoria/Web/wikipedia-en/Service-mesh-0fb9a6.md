---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Service_mesh"
tema: "Kubernetes Service Mesh"
tags: [web]
---
# Service mesh

## Resumen
Una *service mesh* es una capa de infraestructura dedicada que facilita la comunicación entre servicios mediante el uso de proxies. Esta arquitectura separa las funciones en un plano de datos para interceptar llamadas y un plano de control que coordina el comportamiento y ofrece herramientas de observabilidad y seguridad. Diversos productos implementan esta solución, siendo común el uso del proxy Envoy en el nivel de datos.

## Datos clave
- **Componentes**: Plano de datos (data plane) con proxies y plano de control (control plane).
- **Funciones principales**: Observabilidad, conexiones seguras, automatización de reintentos y backoff.
- **Software destacado**: Istio, Cilium, Linkerd, Consul, AWS App Mesh, Kuma, Traefik Mesh, Greymatter.io.
- **Proxy común**: Envoy (utilizado en la mayoría de las implementaciones).

## Etiquetas
#service_mesh #microservicios #arquitectura_de_reds #istio #envoy

Fuente: https://en.wikipedia.org/wiki/Service_mesh
