---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://es.wikipedia.org/wiki/Vista_materializada"
tema: "PostgreSQL Materialized Views"
tags: [web]
---
# Vista materializada

## Resumen
Una vista materializada almacena el resultado de una consulta en una tabla física real, ofreciendo un acceso más rápido a cambio de mayor espacio y posible desactualización. A diferencia de las vistas virtuales que calculan los datos al vuelo, estas permiten la creación de índices para optimizar búsquedas complejas. Son fundamentales en entornos de almacenes de datos donde el costo de consultar tablas base es elevado.

## Datos clave
- **Ventajas**: Acceso eficiente y capacidad de crear índices en cualquier columna.
- **Desventajas**: Incremento del tamaño de la base de datos y riesgo de falta de sincronía (datos desfasados).
- **Implementaciones**: Oracle 8i, Sybase SQL Anywhere, IBM DB2 ("materialized query tables"), Microsoft SQL Server ("vistas indexadas"). PostgreSQL soporta vistas desde la versión 9.3, con actualización manual o concurrente (opción CONCURRENTLY).
- **MySQL**: No tiene soporte nativo; requiere triggers o procedimientos almacenados como aproximación.

## Etiquetas
#bases_de_datos #optimización #almacén_de_datos #PostgreSQL #Oracle

Fuente: https://es.wikipedia.org/wiki/Vista_materializada
