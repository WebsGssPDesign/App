---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-search-social-en/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe una herramienta para buscar contenido en plataformas sociales en inglés como Reddit, Twitter/X y YouTube. Su función principal es facilitar la obtención de resultados específicos mediante scripts automatizados que respetan las políticas de seguridad al manejar credenciales externas.

## Datos clave
- **Proyecto**: `sn-search-social-en` (SenseNova Skills).
- **Tecnologías**: Python 3, librerías de terceros (Reddit API, TikHub para Twitter, YouTube Data API), gestión de dependencias vía `requirements.txt`.
- **Configuración**: Las credenciales (`TIKHUB_TOKEN`, `YOUTUBE_API_KEY`) deben almacenarse en `.env` o pasadas por CLI; nunca en el código.
- **Scripts principales**:
  - `reddit_search.py`: No requiere API key, soporta filtros de subreddit y tiempo.
  - `twitter_search.py`: Requiere token de TikHub.
  - `youtube_search.py`: Requiere API key de YouTube.
- **Comandos clave**: `python3 scripts/[nombre].py <query> [opciones]`. El límite por defecto es 10 resultados y el formato de salida es JSON.

## Etiquetas
#búsqueda #redes_sociales #automatización #python

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-search-social-en\SKILL.md`
