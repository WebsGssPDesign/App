---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/JobRunr"
tema: "Kubernetes CronJobs"
tags: [web]
---
# JobRunr

## Resumen
JobRunr es una biblioteca de código abierto para Java que permite programar tareas en segundo plano distribuidas entre múltiples máquinas virtuales (JVM). A diferencia de soluciones tradicionales como Quartz o Spring Batch, ofrece una API ligera integrada con frameworks modernos y un panel de control incorporado. Su arquitectura reciente incorpora características avanzadas como programación consciente del carbono y soporte nativo para hilos virtuales.

## Datos clave
- **Historial**: Lanzada en abril de 2020 por Ronald Dehuysser; versiones destacadas incluyen la 8.0 (programación verde) y la 8.6 (compatibilidad JDK 26).
- **Funcionalidad**: Enqueue, delay o ejecución recurrente de tareas (emails, PDFs, ETL) usando lambdas Java o referencias a métodos.
- **Almacenamiento**: Soporta RDBMS (PostgreSQL, Oracle), NoSQL (MongoDB, Redis) y almacenamiento en memoria mediante `StorageProvider`.
- **Arquitectura**: Uso de bloqueos optimistas para garantizar ejecución exactamente una vez; servidores (`BackgroundJobServer`) consultan la base de datos cada 200 ms a 15 s.
- **Nuevas características (v8+)**: Programación consciente del carbono (CO₂), hilos virtuales JDK 21+, UUIDs basados en tiempo y soporte para Kotlin.

## Etiquetas
#Java #JobRunr #OrquestaciónDeTareas #JDK26 #Sostenibilidad

Fuente: https://en.wikipedia.org/wiki/JobRunr
