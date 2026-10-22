---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/research/polymarket/references/api-endpoints.md"
tags: [hecho]
---
# api-endpoints.md

## Resumen
Este documento describe la referencia de endpoints públicos REST para acceder a datos del mercado Polymarket sin autenticación. Sirve como guía técnica para consultar eventos, mercados, precios en tiempo real y datos históricos mediante tres APIs principales: Gamma, CLOB y Data.

## Datos clave
- **APIs**: `gamma-api`, `clob` y `data-api`. Todos usan GET y retornan JSON.
- **Gamma API**: Endpoints `/public-search`, `/events`, `/markets` y `/tags`. Los campos `outcomePrices`, `outcomes` y `clobTokenIds` son cadenas JSON dobles que deben parsearse.
- **CLOB API**: Proporciona precios actuales (`/price`), punto medio (`/midpoint`), spread (`/spread`) y libros de órdenes (`/book`). Usa `token_id` (índice 0 para "Yes", 1 para "No").
- **Historial**: `/prices-history` requiere el `conditionId` y devuelve precios como probabilidad con timestamps Unix.
- **Flujo de datos**: Para cruzar datos, obtener el `clobTokenIds` del mercado Gamma, parsearlo y usar los tokens correspondientes en las rutas CLOB junto con el `conditionId`.

## Etiquetas
#Polymarket #API #FinanzasDeportivas #Trading

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\research\polymarket\references\api-endpoints.md`
