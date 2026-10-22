---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/social-scheduler.md"
tags: [hecho]
---
# social-scheduler.md

## Resumen
Este documento define las operaciones para programar publicaciones en Facebook e Instagram mediante la Graph API, enfatizando que son mecanismos distintos que requieren verificación independiente. Su función es gestionar la cola de publicación asegurando que el contenido aparezca correctamente en ambas plataformas y confirmar el éxito final en Instagram.

## Datos clave
- **Proyecto:** social-scheduler (operación de publicaciones).
- **Tecnologías:** Graph API, Content Publishing API, Bash, Glob, curl.
- **Decisión crítica:** El espejo a Instagram es un job separado (`publish_ig_from_fb.py`), no el parámetro `instagram_actor_id`.
- **Comandos y rutas importantes:**
  - Facebook: `/{PAGE_ID}/photos` (published=false) seguido de `/{PAGE_ID}/feed` con `attached_media` y `scheduled_publish_time`.
  - Verificación FB: `GET /{PAGE_ID}/scheduled_posts` y `/{PAGE_ID}/published_posts`.
  - Verificación IG (la verdad): `GET /{IG_ID}/media?fields=caption,timestamp`.
- **Gotchas técnicos:** Usar `-g`/`--globoff` con llaves en curl; la imagen del post está en `attachments{media,target}` → `target.id`; los lotes de ~5 imágenes pueden causar timeouts.

## Etiquetas
#social-media #graph-api #automatización #verificación

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\social-scheduler.md`
