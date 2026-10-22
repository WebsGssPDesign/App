---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Database_trigger"
tema: "PostgreSQL Row Level Security"
tags: [web]
---
# Database trigger

## Resumen
Un disparador de base de datos es un código procedural que se ejecuta automáticamente ante eventos específicos en una tabla o vista, siendo fundamental para mantener la integridad de los datos y realizar registros históricos. Diferentes sistemas de gestión (como Oracle, SQL Server o PostgreSQL) ofrecen distintos niveles de granularidad, permitiendo ejecutar lógica por fila o por sentencia, e incluso responder a cambios en el esquema o eventos del sistema.

## Datos clave
- **Granularidad**: Nivel de ejecución puede ser "por fila" (una vez por cada registro afectado) o "por sentencia" (una sola vez para toda la operación SQL).
- **Filtrado por evento**: Se activa ante operaciones generales de tabla o específicamente cuando se modifica una columna concreta.
- **Niveles de disparador**:
  - *DML*: Modificaciones de datos (INSERT, UPDATE, DELETE).
  - *DDL*: Cambios en el esquema (CREATE, ALTER, DROP).
  - *Sistema*: Eventos globales como inicio/fin de sesión o arranque/apagado del servidor.
- **Variables contextuales**: Sistemas como Firebird usan `NEW` y `OLD` para acceder al estado de los datos antes y después de la modificación; MySQL soporta múltiples disparadores del mismo tipo desde la versión 8.0.
- **Restricciones**: Oracle introduce disparadores a nivel de esquema en la versión 8i; PostgreSQL usa "Event Triggers" desde la versión 9.3 para modificaciones no DML.

## Etiquetas
#bases_de_datos #integridad_de_datos #desarrollo_software #sql #automatización

Fuente: https://en.wikipedia.org/wiki/Database_trigger
