---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/media/songsee/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe **songsee**, una herramienta de línea de comandos escrita en Go para generar espectrogramas y visualizaciones multigrilla de características de audio (como MFCC, cromática y loudness). Sirve para analizar archivos de sonido, depurar síntesis musical o documentar pipelines de procesamiento auditivo mediante la exportación de imágenes detalladas.

## Datos clave
- **Proyecto**: songsee (versión 1.0.0, licencia MIT).
- **Tecnologías**: Go (requisito principal), soporte opcional para `ffmpeg` en formatos no nativos.
- **Comandos y pasos**:
    - Instalación: `go install github.com/steipete/songsee/cmd/songsee@latest`.
    - Espectrograma básico: `songsee track.mp3`.
    - Visualización multigrilla (ejemplo): `songsee track.mp3 --viz spectrogram,mel,chroma,hpss,selfsim,loudness,tempogram,mfcc,flux`.
    - Extracción de segmento temporal: `--start 12.5 --duration 8`.
- **Opciones importantes**: `--format` (jpg/png), `--style` (paletas de color), `-o` para ruta de salida y `cat archivo | songsee` para entrada desde stdin.

## Etiquetas
#audio-analysis #go-tools #spectrogram

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\media\songsee\SKILL.md`
