---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-search-social-cn/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe un conjunto de scripts para buscar contenido en plataformas sociales chinas como Bilibili, Zhihu y Douyin. Su función principal es facilitar la recuperación de información mediante APIs específicas o métodos de respaldo web cuando no existen scripts automatizados disponibles.

## Datos clave
- **Proyecto**: `sn-search-social-cn` (Skills/SenseNova).
- **Plataformas con script**: Bilibili (`bilibili_search.py`), Zhihu (`zhihu_search.py`), Douyin (`douyin_search.py`).
- **Plataformas sin script**: Xiaohongshu, Weibo (requieren `browser-use` o búsqueda web manual).
- **Configuración de credenciales**: Los cookies deben almacenarse en variables de entorno (`.env`) como `BILIBILI_COOKIE`, `ZHIHU_COOKIE`, `DOUYIN_COOKIE`. No se incluyen claves reales en el payload.
- **Instalación**: Se requiere ejecutar `python3 -m pip install -r requirements.txt` antes del uso.
- **Comandos de ejemplo**:
  - Bilibili: `python3 scripts/bilibili_search.py "query" --order click --limit 10`
  - Zhihu: `ZHIHU_COOKIE="..." python3 scripts/zhihu_search.py "topic" --type topic --limit 5`
  - Douyin: `DOUYIN_COOKIE="..." python3 scripts/douyin_search.py "query" --limit 5`
- **Salida**: Formato JSON estándar para scripts activos; estructura flexible para búsquedas web de respaldo.

## Etiquetas
#búsqueda #chinasocialmedia #automatización #cookies #api

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-search-social-cn\SKILL.md`
