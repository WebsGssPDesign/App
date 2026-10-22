---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/DataDog/temporal-large-payload-codec"
tema: "Temporal Workflow History Service"
tags: [web]
---
# DataDog/temporal-large-payload-codec

## Resumen
Este repositorio ofrece un servicio HTTP y un codificador de cargas para Temporal que permite persistir payloads más allá del límite de 4MB fuera del historial de flujos de trabajo. La solución utiliza almacenamiento en la nube como backend mediante una interfaz de almacenamiento direccionado por contenido, facilitando el manejo transparente de datos grandes sin comprometer la integridad del workflow.

## Datos clave
- Límite nativo de Temporal: 4MB (el servicio maneja payloads >128KB automáticamente).
- Backend: Almacenamiento en la nube (ejemplo: S3) vía interfaz HTTP.
- Configuración: Requiere variables de entorno `AWS_SDK_REGION` y `BUCKET`.
- Punto de conexión: El servidor escucha por defecto en el puerto 8577.
- Seguridad: Por defecto, lanza pánico ante errores de E/S para permitir la reintentabilidad segura dentro del SDK Temporal.
- Formato: Añade metadatos `temporal.io/remote-codec` y usa hashes SHA256 para identificar blobs remotos.

## Etiquetas
#Temporal #BigData #CloudStorage #DevOps #Golang

Fuente: https://github.com/DataDog/temporal-large-payload-codec
