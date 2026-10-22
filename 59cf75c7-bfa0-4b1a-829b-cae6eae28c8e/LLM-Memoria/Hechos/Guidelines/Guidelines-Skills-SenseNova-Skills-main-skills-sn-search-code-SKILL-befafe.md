---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-search-code/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe una herramienta de búsqueda para desarrolladores que consulta cuatro plataformas clave: GitHub, Stack Overflow, Hacker News y HuggingFace. Su función principal es permitir la recuperación de código, repositorios, discusiones técnicas y recursos de IA mediante scripts automatizados que generan resultados en formato JSON.

## Datos clave
- **Proyecto**: `sn-search-code` (Skills/SenseNova).
- **Tecnologías**: Python 3, APIs de GitHub/Stack Overflow/HuggingFace/Hacker News.
- **Decisión crítica**: La búsqueda de código en GitHub (`--type code`) requiere obligatoriamente un token de autenticación; los otros tipos y las demás plataformas no lo necesitan para funcionar básico.
- **Configuración**: Las credenciales (tokens, claves API) deben almacenarse exclusivamente en el archivo `.env` o pasadas vía CLI, nunca en el código fuente ni logs.
- **Comandos principales**: `python3 scripts/github_search.py <query> --type code --token ...`, `python3 scripts/stackoverflow_search.py <query> --sort votes`.
- **Instalación**: Se requiere ejecutar `python3 -m pip install -r requirements.txt` antes de usar los scripts.

## Etiquetas
#búsqueda_de_código #automatización_dev #api_integration #herramientas_python

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-search-code\SKILL.md`
