---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/wwindcloud/pg-subscription-stream"
tema: "PostgreSQL Logical Replication Slots"
tags: [web]
---
# wwindcloud/pg-subscription-stream

## Resumen
Esta biblioteca facilita la suscripción a cambios de datos en PostgreSQL mediante replicación lógica, evitando errores comunes con los mecanismos nativos de notificación. Funciona emulando `pg_recvlogical` para permitir que aplicaciones Node.js consuman flujos de datos desde múltiples publicaciones de forma confiable. El sistema garantiza que el lado receptor obtenga todos los cambios antes de avanzar, asegurando la integridad de los datos incluso ante problemas de red transitorios.

## Datos clave
- **Instalación**: `npm install pg-subscription-stream`
- **Mecanismo**: Utiliza slots de replicación lógica (`pgoutput`) y publicaciones (`PUBLICATION`).
- **Clases principales**: `PgSubscriptionStream` para iniciar el flujo y `PgOutputParser` para decodificar los datos.
- **Estructura del dato**: Los chunks devueltos contienen propiedades como `kind`, `schema`, `table`, `KEY`, `OLD` (antes) y `NEW` (después).
- **Flujo de trabajo**: Se conecta un cliente de replicación, se crea el stream con el nombre del slot y las publicaciones objetivo, y luego se procesa mediante una tubería (`pipeline`) o iterador asíncrono.

## Etiquetas
#PostgreSQL #ReplicaciónLógica #NodeJS #Streaming #BaseDeDatos

Fuente: https://github.com/wwindcloud/pg-subscription-stream
