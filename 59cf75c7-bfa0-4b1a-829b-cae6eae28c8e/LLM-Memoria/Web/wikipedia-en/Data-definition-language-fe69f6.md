---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Data_definition_language"
tema: "PostgreSQL Indexes"
tags: [web]
---
# Data definition language

## Resumen
El Lenguaje de Definición de Datos (DDL) es un conjunto de instrucciones sintácticas utilizado para crear, modificar y eliminar objetos dentro de una base de datos relacional. Aunque forma parte del SQL, su función específica se centra en la administración de esquemas mediante comandos imperativos como CREATE, ALTER y DROP, a diferencia de los lenguajes que manipulan datos existentes.

## Datos clave
- **Conceptos principales**: DDL (Data Definition Language), esquema de base de datos, objetos relacionales.
- **Comandos esenciales**:
  - `CREATE`: Establece nuevos componentes como tablas, índices o procedimientos almacenados (`CREATE TABLE`).
  - `DROP`: Elimina completamente un objeto existente (tabla, vista) sin dejar rastro en el sistema.
  - `ALTER`: Modifica las propiedades de un objeto ya creado, por ejemplo, añadiendo columnas.
  - `TRUNCATE`: Borra todos los datos de una tabla pero mantiene la estructura; es más rápido que `DELETE`.
- **Diferencia crítica**: `DROP` elimina la tabla en sí misma, mientras que `DELETE` o `TRUNCATE` solo afectan a los registros dentro de ella.
- **Otros ejemplos**: XML Schema y JSON Schema actúan como DDL para sus respectivos formatos.

## Etiquetas
#BasesDeDatos #SQL #DDL #GestiónDeEsquemas

Fuente: https://en.wikipedia.org/wiki/Data_definition_language
