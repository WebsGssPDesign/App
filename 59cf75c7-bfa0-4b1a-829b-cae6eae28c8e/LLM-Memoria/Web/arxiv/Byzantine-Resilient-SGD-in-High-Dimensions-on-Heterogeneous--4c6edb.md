---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2005.07866v1"
tema: "PostgreSQL Change Data Capture"
tags: [web]
---
# Byzantine-Resilient SGD in High Dimensions on Heterogeneous Data

## Resumen
El artículo estudia la descente de gradiente estocástico (SGD) distribuida en arquitecturas maestro-trabajador bajo ataques bizantinos y datos heterogéneos, sin asumir probabilidades sobre la generación de datos. Propone un algoritmo que utiliza un procedimiento de filtrado de outliers para eliminar gradientes corruptos, derivando nuevos resultados de concentración matricial aplicables a este entorno específico.

## Datos clave
- **Tolerancia al fallo**: El algoritmo soporta hasta $\frac{1}{4}$ (25%) de trabajadores bizantinos.
- **Convergencia**: Logra parámetros óptimos aproximados exponencialmente rápido en funciones fuertemente convexas y puntos estacionarios con velocidad lineal en casos no convexos, igualando las tasas de SGD estándar libre de ataques.
- **Supuestos**: Se requiere varianza acotada en gradientes estocásticos locales y una condición determinista sobre la disimilitud de los gradientes entre datasets.
- **Optimización de comunicación**: Una variante con compresión de gradientes envía solo $k$ coordenadas aleatorias, logrando un ahorro de $\frac{d}{k}$ en bits de comunicación y complejidad de decodificación sin afectar la tasa de convergencia ni el error de aproximación.
- **Modelo**: Heterogeneidad de datos donde cada trabajador posee un dataset local diferente, sin suposiciones probabilísticas sobre su generación.

## Etiquetas
#SGD #Robustez #AtaquesBizantinos #OptimizaciónDistribuida #Heterogeneidad

Fuente: http://arxiv.org/abs/2005.07866v1
