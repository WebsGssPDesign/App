---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Temporal_database"
tema: "Temporal Event Sourcing"
tags: [web]
---
# Temporal database

## Resumen
Una base de datos temporal almacena información relacionada con instancias pasadas, presentes y futuras del tiempo, diferenciándose de las bases de datos actuales que solo reflejan el estado presente. Estas bases gestionan múltiples ejes temporales, como el tiempo válido (cuando un hecho es cierto en la realidad) y el tiempo transaccional (cuando se registró en la base).

## Datos clave
- **Tipos:** Uni-temporal (un eje), Bi-temporal (tiempo válido + transaccional/decisión) y Tri-temporal (los tres ejes).
- **Conceptos temporales:** Tiempo válido (*valid time*), tiempo transaccional (*transaction time*) y tiempo de decisión (*decision time*).
- **Estándares SQL:** Evolución desde TSQL2 hacia SQL:2011, que incluye tablas de "periodo de tiempo de aplicación", "versionadas por sistema" y bitemporales.
- **Características técnicas:** Tipos de datos de periodos temporales, claves primarias temporales, integridad referencial temporal y predicados basados en la álgebra de intervalos de Allen.
- **Ejemplo ilustrativo:** La biografía ficticia de John Doe para demostrar cómo registrar cambios de estado (nacimiento, mudanza, fallecimiento) con precisión temporal.

## Etiquetas
#basesdedatos #tiempodiscreto #SQLtemporal #historialdedatos #tecnologiadeinformación

Fuente: https://en.wikipedia.org/wiki/Temporal_database
