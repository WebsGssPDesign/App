---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/media/youtube-content/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía define una herramienta para extraer transcripciones de videos de YouTube y transformarlas en formatos estructurados como resúmenes, hilos o artículos. Sirve para procesar contenido audiovisual en Linux, macOS y Windows mediante un script automatizado que gestiona errores y adapta el idioma del texto.

## Datos clave
- **Proyecto**: `youtube-content` (herramienta de conversión de video a texto).
- **Tecnologías**: Python 3, entorno gestionado por `uv`, librería `youtube-transcript-api`.
- **Ruta del script**: `SKILL_DIR/scripts/fetch_transcript.py`.
- **Comandos principales**:
  - Instalación: `uv pip install youtube-transcript-api`
  - Ejecución JSON: `uv run python3 SKILL_DIR/scripts/fetch_transcript.py "URL"`
  - Texto plano: `... --text-only`
  - Con timestamps: `... --timestamps`
  - Selección de idioma: `... --language tr,en`
- **Flujo de trabajo**: Obtener transcripción -> Validar contenido -> Dividir si excede 50K caracteres -> Transformar al formato solicitado (capítulos, resumen, hilo, etc.) -> Verificar coherencia.

## Etiquetas
#YouTube #Automatización #Python #ProcesamientoDeTexto

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\media\youtube-content\SKILL.md`
