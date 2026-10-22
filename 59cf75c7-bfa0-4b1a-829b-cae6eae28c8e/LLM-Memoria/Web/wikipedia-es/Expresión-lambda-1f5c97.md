---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://es.wikipedia.org/wiki/Expresi%C3%B3n_lambda"
tema: "Rust Async Runtime"
tags: [web]
---
# Expresión lambda

## Resumen
Una expresión lambda es una subrutina anónima definida sin nombre, común en programación funcional para pasar argumentos a funciones de orden superior o construir resultados. Estas expresiones simplifican el código cuando se usa una función solo ocasionalmente y pueden acceder a variables externas mediante clausuras (closures).

## Datos clave
- **Definición**: Subrutina no enlazada a un identificador, también llamada función literal o anónima.
- **Origen**: Trabajo de Alonzo Church en el cálculo lambda (1936); integrada desde Lisp (1958).
- **Implementación técnica**: Requieren clausuras para acceder a variables no locales; no son recursivas sin un operador de punto fijo o nombre explícito.
- **Usos principales**: Clasificación personalizada, vinculación de eventos, currificación y mapeo sobre listas (ej. `map` en Python).
- **Ejemplo de clasificación**: Ordenar una lista usando `cmp()` dentro de una lambda para comparar longitudes de cadenas o tipos de clase.

## Etiquetas
#programación #lambda #funciones_anónimas #clausuras #currificación

Fuente: https://es.wikipedia.org/wiki/Expresi%C3%B3n_lambda
