---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2010.09073v1"
tema: "gRPC Bidirectional Streams"
tags: [web]
---
# Handling Bidirectional Control Flow: Technical Report

## Resumen
El informe presenta "efectos algebraicos bidireccionales", una nueva abstracción de programación diseñada para manejar flujos de control complejos que permiten transferir el control hacia atrás al sitio donde se originó un efecto, superando las limitaciones de los efectos asíncronos tradicionales. Este enfoque busca unificar la programación basada en efectos con la orientación a objetos mediante una semántica formal tipo-safe y abstraction-safe.

## Datos clave
- **Bidirectional Algebraic Effects**: Abstracción que permite a los manejadores (handlers) levantar efectos para devolver el control al origen y manejar sus propios efectos recursivamente.
- **Problema de parametricity**: La propagación estándar de efectos (como excepciones) rompe la parametricidad en presencia de polimorfismo de efectos; la bidireccionalidad agrava esto.
- **Core Language**: Un lenguaje base que generaliza operaciones y manejadores de efectos, construido sobre semántica existente de "tunneling".
- **Seguridad formal**: Garantía de que no hay efectos sin manejar (type-safe) ni manejados accidentalmente (abstraction-safe).
- **Modelo lógico**: Uso de relaciones lógicas indexadas por pasos para demostrar parametricidad y corrección, totalmente mecanizadas en Coq.
- **Eficiencia**: Experimentos preliminares confirman que los manejadores bidireccionales pueden implementarse eficientemente como característica de primera clase.

## Etiquetas
#programación #efectos_algebraicos #bidireccionalidad #Coq #formal_verification

Fuente: http://arxiv.org/abs/2010.09073v1
