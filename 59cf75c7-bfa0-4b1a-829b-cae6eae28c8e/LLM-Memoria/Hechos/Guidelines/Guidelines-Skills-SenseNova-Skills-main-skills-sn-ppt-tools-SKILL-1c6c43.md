---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-ppt-tools/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define `sn-ppt-tools`, un conjunto de scripts auxiliares dentro del proyecto SenseNova-Skills para ejecutar búsquedas web, imágenes y generación visual cuando las capacidades nativas del agente principal fallan o no existen. Su función es servir como capa de infraestructura secundaria que complementa al agente host sin duplicar flujos de contenido.

## Datos clave
- **Proyecto**: SenseNova-Skills (Tier 0).
- **Lógica de prioridad**: El agente host siempre tiene prioridad; estos scripts solo se usan si la capacidad nativa falla o no existe tras verificación.
- **Configuración segura**: Los secretos se cargan desde archivos `.env` (`~/.openclaw/.env`, `~/.hermes/.env`) y nunca deben escribirse en el código, prompts ni logs. Se recomienda usar `sn-ppt-doctor` para validar la configuración.
- **Scripts principales**:
  - `web_search.py`: Búsqueda web (requiere API key de Serper/OpenAI).
  - `image_search.py` & `fetch_image.py`: Búsqueda y descarga de imágenes a un directorio específico (`DECK_DIR`).
  - `image_generate.py`: Generación de imágenes usando modelos compatibles con OpenAI/SenseNova.
- **Salidas**: Devuelven JSON simple (`status: ok`, `unavailable` o `failed`) con códigos de salida específicos (0, 2, 1). No realizan bucles de reintento; la lógica de reintentos corresponde al Skill llamador.

## Etiquetas
#SenseNova #PPT-Tools #Infraestructura #Python

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-ppt-tools\SKILL.md`
