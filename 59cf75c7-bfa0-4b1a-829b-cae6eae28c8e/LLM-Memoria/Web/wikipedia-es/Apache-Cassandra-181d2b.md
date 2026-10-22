---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://es.wikipedia.org/wiki/Apache_Cassandra"
tema: "gRPC Server Streaming"
tags: [web]
---
# Apache Cassandra

## Resumen
Apache Cassandra es una base de datos NoSQL distribuida y descentralizada escrita en Java, diseñada por Facebook y mantenida por la Apache Software Foundation para manejar grandes volúmenes de datos con alta disponibilidad y escalabilidad lineal. Su arquitectura elimina el punto único de fallo mediante nodos iguales que se comunican entre sí sin un servidor maestro.

## Datos clave
- **Arquitectura**: Modelo P2P (peer-to-peer) basado en protocolo "gossip" y topología anillo; no tiene nodo maestro.
- **Escalabilidad**: Permite escalar o reducir dinámicamente el clúster sin interrupciones.
- **Modelo de datos**: Almacena datos estructurados/semi-estructurados (cadenas, enteros, fechas); utiliza particiones y claves primarias con componente de clave de partición.
- **Limitaciones**: No soporta sentencias JOIN ni subconsultas; enfatiza la desnormalización mediante colecciones.
- **Lenguaje**: Utiliza CQL (Cassandra Query Language), similar a SQL pero menos funcional, accesible vía JDBC en Java.
- **Historia**: Desarrollada inicialmente por Facebook, lanzada como open source en 2008 y graduada como proyecto Apache en 2010.

## Etiquetas
#ApacheCassandra #BaseDeDatosNoSQL #ArquitecturaDistribuida #Escalabilidad

Fuente: https://es.wikipedia.org/wiki/Apache_Cassandra
