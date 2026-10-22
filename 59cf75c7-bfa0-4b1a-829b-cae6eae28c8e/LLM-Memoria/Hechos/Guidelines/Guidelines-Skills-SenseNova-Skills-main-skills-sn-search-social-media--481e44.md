---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-search-social-media/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía define las directrices para la habilidad de búsqueda en redes sociales y medios, permitiendo a los agentes recopilar señales públicas sobre tendencias tecnológicas sin utilizar datos sensibles o recursos de pago. Su función es asegurar que las consultas se limiten a fuentes abiertas y gratuitas, evitando temas como criptomonedas y protegiendo credenciales de seguridad.

## Datos clave
- **Restricciones estrictas**: Prohibido usar API keys, tokens, cookies o datos relacionados con criptomonedas, Web3 y blockchain; solo fuentes públicas y gratuitas.
- **Herramientas permitidas**: Scripts locales (`wikimedia_pageviews.py`, `github_public_search.py`, etc.) y navegación web manual vía `browser-use`.
- **Configuración de seguridad**: Las credenciales deben almacenarse en `.env` como variables de entorno, nunca en el código o logs.
- **Comandos principales**: Ejecución de scripts para buscar repositorios de GitHub, issues, tendencias en Stack Exchange y noticias de Hacker News.
- **Flujo de trabajo**: Combinar resultados de múltiples fuentes (GitHub, Wikipedia, Baidu Index) y reportar conflictos sin generalizar una sola plataforma como tendencia global.

## Etiquetas
#búsqueda-social #guías-de-uso #seguridad-información #tendencias-tecnológicas

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-search-social-media\SKILL.md`
