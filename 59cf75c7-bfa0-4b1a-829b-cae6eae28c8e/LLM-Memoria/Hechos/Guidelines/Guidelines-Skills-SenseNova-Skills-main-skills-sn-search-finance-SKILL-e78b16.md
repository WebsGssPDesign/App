---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-search-finance/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define las directrices para la habilidad de búsqueda financiera "sn-search-finance", diseñada para recopilar datos de mercados globales, fundamentales y noticias. Su función principal es orquestar el uso combinado de scripts automatizados (yfinance, mootdx) y navegación web (browser-use) para validar información y generar reportes estructurados sin fines de inversión.

## Datos clave
- **Proyecto**: `sn-search-finance` (SenseNova Skills).
- **Tecnologías**: Python (`scripts/finance_search.py`), librerías `yfinance`, `mootdx`, `browser-use`.
- **Configuración**: Credenciales en `.env`; instalación de dependencias vía `python3 -m pip install -r requirements.txt`.
- **Comandos principales**: `yf-search`, `yf-profile`, `yf-history`, `tdx-bars` (con frecuencias como `day`, `week`).
- **Flujo de trabajo**: Confirmar mercado -> Ejecutar scripts JSON -> Validar con browser-use si hay errores o falta de evidencia.
- **Restricciones**: No incluir claves en logs; detenerse ante paywalls o captchas; no interpretar resultados como consejos financieros.

## Etiquetas
#finanzas #python #yfinance #browser-use #datos-de-mercado

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-search-finance\SKILL.md`
