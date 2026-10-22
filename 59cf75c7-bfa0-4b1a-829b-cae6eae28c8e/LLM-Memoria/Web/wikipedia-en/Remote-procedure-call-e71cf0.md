---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Remote_procedure_call"
tema: "gRPC Protobuf"
tags: [web]
---
# Remote procedure call

## Resumen
Una llamada a procedimiento remoto (RPC) es un mecanismo de comunicación entre procesos que permite ejecutar subrutinas en una computadora diferente como si fuera local, ocultando los detalles de la red al programador. Este modelo implica transparencia de ubicación pero requiere distinguir llamadas remotas de locales debido a diferencias críticas en velocidad y fiabilidad.

## Datos clave
- **Definición**: Acción donde un programa ejecuta una subrutina en otro espacio de direcciones (usualmente otra computadora) sin escribir detalles de interacción remota explícitamente.
- **Componentes**: Cliente (llamador), Servidor (ejecutor), Stub del cliente, Stub del servidor.
- **Proceso**: Marshalling (empaquetar parámetros) -> Envío de mensaje -> Unmarshalling (desempaquetar) -> Ejecución en servidor -> Respuesta.
- **Desafíos**: Las llamadas remotas son órdenes de magnitud más lentas y menos fiables; el cliente debe manejar fallos de red sin saber si la invocación ocurrió realmente.
- **Tecnologías modernas**: gRPC, Apache Thrift (usan serialización binaria eficiente, HTTP/2, autenticación y balanceo de carga).
- **Historia**: Término acuñado por Bruce Jay Nelson en 1981; primeras implementaciones prácticas en los años 80 (Newcastle Connection, Lupine).

## Etiquetas
#RPC #ComputaciónDistribuida #gRPC #Microservicios #Redes

Fuente: https://en.wikipedia.org/wiki/Remote_procedure_call
