---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/software-development/test-driven-development/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía define el desarrollo impulsado por pruebas (TDD) como una metodología estricta que exige escribir la prueba antes del código para garantizar calidad y detectar errores tempranamente. Su objetivo es forzar al desarrollador a definir el comportamiento deseado claramente, eliminando suposiciones y asegurando que cada característica funcione exactamente como se planeó desde el inicio.

## Datos clave
- **Principio central:** "NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST" (Ningún código de producción sin una prueba fallante primero).
- **Ciclo obligatorio:** RED (escribir prueba fallante) → GREEN (código mínimo para pasar) → REFACTOR (limpieza), repitiendo el proceso.
- **Estrategia recomendada:** Usar "balas trazadoras" verticales (una prueba seguida de su implementación inmediata) en lugar de escribir todas las pruebas primero.
- **Herramientas sugeridas:** Comandos `pytest` para ejecutar pruebas específicas y verificar regresiones.
- **Reglas estrictas:** Prohibido adaptar el código existente; si la prueba pasa al inicio, se debe corregir la prueba o borrar el código.

## Etiquetas
#TDD #CalidadDeCódigo #DesarrolloSoftware #PruebasAutomáticas

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\software-development\test-driven-development\SKILL.md`
