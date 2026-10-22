---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Netdata"
tema: "OpenTelemetry Resource Detection"
tags: [web]
---
# Netdata

## Resumen
Netdata es una plataforma de observabilidad en tiempo abierto que permite monitorear infraestructuras y aplicaciones mediante agentes distribuidos. Su arquitectura procesa datos localmente para ofrecer dashboards automáticos y detección de anomalías basada en aprendizaje automático sin enviar grandes volúmenes de datos a un servidor central.

## Datos clave
- **Agentes:** Daemon que recopila métricas, ejecuta detección de anomalías y sirve el panel web.
- **Base de datos:** Motor `dbengine` personalizado con hasta 5 niveles de almacenamiento (por segundo, minuto o hora).
- **Eficiencia:** Alcanza aproximadamente 0,5 bytes por muestra en disco para datos de alta resolución.
- **ML y AI:** Detección no supervisada local con 18 modelos de k-means por métrica; integración vía Protocolo de Contexto del Modelo (MCP).
- **Recursos monitoreados:** CPU, memoria, red, contenedores, Kubernetes y servicios comunes en Linux, Windows, FreeBSD y macOS.
- **Financiación:** Inversión total de 31 millones de dólares hasta febrero de 2023.

## Etiquetas
#monitorización #observabilidad #Netdata #IA #Infraestructura

Fuente: https://en.wikipedia.org/wiki/Netdata
