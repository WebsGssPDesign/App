---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Decision_time"
tema: "Temporal History Tables"
tags: [web]
---
# Decision time

## Resumen
El tiempo de decisión en bases de datos temporales marca el momento exacto en que se tomó una resolución sobre un hecho, diferenciándose del tiempo válido (cuándo ocurrió) y el tiempo transaccional (cuándo se guardó). Este concepto permite modelar la historia de las decisiones que validaron los datos, siendo esencial para sistemas bitemporales o tritemporales.

## Datos clave
- **Definición**: Momento en que se decide sobre un hecho almacenado; intervalo cerrado-abierto [inicio, fin).
- **Relación temporal**: Debe ser estrictamente anterior al tiempo transaccional (nunca futuro), pero no está vinculado cronológicamente al tiempo válido.
- **Historia**: El término fue acuñado por Nascimento y Eich en 1995; el estándar ISO SQL lo incluye como "application-time period tables" desde la versión de 2011, aunque sin cláusulas específicas dedicadas.
- **Ejemplo práctico**: En elecciones presidenciales de EE.UU., un retraso de 7 días entre la decisión y la transacción muestra cómo los cargos (ej. Nixon/Agnew) cambian según el tiempo de consulta.

## Etiquetas
#bases_de_datos #tiempo_decision #temporalidad #SQL #historia_datos

Fuente: https://en.wikipedia.org/wiki/Decision_time
