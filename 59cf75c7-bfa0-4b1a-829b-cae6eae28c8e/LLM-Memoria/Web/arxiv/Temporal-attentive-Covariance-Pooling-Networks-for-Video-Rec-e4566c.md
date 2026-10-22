---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2110.14381v3"
tema: "PostgreSQL Connection Pooling"
tags: [web]
---
# Temporal-attentive Covariance Pooling Networks for Video Recognition

## Resumen
Este artículo propone las Redes de Acoplamiento Covariante Atentas Temporales (TCP), un módulo diseñado para mejorar el reconocimiento de videos al superar las limitaciones del agrupamiento promedio global tradicional. La arquitectura introduce atención temporal para calibrar características espacio-temporales antes de realizar un acoplamiento covariante que capture correlaciones intra e inter-marco, mejorando la representación de dinámicas complejas.

## Datos clave
- **TCP (Temporal-attentive Covariance Pooling):** Módulo insertado al final de arquitecturas profundas para generar representaciones potentes.
- **Módulo de atención temporal:** Calibra adaptativamente las características espacio-temporales antes del acoplamiento.
- **Acoplamiento covariante temporal:** Caracteriza correlaciones dentro y entre fotogramas de las características calibradas.
- **Normalización de potencia matricial rápida:** Explota la geometría de las representaciones covariantes.
- **TCPNet:** Arquitectura resultante al integrar TCP, model-agnóstica y flexible para diversos sistemas de video.
- **Benchmarks evaluados:** Kinetics, Something-Something V1 y Charades.

## Etiquetas
#video-recognition #deep-learning #covariance-pooling #temporal-attention #computer-vision

Fuente: http://arxiv.org/abs/2110.14381v3
