---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Write-ahead_logging"
tema: "PostgreSQL Write-Ahead Logging"
tags: [web]
---
# Write-ahead logging

## Resumen
La escritura anticipada (WAL) es una técnica fundamental en sistemas de bases de datos que garantiza las propiedades ACID de atomicidad y durabilidad mediante un registro secuencial antes de modificar los datos principales. Esta estrategia permite recuperar el estado consistente del sistema tras fallos de energía o errores, asegurando que todas las operaciones persistentes se escriban primero en almacenamiento estable.

## Datos clave
- **Atomicidad y Durabilidad**: Propiedades ACID aseguradas por la WAL.
- **Estructura auxiliar**: Registro exclusivo para recuperación ante fallos (crash recovery).
- **Orden de escritura**: Los cambios se registran en el log antes de aplicarse a las páginas de la base de datos.
- **Redo y Undo**: El log almacena tanto información para rehacer como deshacer operaciones.
- **Checkpointing**: Proceso periódico que sincroniza los cambios del log con la base de datos y limpia el registro.
- **Actualización in-place**: Permite modificar datos sin necesidad de copias completas, a diferencia del shadow paging.
- **Journaling**: Variante de WAL utilizada por sistemas de archivos modernos para metadatos.

## Etiquetas
#bases_de_datos #ACID #recuperación_de_fallos #arquitectura_sistemas #persistencia

Fuente: https://en.wikipedia.org/wiki/Write-ahead_logging
