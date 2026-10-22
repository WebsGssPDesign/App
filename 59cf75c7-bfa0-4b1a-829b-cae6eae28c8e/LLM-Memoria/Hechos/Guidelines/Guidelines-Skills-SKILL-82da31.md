---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía establece el protocolo inicial para configurar la integración de Meta Developers, permitiendo publicar contenido en Facebook e Instagram mediante API. Su función principal es estandarizar la creación de aplicaciones, la vinculación de cuentas y la gestión segura de credenciales a largo plazo.

## Datos clave
- **Requisitos**: App tipo Business, Página de FB vinculada a cuenta IG Business.
- **Scopes necesarios**: `pages_manage_posts`, `instagram_content_publish`, `business_management` entre otros.
- **Gestión de tokens**: Se requiere un Long-lived User Access Token (~60 días) para derivar el Page Access Token dinámicamente en cada ejecución.
- **Seguridad**: Las credenciales (PAGE_ID, IG_ID, USER_TOKEN) deben almacenarse en archivos JSON locales fuera del repositorio Git y nunca compartirse públicamente.
- **Diagnóstico**: Un error 190 en `GET /me` indica que el token ha caducado y debe renovarse.

## Etiquetas
#MetaDevelopers #APIInstagram #GestiónDeTokens #Seguridad

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SKILL.md`
