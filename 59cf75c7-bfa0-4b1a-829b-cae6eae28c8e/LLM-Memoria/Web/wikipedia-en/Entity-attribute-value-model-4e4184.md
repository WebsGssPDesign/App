---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Entity%E2%80%93attribute%E2%80%93value_model"
tema: "PostgreSQL JSONB"
tags: [web]
---
# Entity–attribute–value model

## Resumen
El modelo entidad-atributo-valor (EAV) es una estructura de datos diseñada para almacenar eficientemente propiedades dispersas o ad-hoc en situaciones donde los patrones de uso son impredecibles. Este enfoque, análogo a las matrices dispersas, permite gestionar sistemas con un gran número de tipos de propiedad sin necesidad de crear columnas fijas para cada uno.

## Datos clave
- **Conceptos**: Modelo EAV, matriz dispersa, esquema abierto, volatilidad de atributos.
- **Estructura**: Tres columnas principales: Entidad (ID del ítem), Atributo (clave foránea a definiciones) y Valor.
- **Características físicas**: Tablas descritas como "largas y delgadas" (muchas filas, pocas columnas).
- **Analogías**: Comparado con una lista de artículos en un recibo de supermercado que solo incluye lo comprado, no todo el inventario.
- **Ventaja**: Evita la necesidad de agregar o revisar constantemente tablas cuando surgen nuevos atributos (ej. nuevas pruebas médicas o productos).

## Etiquetas
#modelos_de_datos #EAV #almacenamiento_disperso #base_de_datos_relacional

Fuente: https://en.wikipedia.org/wiki/Entity%E2%80%93attribute%E2%80%93value_model
