---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/comfyui/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este archivo define una guía técnica para generar imágenes, video y audio utilizando ComfyUI mediante la herramienta oficial `comfy-cli` y APIs REST/WebSocket. Sirve como referencia para instalar el entorno, gestionar nodos y modelos, ejecutar flujos de trabajo con inyección de parámetros y monitorear tareas en tiempo real.

## Datos clave
- **Proyecto**: Skill técnico para ComfyUI (versión 5.1.0).
- **Tecnologías**: Python (`comfy-cli`, `pipx`), APIs REST/WebSocket, modelos como Stable Diffusion, Flux y Wan.
- **Scripts principales**: `hardware_check.py` (detección de hardware local vs nube), `comfyui_setup.sh` (instalación automática), `run_workflow.py` (ejecución con parámetros) y `ws_monitor.py` (visualización en vivo).
- **Flujo de trabajo**: Verificar entorno → Exportar flujo en formato API JSON → Extraer esquema de parámetros (`extract_schema.py`) → Ejecutar e inyectar datos.
- **Decisión crítica**: Siempre ejecutar `hardware_check.py` antes de decidir entre instalación local o uso de Comfy Cloud.

## Etiquetas
#comfyui #generative-ai #python #workflows

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\comfyui\SKILL.md`
