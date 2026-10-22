---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/mlops/models/audiocraft/references/advanced-usage.md"
tags: [hecho]
---
# advanced-usage.md

## Resumen
Esta guía técnica detalla el flujo de trabajo avanzado para MusicGen y AudioCraft, cubriendo desde la preparación personalizada de conjuntos de datos hasta técnicas de entrenamiento escalable. Su objetivo es permitir a los usuarios afinar modelos con sus propios datos, implementar adaptaciones eficientes como LoRA y gestionar recursos multi-GPU para entrenamientos complejos.

## Datos clave
- **Proyecto**: AudioCraft (MusicGen).
- **Tecnologías**: PyTorch, Dora (gestión de experimentos), PEFT (LoRA), librosa.
- **Preparación de datos**: Script en Python que normaliza audio a 32kHz y mono, generando `metadata.json`.
- **Entrenamiento**: Uso de `dora run` con configuraciones YAML para afinamiento completo o LoRA (`r=8`, `lora_alpha=16`).
- **Escalabilidad**: Implementación de `DataParallel` y `DistributedDataParallel (DDP)` para múltiples GPUs.
- **Condiciones personalizadas**: Creación de condicionadores personalizados y extracción manual de características de croma con librosa.
- **Compresión**: Configuración de EnCodec con ajuste de ancho de banda (`set_target_bandwidth`) y codificación en streaming.

## Etiquetas
#MusicGen #AudioCraft #FineTuning #PyTorch #MLOps

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\mlops\models\audiocraft\references\advanced-usage.md`
