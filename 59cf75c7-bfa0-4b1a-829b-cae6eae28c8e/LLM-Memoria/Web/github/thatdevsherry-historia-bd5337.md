---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/thatdevsherry/historia"
tema: "Temporal History Tables"
tags: [web]
---
# thatdevsherry/historia

## Resumen
Historia es un módulo en Python que implementa tablas temporales para SQLite utilizando el módulo nativo sqlite3, permitiendo rastrear cambios de datos y su historial. El sistema crea automáticamente una tabla de respaldo al modificar registros principales y soporta consultas específicas para recuperar información en momentos pasados.

## Datos clave
- **Conceptos**: Tablas temporales, auditoría de datos, recuperación de versiones anteriores.
- **Columnas adicionales**: `valid_from` (fecha inicio) y `valid_to` (fecha fin).
- **Comandos soportados**: CREATE TABLE, INSERT, UPDATE, DELETE.
- **Cláusulas de consulta temporal**: AS OF, FROM 'X' TO 'Z', BETWEEN 'X' AND 'Z', CONTAINED IN ('X', 'Y').
- **Mecanismo**: Al insertar, actualizar o eliminar en la tabla principal, se generan automáticamente registros en la tabla `_history` con marcas de tiempo.

## Etiquetas
#Python #SQLite #HistorialDeDatos #TemporalTables #Auditoría

Fuente: https://github.com/thatdevsherry/historia
