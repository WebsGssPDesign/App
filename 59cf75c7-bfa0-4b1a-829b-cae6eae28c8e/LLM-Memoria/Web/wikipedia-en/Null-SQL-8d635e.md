---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Null_%28SQL%29"
tema: "PostgreSQL Logical Decoding"
tags: [web]
---
# Null (SQL)

## Resumen
NULL en SQL es un marcador especial que indica la ausencia de información o datos inaplicables, introducido por E.F. Codd para cumplir con los requisitos de las bases de datos relacionales. A diferencia del valor cero, NULL representa una falta de dato conocida, no un valor numérico nulo. Su propagación en operaciones aritméticas y lógicas genera resultados desconocidos, siguiendo una lógica ternaria que ha sido fuente de controversia y debate técnico.

## Datos clave
- **Definición**: Marcador para datos faltantes o inaplicables (no confundir con 0).
- **Origen**: Propuesto por E.F. Codd en los años 70; simbolizado originalmente con la omega griega ($\omega$).
- **Comportamiento aritmético**: Cualquier operación matemática con NULL devuelve NULL (ej: $10 \times \text{NULL} = \text{NULL}$).
- **Lógica ternaria (3VL)**: Las comparaciones con NULL generan tres estados: Verdadero, Falso o Desconocido.
- **Controversia**: La complejidad de la lógica NULL y las inconsistencias en el estándar SQL han impedido la adopción de propuestas alternativas como los "A-Values" e "I-Values".

## Etiquetas
#SQL #BasesDeDatos #NULL #LógicaTernaria #EFCodd

Fuente: https://en.wikipedia.org/wiki/Null_%28SQL%29
