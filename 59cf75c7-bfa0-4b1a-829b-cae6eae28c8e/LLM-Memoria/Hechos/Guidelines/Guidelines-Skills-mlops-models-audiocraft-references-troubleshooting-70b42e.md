---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/mlops/models/audiocraft/references/troubleshooting.md"
tags: [hecho]
---
# troubleshooting.md

## Resumen
Esta guía técnica resuelve errores comunes al instalar y ejecutar AudioCraft, una librería para generación de audio. Proporciona soluciones paso a paso para problemas de instalación (como dependencias faltantes o versiones incompatibles), carga de modelos con limitaciones de memoria y fallas durante la generación de audio.

## Datos clave
- **Proyecto**: AudioCraft (MusicGen, AudioGen).
- **Errores críticos**: `ModuleNotFoundError`, `ffmpeg not found`, desajuste CUDA/PyTorch, `OutOfMemoryError`.
- **Soluciones técnicas**: Instalar desde PyPI o GitHub; usar comandos específicos de `pip` para versiones de CUDA 12.1 y 11.8; configurar variables de entorno (`AUDIOCRAFT_USE_XFORMERS=0`, `HF_HOME`).
- **Parámetros de generación**: Ajustar `duration`, `top_k`, `temperature` y `cfg_coef`; normalizar amplitud silenciosa.
- **Modelos específicos**: Diferenciar entre `MusicGen` (música), `AudioGen` (sonidos) y variantes `melody` o `stereo`.

## Etiquetas
#audiocraft #mlops #pytorch #troubleshooting

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\mlops\models\audiocraft\references\troubleshooting.md`
