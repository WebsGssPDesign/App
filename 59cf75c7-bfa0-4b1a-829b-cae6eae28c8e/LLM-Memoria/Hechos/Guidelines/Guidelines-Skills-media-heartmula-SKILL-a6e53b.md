---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/media/heartmula/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
HeartMuLa es un conjunto de modelos de código abierto para generar música completa a partir de letras y etiquetas, funcionando como alternativa local a Suno. Incluye componentes clave como el modelo generador HeartMuLa, el códec de alta fidelidad HeartCodec y herramientas para transcripción y alineación audio-texto.

## Datos clave
- **Proyecto**: heartlib (GitHub: HeartMuLa/heartlib).
- **Tecnologías**: Apache-2.0, PyTorch 2.4.1, `torchtune`, Hugging Face (`hf download`).
- **Requisitos de hardware**: Mínimo 8GB VRAM con `--lazy_load true`; recomendado 16GB+. Soporte multi-GPU vía `--mula_device cuda:0 --codec_device cuda:1`.
- **Pasos críticos**:
    - Crear entorno virtual Python 3.10 (`uv venv`).
    - Actualizar dependencias conflictivas (`datasets`, `transformers`).
    - Parchear código fuente: re-inicialización de RoPE caches en `modeling_heartmula.py` y uso de `ignore_mismatched_sizes=True` al cargar HeartCodec.
- **Comandos principales**: `python ./examples/run_music_generation.py` con parámetros como `--lyrics`, `--tags`, `--save_path`.
- **Formato de entrada**: Letras con etiquetas estructurales `[Verse]`, `[Chorus]`; tags separados por comas sin espacios.

## Etiquetas
#músicaIA #HeartMuLa #generaciónAudio #openSource

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\media\heartmula\SKILL.md`
