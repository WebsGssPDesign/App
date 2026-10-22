---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/1112.2155v1"
tema: "Tanita Vector Database"
tags: [web]
---
# A Concurrency Control Method Based on Commitment Ordering in Mobile Databases

## Resumen
El artículo presenta el algoritmo OPCOT, un método de control de concurrencia para bases de datos móviles que combina técnicas optimistas con un ordenamiento basado en marcas temporales (timestamps). Este enfoque busca superar las limitaciones de los métodos pesimistas y puramente optimistas ante desconexiones frecuentes.

## Datos clave
- **Problema principal**: Las desconexiones impredecibles en entornos móviles dificultan el control de concurrencia.
- **Método base**: Control de concurrencia optimista (para reducir bloqueos y tiempos de espera).
- **Mecánica OPCOT**: Asignación de timestamps a los operadores durante la ejecución; verificación del orden de compromiso en el servidor al final.
- **Ventajas**: Reduce la tasa de abortos, disminuye bloqueos y evita deadlocks comparado con 2PL y métodos optimistas estándar.
- **Validación**: Demostración de serializabilidad mediante grafos y resultados positivos en simulaciones.

## Etiquetas
#basesdedatos #móviles #concurrencia #algoritmos

Fuente: http://arxiv.org/abs/1112.2155v1
