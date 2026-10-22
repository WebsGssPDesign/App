---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/mlops/inference/vllm/references/server-deployment.md"
tags: [hecho]
---
# server-deployment.md

## Resumen
Este documento detalla los patrones de despliegue para servidores vLLM, cubriendo configuraciones desde contenedores Docker hasta orquestación en Kubernetes y distribución multi-nodo. Su objetivo es guiar la implementación robusta de modelos de lenguaje grandes (LLMs) en entornos de producción, optimizando el rendimiento según las necesidades específicas de latencia o throughput.

## Datos clave
- **Contenedores**: Uso de `nvidia/cuda:12.1.0-devel` y Docker Compose con métricas expuestas en puerto 9090.
- **Kubernetes**: Manifests para Deployment (réplicas, probes) y Service tipo LoadBalancer.
- **Balanceo**: Configuración Nginx con `least_conn` y timeouts ajustados para inferencia larga.
- **Distribución**: Ejecución multi-nodo usando variables de entorno (`MASTER_ADDR`, `RANK`) y paralelismo tensorial/pipeline.
- **Optimización**: Parámetros como `--gpu-memory-utilization`, `--enable-prefix-caching` y cuantización AWQ para GPUs limitadas.
- **Monitoreo**: Endpoints `/health`, scraping de Prometheus en 9090 y métricas clave (TTFT, GPU cache) en Grafana.

## Etiquetas
#vllm #kubernetes #docker #llm-inference #devops

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\mlops\inference\vllm\references\server-deployment.md`
