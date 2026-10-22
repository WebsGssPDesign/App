---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/productivity/maps/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta herramienta es un conjunto de scripts en Python que permite obtener inteligencia geográfica utilizando datos abiertos de OpenStreetMap y servicios como Nominatim y OSRM. Su función principal es facilitar búsquedas de puntos de interés, cálculo de rutas, conversión entre coordenadas y direcciones, así como la obtención de información horaria y de zonas horarias sin necesidad de claves API ni dependencias externas.

## Datos clave
- **Proyecto**: Skill `maps` para el framework Hermes (versión 1.2.0).
- **Tecnologías**: Python 3.8+ (solo librerías estándar), OpenStreetMap, Nominatim, Overpass API, OSRM, TimeAPI.io.
- **Ruta del script**: `~/.hermes/skills/maps/scripts/maps_client.py`.
- **Comandos principales**:
    - `search`: Geocodificación de nombres a coordenadas.
    - `reverse`: Conversión de coordenadas a dirección completa.
    - `nearby`: Búsqueda de POIs (restaurantes, hospitales, etc.) por categoría y ubicación.
    - `distance` / `directions`: Cálculo de distancia y rutas paso a paso (caminar, conducir, bicicleta).
    - `timezone`: Obtención de zona horaria y hora local.
    - `area` / `bbox`: Definición y búsqueda dentro de cajas delimitadoras geográficas.
- **Integración**: Diseñado para procesar automáticamente coordenadas enviadas como "location pins" en Telegram.

## Etiquetas
#OpenStreetMap #Geolocalización #Python #Rutas #POI

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\productivity\maps\SKILL.md`
