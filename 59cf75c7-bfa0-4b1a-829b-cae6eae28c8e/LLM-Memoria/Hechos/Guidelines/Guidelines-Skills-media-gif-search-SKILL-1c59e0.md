---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/media/gif-search/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este archivo describe una guía técnica para buscar y descargar GIFs directamente desde la API de Tenor utilizando las herramientas estándar `curl` y `jq`. Su objetivo es facilitar la obtención de contenido visual sin necesidad de instalar software adicional, permitiendo filtrar por calidad y formato según el uso previsto.

## Datos clave
- **Proyecto**: gif-search (versión 1.1.0).
- **Tecnologías**: Tenor API, `curl`, `jq`.
- **Requisitos previos**: Variable de entorno `TENOR_API_KEY` (obtenida en Google Cloud Console), herramientas `curl` y `jq`.
- **Comandos principales**: Búsqueda con parámetros `q`, `limit` y `key`; extracción de URLs mediante `jq -r '.results[].media_formats.gif.url'`.
- **Descarga**: Flujo que combina búsqueda para obtener la URL y descarga directa con `curl -sL "$URL" -o archivo.gif`.
- **Formatos disponibles**: `gif`, `tinygif` (previos), `mp4`, `tinymp4`, `webm`, `nanogif`.
- **Parámetros de seguridad**: Filtro `contentfilter` (off, low, medium, high).

## Etiquetas
#TenorAPI #GIFSearch #curl #jq #Automatización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\media\gif-search\SKILL.md`
