---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/mlops/models/audiocraft/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe AudioCraft, un framework de Meta para generar música y efectos sonoros a partir de texto utilizando los modelos MusicGen y AudioGen. Sirve como guía técnica para instalar las dependencias, configurar parámetros de generación y ejecutar inferencia mediante Python o HuggingFace Transformers.

## Datos clave
- **Proyecto**: AudioCraft (Meta/Orchestra Research).
- **Modelos principales**: `MusicGen` (música), `AudioGen` (efectos sonoros) y `EnCodec` (codificador de audio).
- **Tecnologías**: PyTorch, HuggingFace Transformers, torchaudio.
- **Variantes de modelos**: Desde 300M hasta 3.3B parámetros; incluye versiones para melodía condicionada (`melody`) y salida estéreo (`stereo-*`).
- **Comandos clave**: `pip install audiocraft`, `MusicGen.get_pretrained()`, `model.generate(descriptions)`.
- **Parámetros de generación**: `duration` (1-120s), `top_k`, `temperature`, `cfg_coef` para adherencia al texto.
- **Flujo de trabajo**: Cargar modelo -> Configurar parámetros -> Generar tokens con Transformer Decoder -> Decodificar a waveform con EnCodec.

## Etiquetas
#AudioGeneration #MusicGen #MLOps #PyTorch #MetaAI

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\mlops\models\audiocraft\SKILL.md`
