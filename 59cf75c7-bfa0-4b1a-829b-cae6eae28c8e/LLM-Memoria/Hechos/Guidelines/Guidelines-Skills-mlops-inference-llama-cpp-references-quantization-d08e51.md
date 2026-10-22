---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/mlops/inference/llama-cpp/references/quantization.md"
tags: [hecho]
---
# quantization.md

## Resumen
Esta guía detalla los formatos de cuantización GGUF para modelos Llama, estableciendo **Q4_K_M** como el equilibrio óptimo entre calidad y velocidad. Explica cómo convertir modelos desde Hugging Face a GGUF, seleccionar la precisión adecuada según el uso (ej. código vs chat) y optimizar resultados mediante matrices de importancia (`imatrix`).

## Datos clave
- **Formato recomendado**: Q4_K_M (mejor balance), Q5_K_M/M6_K para mayor precisión en generación de código o tareas técnicas.
- **Conversión**: `hf download` seguido de `convert_hf_to_gguf.py` y `llama-quantize`.
- **Comandos útiles**: `llama-perplexity` para validar calidad, `llama-imatrix` para calibración en cuantizaciones bajas (Q3 o inferior).
- **Selección de modelos**: Usar filtros `?local-app=llama.cpp` en Hugging Face para ver compatibilidad hardware y tamaños exactos.
- **Escalado**: Modelos 70B requieren Q3_K_M o Q4_K_S para ejecutarse en hardware consumidor; los de 7B caben con Q2_K a Q8_0 según RAM disponible.

## Etiquetas
#MLOps #LLaMA #GGUF #Cuantización #Inferencia

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\mlops\inference\llama-cpp\references\quantization.md`
