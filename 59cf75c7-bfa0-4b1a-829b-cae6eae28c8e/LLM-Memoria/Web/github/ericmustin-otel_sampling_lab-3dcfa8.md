---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/ericmustin/otel_sampling_lab"
tema: "OpenTelemetry Sampling Strategies"
tags: [web]
---
# ericmustin/otel_sampling_lab

## Resumen
Este laboratorio compara cinco técnicas de muestreo y estrategias de reducción de volumen en OpenTelemetry utilizando tráfico vivo idéntico. El proyecto demuestra cómo diferentes procesadores, desde muestreo probabilístico hasta detección de anomalías con IA, afectan la retención de errores y el tamaño de los datos, visualizándose tanto en Grafana como en Elasticsearch.

## Datos clave
- **Técnicas evaluadas:** Muestreo completo (base), cola (tail sampling), probabilístico, poda de spans (span pruning) y prioridad por anomalías ML (isolation forest).
- **Componentes OCB:** `tail_sampling`, `groupbytrace`, `spanpruning`, `isolationforest`.
- **Herramientas:** OpenTelemetry Collector (OCB), Grafana, Elasticsearch con PromQL.
- **Comandos principales:** `make up` (iniciar demo y tráfico), `make break` (simular fallos para probar detección de anomalías), `make dashboards` (visualización).
- **Requisitos:** Docker, Docker Compose v2, ~3 GB de disco.

## Etiquetas
#OpenTelemetry #Muestreo #Observabilidad #Elasticsearch #Grafana

Fuente: https://github.com/ericmustin/otel_sampling_lab
