---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/hooopo/shadow"
tema: "Temporal History Tables"
tags: [web]
---
# hooopo/shadow

## Resumen
El proyecto Shadow es una extensión para PostgreSQL que implementa tablas de historial (Shadow Tables) a nivel de base de datos. Captura automáticamente el estado anterior de las filas antes de insertar, actualizar o eliminar registros, resolviendo problemas de dimensiones cambiantes lentamente sin depender del código de la aplicación.

## Datos clave
- **Mecanismo**: Usa triggers (`BEFORE INSERT/UPDATE/DELETE`) para capturar snapshots y un rango temporal (`tstzrange` en `sys_period`).
- **Modos de implementación**:
  - *Static copy*: Replica la estructura exacta de la tabla original; requiere mantenimiento manual si cambian los campos.
  - *JSONB*: Almacena el historial en formato JSON flexible, evitando problemas de incompatibilidad de tipos de datos entre tablas.
- **Información capturada**: Valores previos, tipo de operación (`op`), consulta ejecutada (`op_query`) y usuarios de sesión (DB y App).
- **Ventajas**: Funciona con SQL directo (bypass del ORM), es compatible con servicios en la nube (sin C extensions) e integra información de aplicación.

## Etiquetas
#PostgreSQL #ShadowTable #HistorialDeDatos #SlowlyChangingDimension #Auditoría

Fuente: https://github.com/hooopo/shadow
