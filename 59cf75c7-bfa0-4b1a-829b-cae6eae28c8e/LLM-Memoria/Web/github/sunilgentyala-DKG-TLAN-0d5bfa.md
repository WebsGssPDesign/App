---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/sunilgentyala/DKG-TLAN"
tema: "Temporal Cloud Native Observability"
tags: [web]
---
# sunilgentyala/DKG-TLAN

## Resumen
DKG-TLAN es un marco híbrido diseñado para la detección de anomalías y localización de causas raíz en entornos de microservicios cloud-native. Integra un Grafo de Conocimiento Dinámico (DKG) con una Red de Atención Lógica Temporal (TLAN) para analizar trazas, logs y metadatos de Kubernetes.

## Datos clave
- **Componentes principales**: Dynamic Knowledge Graph (DKG), Temporal Logical Attention Network (TLAN).
- **Mecanismos técnicos**: Matriz de adyacencia adaptativa y dispersa; extracción de características multi-escala con kernels Conv1D {3, 5, 7}; fusión dual BiLSTM + GAT.
- **Fusión cruzada**: Puerta aprendible que equilibra evidencia temporal y estructural para identificar cuellos de botella físicos compartidos.
- **Evaluación sintética**: En un benchmark reproducible con topología de 13 nodos, DKG-TLAN alcanzó una precisión macro-F1 del 92.5% y ROC-AUC del 99.7%.
- **Instalación**: `pip install -e ".[dev]"`.
- **Benchmarks**: `benchmarks/synthetic_eval.py` para clasificación de fallos (pod failure, network delay, memory stress).

## Etiquetas
#cloud-native #anomaly-detection #knowledge-graphs #microservices #deep-learning

Fuente: https://github.com/sunilgentyala/DKG-TLAN
