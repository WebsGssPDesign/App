---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2608.26573v1"
tema: "Kubernetes Gateway API"
tags: [web]
---
# Optimizing API Gateway Placement in Multi-Cloud Kubernetes

## Resumen
Este trabajo aborda el desafío de colocar API Gateways en clústeres Kubernetes distribuidos en múltiples nubes, equilibrando costos, recursos y latencia. Se propone una formulación matemática que determina la activación de clusters, el número de réplicas y la distribución del tráfico bajo restricciones de latencia.

## Datos clave
- **Problema:** Capacitated Facility Location Problem (CFLP).
- **Métodos:** Programación entera mixta lineal (MILP) y un algoritmo heurístico constructivo tipo "greedy".
- **Rendimiento Heurística:** Brecha de optimalidad entre 3.2% y 4.7%, con aceleración de 660x a 3,490x respecto al MILP.
- **Ahorro Costos:** La solución óptima del MILP reduce el costo mensual en un 24.2% frente a una réplica completa; elegir solo el cluster más barato ahorra un 24.8% pero incumple requisitos de latencia para 3 regiones.

## Etiquetas
#Kubernetes #MultiCloud #APIGateway #Optimización #Latencia

Fuente: http://arxiv.org/abs/2608.26573v1
