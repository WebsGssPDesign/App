---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-image-resume/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta habilidad genera imágenes de portafolio tipo currículum a partir del texto proporcionado por el usuario, aplicando un diseño vertical predefinido. Sirve para convertir datos de experiencia y perfil en una visualización atractiva lista para compartir, evitando la creación de documentos de texto plano o formatos ATS convencionales.

## Datos clave
- **Proyecto**: SenseNova-Skills (nivel 1).
- **Tecnologías**: `sn-text-optimize` y `sn-image-generate` (basado en `sn-image-base`).
- **Arquitectura**: Agente principal (gestiona mensajes) + Agente trabajador (ejecuta lógica sin hablar con el usuario).
- **Entradas clave**: `resume_content` (obligatorio), `style`, `aspect_ratio` (por defecto 9:16), `image_size`.
- **Flujo de trabajo**: Validación de parámetros -> Creación de directorio temporal (`/tmp/openclaw`) -> Generación de prompt con `prompts/resume.md` -> Renderizado final.
- **Restricciones**: No edita textos planos, no parsea archivos subidos y comprime párrafos largos para el diseño visual.

## Etiquetas
#SenseNova #GeneraciónDeImágenes #CurrículumVisual #ArquitecturaDeAgentes

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-image-resume\SKILL.md`
