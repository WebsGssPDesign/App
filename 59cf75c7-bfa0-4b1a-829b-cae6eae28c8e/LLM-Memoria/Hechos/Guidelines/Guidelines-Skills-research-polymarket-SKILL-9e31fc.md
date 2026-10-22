---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/research/polymarket/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define una habilidad técnica para consultar datos públicos de mercados predictivos en Polymarket mediante sus APIs REST sin autenticación. Sirve para extraer probabilidades, precios y volúmenes de eventos específicos, presentando la información como porcentajes legibles para el usuario final.

## Datos clave
- **APIs públicas**: Gamma (búsqueda), CLOB (precios en tiempo real/libros de órdenes) y Data (historial de operaciones).
- **Conceptos centrales**: Los precios representan probabilidades directas (ej. 0.65 = 65%); los eventos contienen múltiples mercados binarios (Sí/No).
- **Flujo de trabajo**: Buscar con `gamma-api`, parsear respuestas JSON doblemente codificadas y presentar resultados formateados.
- **Limitaciones**: Solo lectura; no permite ejecutar operaciones comerciales ni requiere claves privadas para datos públicos.

## Etiquetas
#polymarket #api-rest #datos-financieros #mercados-predictivos

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\research\polymarket\SKILL.md`
