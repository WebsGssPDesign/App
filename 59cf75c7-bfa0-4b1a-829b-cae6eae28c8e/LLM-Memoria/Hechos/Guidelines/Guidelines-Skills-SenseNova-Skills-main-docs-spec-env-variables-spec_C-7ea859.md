---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/docs/spec/env-variables-spec_CN.md"
tags: [hecho]
---
# env-variables-spec_CN.md

## Resumen
Este documento define la arquitectura de configuración mediante variables de entorno para las habilidades de SenseNova-Skills, priorizando una experiencia "cero configuración" con valores por defecto robustos. Permite a los usuarios iniciar rápidamente con un mínimo de parámetros mientras ofrece capas granulares para personalizar modelos y endpoints específicos según la capacidad (texto, visión o generación de imágenes).

## Datos clave
- **Variables mínimas**: `SN_API_KEY` es el único obligatorio; `SN_BASE_URL`, `SN_CHAT_MODEL` y `SN_IMAGE_GEN_MODEL` tienen valores por defecto.
- **Jerarquía de capacidades**: Text/Vision comparten un runtime (`SN_CHAT_*`), mientras que Image Gen tiene uno independiente (`SN_IMAGE_GEN_*`).
- **Cadena de retroceso (Fallback)**: Las variables específicas (`SN_TEXT_*`, `SN_VISION_*`) heredan valores de las grupales (`SN_CHAT_*`) y luego de las globales (`SN_*`), terminando en los defaults internos.
- **Modelos por defecto**: `sensenova-6.8-flash-lite` para chat/visión y `sensenova-u1.5-lite` para generación de imágenes.
- **URL base predeterminada**: `https://token.sensenova.cn/v1`.

## Etiquetas
#SenseNova #Configuración #VariablesDeEntorno #IA #DocumentaciónTécnica

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\docs\spec\env-variables-spec_CN.md`
