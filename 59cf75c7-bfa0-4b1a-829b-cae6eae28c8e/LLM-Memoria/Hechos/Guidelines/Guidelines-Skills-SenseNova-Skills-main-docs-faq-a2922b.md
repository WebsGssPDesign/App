---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/docs/faq.md"
tags: [hecho]
---
# faq.md

## Resumen
Este documento es un manual de preguntas frecuentes para solucionar errores comunes en la configuración y ejecución de las habilidades de SenseNova Skills. Proporciona soluciones prácticas para problemas de compatibilidad con versiones de software, tiempos de espera en generación de presentaciones, claridad textual en infografías y limitaciones de cuota del plan gratuito.

## Datos clave
- **Problema de compatibilidad:** El error `400 role` en Claude Code v2.1.154+ se soluciona bajando a la versión 2.1.153 usando `npm install -g @anthropic-ai/claude-code@2.1.153`.
- **Desactivar actualizaciones:** Se debe exportar `DISABLE_AUTOUPDATER=1` o configurarlo en el campo `env` de cc-switch para evitar sobrescrituras automáticas.
- **Tiempos de espera (Timeouts):** Para PPT complejos, aumentar los límites a 600 segundos mediante las variables `SN_TEXT_TIMEOUT`, `SN_VISION_TIMEOUT` y `SN_CHAT_TIMEOUT`.
- **Infografías en chino:** Mejorar la claridad textual estableciendo `max_rounds=3` para activar la revisión visual (VLM).
- **Modelos recomendados:** Usar `deepseek-v4-pro` en lugar de `SenseNova 6.7 Flash-Lite` para tareas complejas de razonamiento y codificación.
- **Límites de cuota:** El plan gratuito permite 1,500 llamadas cada 5 horas; el acceso a modelos como `sensenova-u1-fast` requiere usar herramientas específicas de generación de imágenes.

## Etiquetas
#SenseNova #FAQ #DevOps #LLM #Troubleshooting

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\docs\faq.md`
