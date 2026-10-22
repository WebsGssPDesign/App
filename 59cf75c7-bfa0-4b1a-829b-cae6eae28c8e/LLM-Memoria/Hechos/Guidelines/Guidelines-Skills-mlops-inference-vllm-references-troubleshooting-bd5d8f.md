---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/mlops/inference/vllm/references/troubleshooting.md"
tags: [hecho]
---
# troubleshooting.md

## Resumen
Esta guía técnica documenta procedimientos para diagnosticar y resolver errores comunes en la implementación de servidores de modelos con vLLM, como fallos por falta de memoria (OOM), problemas de rendimiento y errores de carga. Su objetivo es proporcionar soluciones inmediatas mediante ajustes de configuración específicos del servidor y verificación de dependencias.

## Datos clave
- **Comandos principales**: `vllm serve MODEL` con parámetros críticos como `--gpu-memory-utilization`, `--max-model-len`, `--quantization awq` y `--tensor-parallel-size`.
- **Herramientas de diagnóstico**: `nvidia-smi` para monitoreo de GPU, `curl http://localhost:8000/health` para verificar el estado del servidor y `lsof -i :8000` para revisar puertos.
- **Soluciones a OOM**: Reducir la utilización de memoria GPU, disminuir la longitud máxima del modelo o habilitar paralelismo tensorial.
- **Manejo de errores de carga**: Uso de `huggingface-cli login` para modelos privados y `--trust-remote-code` para código personalizado; instalación manual de `flash-attn`.
- **Optimizaciones de rendimiento**: Activación de `--enable-prefix-caching`, `--enable-chunked-prefill` y ajuste de `--max-num-seqs` según la carga.

## Etiquetas
#vllm #MLOps #Troubleshooting #GPU #Inference

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\mlops\inference\vllm\references\troubleshooting.md`
