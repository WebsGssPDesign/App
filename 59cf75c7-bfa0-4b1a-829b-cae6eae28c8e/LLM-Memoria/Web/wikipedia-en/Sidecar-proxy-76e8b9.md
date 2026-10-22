---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Sidecar_proxy"
tema: "Kubernetes Service Mesh Patterns"
tags: [web]
---
# Sidecar proxy

## Resumen
El patrón de diseño Sidecar Proxy coloca un servidor proxy junto a una aplicación para gestionar su comunicación de red sin modificar el código original. Este enfoque es fundamental en arquitecturas de microservicios y mallas de servicios para manejar tráfico, seguridad y observabilidad. Herramientas como Envoy implementan este patrón en plataformas como Kubernetes para orquestar interacciones entre servicios.

## Datos clave
- **Funciones principales**: Balanceo de carga, descubrimiento de servicios, cifrado de datos e inspección de tráfico (interceptación).
- **Ubicación típica**: Mismo host o mismo contenedor que la aplicación.
- **Implementaciones destacadas**: Envoy.
- **Plataformas asociadas**: Kubernetes, Service Mesh.
- **Ventaja clave**: Permite aplicar políticas y recopilar telemetría sin cambios en el código de la aplicación.

## Etiquetas
#Sidecar #Proxy #Microservicios #ServiceMesh #Envoy #Kubernetes

Fuente: https://en.wikipedia.org/wiki/Sidecar_proxy
