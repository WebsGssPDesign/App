---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-search-market-cn/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía define un protocolo para investigar el mercado chino utilizando exclusivamente fuentes oficiales gratuitas, sin requerir claves API, registros ni datos de criptomonedas. Establece una jerarquía operativa que prioriza scripts automatizados para anuncios bursátiles y utiliza navegación web controlada (browser-use) para acceder a estadísticas macroeconómicas, regulatorias e industriales cuando no existen interfaces públicas directas.

## Datos clave
- **Proyecto**: `sn-search-market-cn` (búsqueda comercial en China).
- **Tecnologías**: Python estándar (`scripts/free_market_api.py`), `browser-use`.
- **API principal**: `cninfo-announcements` para consultar anuncios de la Bolsa A, informes anuales y cartas de interrogatorio.
- **Recursos web clave**: Portal de datos del Estado (GDP, CPI), CNIPA (patentes), NMPA (dispositivos médicos) y sitios de bolsas (SSE, SZSE).
- **Restricciones críticas**: No usar interfaces que requieran firma digital, OAuth o pago; abandonar recursos si presentan CAPTCHA o muros de acceso.
- **Comandos de ejemplo**: `python scripts/free_market_api.py cninfo-announcements --keyword 年报`.

## Etiquetas
#mercado_china #datos_oficiales #scraping_legal #finanzas

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-search-market-cn\SKILL.md`
