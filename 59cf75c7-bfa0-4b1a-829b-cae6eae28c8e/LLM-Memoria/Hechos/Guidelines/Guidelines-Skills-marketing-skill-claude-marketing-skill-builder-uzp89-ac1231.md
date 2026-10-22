---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/marketing-skill-claude-marketing-skill-builder-uzp891/EXAMPLE.md"
tags: [hecho]
---
# EXAMPLE.md

## Resumen
Este documento ilustra un flujo de trabajo completo para investigar competidores, generar contenido y publicar en redes sociales mediante una herramienta de automatización. Su función principal es demostrar cómo el sistema detiene la ejecución antes del envío real hasta recibir confirmación explícita del usuario, garantizando seguridad.

## Datos clave
- **Proyecto:** Pipeline completo de marketing ("full-pipeline") para responder a competidores como "Northwind Cloud".
- **Tecnologías:** n8n (webhooks), Claude (IA generativa), MCP tools (herramientas de generación visual).
- **Decisiones críticas:** El comando inicial "publish it" autoriza la preparación del envío, pero no el envío real; se requiere una confirmación explícita ("Yes — send...").
- **Rutas y pasos:**
  1. Investigación de competidores (análisis SWOT, movimientos recientes).
  2. Creación de contenido (post para LinkedIn, boletín de noticias).
  3. Breve visual (lista de disparos para imágenes).
  4. Punto de control de aprobación: revisión del payload JSON antes de ejecutar la petición POST al webhook.
- **Comandos/acciones:** `POST` a un endpoint de n8n, actualización de estado en `state/content-calendar.md`.

## Etiquetas
#automatización #marketing #seguridad #IA #flujo-trabajo

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\marketing-skill-claude-marketing-skill-builder-uzp891\EXAMPLE.md`
