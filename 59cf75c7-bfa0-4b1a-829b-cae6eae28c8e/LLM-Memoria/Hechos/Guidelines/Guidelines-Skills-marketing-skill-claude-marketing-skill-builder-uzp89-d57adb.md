---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/marketing-skill-claude-marketing-skill-builder-uzp891/skills/publish-pipeline/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define una habilidad técnica para publicar contenido de marketing aprobado mediante un pipeline seguro. Su función principal es empaquetar el contenido final y los activos en JSON para enviarlos a sistemas de automatización (como n8n o Make) o APIs directas, tras obtener la aprobación explícita del usuario sobre cada envío.

## Datos clave
- **Proyecto:** Skill `publish-pipeline` dentro del ecosistema de habilidades de marketing.
- **Tecnologías y herramientas:** Bash, JSON, webhooks (n8n, Make), APIs de plataformas.
- **Ruta crítica:** Se debe resolver la variable `CLAUDE_PLUGIN_ROOT` antes de ejecutar cualquier comando o leer archivos.
- **Flujo de seguridad obligatorio:** Verificar estado de configuración (`brand-voice.md`) y confirmar explícitamente cada envío (o lote numerado) mostrando cuenta, destino, adjuntos y texto final; el silencio no se considera aprobación.
- **Reglas de validación:** No enviar posts marcados como "Go/No-Go" bloqueados ni reenviar entradas ya marcadas como "Sent" sin confirmación nueva.
- **Límites de lote:** Máximo 10 ítems por solicitud; si hay más, dividir en oleadas.

## Etiquetas
#marketing #automatización #seguridad #publicación

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\marketing-skill-claude-marketing-skill-builder-uzp891\skills\publish-pipeline\SKILL.md`
