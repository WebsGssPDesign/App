---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-search-academic/references/search.md"
tags: [hecho]
---
# search.md

## Resumen
Este documento describe la arquitectura y el uso de `search.py`, un script centralizado que orquesta búsquedas académicas desde múltiples proveedores (como ArXiv, Semantic Scholar y Wikipedia). Su función principal es unificar las llamadas a diferentes fuentes en una salida JSON consistente, gestionando automáticamente la lógica de reintentos, concurrencia y parámetros específicos para cada proveedor.

## Datos clave
- **Proyecto**: `sn-search-academic` (módulo `search.py`).
- **Tecnologías**: Python 3, CLI, JSON output.
- **Decisiones de diseño**: Implementación de una "cadena de reintentos" (fallback chain) por fuente para garantizar resultados; parámetros se filtran dinámicamente según el proveedor objetivo.
- **Rutas y comandos**: `python3 scripts/search.py "QUERY" --source arxiv,semantic,wikipedia --limit 5`.
- **Pasos importantes de ejecución**: Los proveedores dentro de una misma fuente se ejecutan secuencialmente hasta éxito; fuentes distintas se ejecutan en paralelo con un timeout configurable (default: 60s).

## Etiquetas
#búsqueda_académica #python #arquitectura_de_búsqueda #json

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-search-academic\references\search.md`
