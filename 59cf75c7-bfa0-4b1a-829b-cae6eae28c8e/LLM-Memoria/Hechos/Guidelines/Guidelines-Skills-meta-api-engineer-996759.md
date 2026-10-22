---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/meta-api-engineer.md"
tags: [hecho]
---
# meta-api-engineer.md

## Resumen
Este archivo define el rol de ingeniero experto en la Graph API de Meta, diseñado para diagnosticar y resolver fallos en la publicación automática de contenido entre Facebook e Instagram. Su función principal es guiar el proceso técnico mediante verificaciones específicas de tokens, permisos, conexiones de cuentas y errores comunes del pipeline.

## Datos clave
- **Proyecto**: meta-api-engineer (sonnet).
- **Herramientas**: Read, Bash, Edit, Glob, WebFetch.
- **Requisitos de configuración**: App tipo Business, Página vinculada a cuenta IG Business (`IG_ID`), Scopes obligatorios (`pages_manage_posts`, `instagram_content_publish`, etc.) y token de usuario de larga duración (~60 días).
- **Flujo de diagnóstico**: Verificar vigencia del token (error 190) → Confirmar programación en FB (`/scheduled_posts`) → Validar recepción en IG (`/media`).
- **Solución técnica para imágenes**: Extraer `target.id` de adjuntos si el post es `/feed`, luego consultar `/{photo_id}?fields=images`.
- **Errores comunes**: Uso incorrecto de llaves `{}` en queries (requiere `-g` o `--globoff` en curl) y fallos en jobs de cron/launchd.

## Etiquetas
#MetaAPI #IngenieríaDeSoftware #AutomatizaciónSocial

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\meta-api-engineer.md`
