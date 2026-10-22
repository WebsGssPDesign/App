---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2602.07455v1"
tema: "Rust Async Runtime"
tags: [web]
---
# RustCompCert: A Verified and Verifying Compiler for a Sequential Subset of Rust

## Resumen
El proyecto presenta el desarrollo de un compilador para Rust basado en CompCert que garantiza la preservación semántica desde el código fuente hasta el ensamblaje y asegura la seguridad de memoria mediante una verificación exhaustiva. Este enfoque permite simplificar la verificación de programas al centrar las herramientas en la corrección funcional gracias a la comprobación de préstamos integrada.

## Datos clave
- Compilador basado en CompCert para un subconjunto secuencial de Rust.
- Garantía 1: Preservación semántica (el comportamiento del código objetivo incluye el del fuente).
- Garantía 2: Seguridad de memoria asegurada por compilación verificadora.
- Paso clave: La fase de comprobación de préstamos (*borrow checking*) simplifica la verificación al permitir a las herramientas enfocarse únicamente en la corrección funcional.

## Etiquetas
#Rust #CompCert #VerificaciónFormal #SeguridadDeMemoria #Compiladores

Fuente: http://arxiv.org/abs/2602.07455v1
