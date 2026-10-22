---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-search-year-report/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define las directrices para una habilidad técnica que busca y descarga informes anuales oficiales gratuitos de empresas listadas en diversos mercados globales. Su función principal es facilitar el acceso a datos financieros públicos mediante la combinación de scripts de Python y herramientas de navegación automatizada, priorizando siempre fuentes abiertas sin restricciones de pago o autenticación compleja.

## Datos clave
- **Proyecto**: `sn-search-year-report` (Habilidad SenseNova).
- **Tecnologías**: Python estándar, `browser-use`, scripts personalizados (`year_report_api.py`).
- **Decisiones**: Exclusión total de APIs que requieren claves, tokens o suscripciones; rechazo de fuentes comerciales.
- **Rutas y comandos importantes**:
  - Scripts: `python scripts/year_report_api.py cninfo "Nombre" --year AÑO`
  - Descarga directa: `python scripts/year_report_api.py download URL --output archivo.pdf`
  - Entradas web clave: CNINFO (A-Share), HKEXnews (Hong Kong), SEC EDGAR (EE.UU.), Companies House (UK).
- **Pasos críticos**: Identificar tipo de entidad antes de consultar; usar scripts para consultas estructuradas y `browser-use` para filtrado interactivo en páginas web.

## Etiquetas
#informes-anuales #datos-financieros #scraping-python #compliance

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-search-year-report\SKILL.md`
