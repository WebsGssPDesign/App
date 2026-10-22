---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/docs/faq_CN.md"
tags: [hecho]
---
# faq_CN.md

## Resumen
Este documento recopila soluciones a problemas frecuentes de integración y ejecución en SenseNova Skills, abordando errores de compatibilidad con Claude Code, tiempos de espera en generación de PPTs y limitaciones de cuota. Sirve como guía práctica para usuarios que enfrentan fallos técnicos o restricciones de servicio al utilizar modelos locales y herramientas de IA.

## Datos clave
- **Problema 400 (role error):** Causado por Claude Code v2.1.154+. Solución: volver a la versión 2.1.153 (`npm install -g @anthropic-ai/claude-code@2.1.153`) y desactivar actualizaciones automáticas con `DISABLE_AUTOUPDATER=1`.
- **Tiempo de espera PPT:** Aumentar `SN_TEXT_TIMEOUT`, `SN_VISION_TIMEOUT` o `SN_CHAT_TIMEOUT` a 600 segundos para evitar cortes en páginas complejas.
- **Calidad de infografías:** Usar `max_rounds=3` y `output_mode=verbose` para activar revisión VLM y mejorar claridad del texto chino.
- **Rendimiento y estabilidad:** Cambiar a `deepseek-v4-pro` si SenseNova 6.7 Flash-Lite falla en tareas complejas o código largo.
- **Límites de cuota (429):** Límite gratuito de 1,500 llamadas cada 5 horas; el servicio se recupera automáticamente tras la ventana deslizante.
- **Modelos:** `sensenova-6.8-flash-lite` y `sensenova-u1-fast`. Nota: U1 Fast requiere herramientas específicas (`sn-image-generate`) y no el endpoint de chat estándar.

## Etiquetas
#SenseNova #ClaudeCode #IA #Troubleshooting #API

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\docs\faq_CN.md`
