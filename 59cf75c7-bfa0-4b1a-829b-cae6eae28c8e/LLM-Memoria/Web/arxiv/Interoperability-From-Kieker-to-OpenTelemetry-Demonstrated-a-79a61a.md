---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2411.07982v1"
tema: "OpenTelemetry Exporters"
tags: [web]
---
# Interoperability From Kieker to OpenTelemetry: Demonstrated as Export to ExplorViz

## Resumen
Este trabajo aborda la falta de interoperabilidad en los datos de trazado del marco Kieker, impidiendo su uso en herramientas de análisis estándar. Se propone una solución para exportar estos datos al formato OpenTelemetry mediante el framework TeeTime, demostrando la viabilidad del enfoque visualizando trazas en ExplorViz.

## Datos clave
- **Problema:** Los resultados de Kieker no son compatibles con la mayoría de las herramientas de análisis por falta de estandarización.
- **Solución propuesta:** Exportar datos de trazado distribuido de Kieker a OpenTelemetry.
- **Herramienta intermedia:** Se utiliza el framework "pipe-and-filter" llamado TeeTime, definiendo una etapa específica para procesar los datos de ejecución de Kieker desde diversos tipos de registros.
- **Demostración:** Visualización exitosa de trazas del sistema TeaStore utilizando la herramienta ExplorViz.

## Etiquetas
#Kieker #OpenTelemetry #TeeTime #ExplorViz #Observabilidad

Fuente: http://arxiv.org/abs/2411.07982v1
