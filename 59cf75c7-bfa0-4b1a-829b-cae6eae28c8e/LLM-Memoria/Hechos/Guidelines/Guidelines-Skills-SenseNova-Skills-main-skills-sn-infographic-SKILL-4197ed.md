---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-infographic/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define la habilidad `sn-infographic` del proyecto SenseNova-Skills, diseñada para generar infografías profesionales mediante un flujo de trabajo automatizado. La herramienta analiza el contenido del usuario, sugiere estilos y genera imágenes finales listas para publicar utilizando una arquitectura de dos agentes. Sirve como punto central para cualquier solicitud relacionada con visualización de datos o diagramas dentro del ecosistema.

## Datos clave
- **Proyecto**: SenseNova-Skills (Tier 1).
- **Tecnologías base**: Depende de `sn-image-base` (Tier 0) para herramientas de generación, reconocimiento y optimización de texto (`sn-image-generate`, `sn-image-recognize`, `sn-text-optimize`).
- **Arquitectura**: Utiliza un agente principal (Main Agent) para la gestión del usuario y parámetros, y un agente trabajador (Worker Agent) que ejecuta el pipeline interno sin interactuar directamente con el usuario.
- **Parámetros críticos**: `max_rounds` (1-8), `output_mode` (`friendly` o `verbose`), `prompts_expand_mode` (`auto`, `force`, `disable`).
- **Autenticación**: Usa claves por defecto de entorno (`SN_TEXT_API_KEY`, `SN_VISION_API_KEY`, `SN_IMAGE_GEN_API_KEY`) leídas vía CLI o variables.
- **Flujo de trabajo**: Extracción de parámetros (directivas en línea y palabras clave) → Expansión de prompts → Generación múltiple con revisión VLM → Clasificación por calidad.

## Etiquetas
#SenseNova #Infografías #Automatización #IAVisual #ArquitecturaAgentes

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-infographic\SKILL.md`
