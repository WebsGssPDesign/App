---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/1907.02664v2"
tema: "PostgreSQL Change Data Capture"
tags: [web]
---
# Data Encoding for Byzantine-Resilient Distributed Optimization

## Resumen
Este artículo propone un método de codificación de datos basado en corrección de errores para proteger algoritmos de optimización distribuida contra nodos corruptos (Byzantine). La solución permite tolerar hasta la mitad menos uno de los trabajadores comprometidos y ofrece garantías determinísticas sin asumir distribuciones específicas de los datos.

## Datos clave
- Algoritmos protegidos: Descent Gradiente Proximal (PGD) y Descenso por Coordenadas (CD).
- Tolerancia óptima: $t \leq \lfloor\frac{m-1}{2}\rfloor$ nodos corruptos entre $m$ trabajadores.
- Eficiencia: Esquema de codificación "sparse" con sobrecarga constante para $t \leq m/3$.
- Extensibilidad: Funciona en modelos de flujo de datos y Descent Gradiente Estocástico (SGD).

## Etiquetas
#optimización #seguridad #byzantine #distribuido #codificación

Fuente: http://arxiv.org/abs/1907.02664v2
