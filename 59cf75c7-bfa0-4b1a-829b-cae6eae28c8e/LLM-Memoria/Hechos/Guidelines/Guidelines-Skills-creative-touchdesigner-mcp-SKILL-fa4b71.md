---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/touchdesigner-mcp/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este archivo documenta la integración de TouchDesigner con el servidor MCP de twozero, permitiendo controlar nodos, parámetros y conexiones en tiempo real mediante 36 herramientas nativas. Su objetivo es automatizar flujos creativos y generativos sin necesidad de licencias comerciales, ofreciendo una arquitectura segura que evita errores comunes al interactuar con la API de TouchDesigner.

## Datos clave
- **Proyecto:** Integración `touchdesigner-mcp` (versión 1.1.0) para control remoto de instancias de TouchDesigner.
- **Tecnologías:** Hermes Agent, MCP (Streamable HTTP), Python, GLSL, codecs ProRes/mjpa.
- **Reglas críticas:** Nunca adivinar nombres de parámetros; usar siempre `td_get_par_info` antes de configurar; evitar rutas absolutas en scripts.
- **Flujo de trabajo:** Descubrimiento (`td_get_hints`, `td_get_focus`) → Creación segura (`td_create_operator`) → Configuración (`td_set_operator_pars`) → Enrutamiento (Python) → Verificación.
- **Comandos de instalación:** Ejecutar `setup.sh` para descargar el plugin y configurar Hermes, seguido de pasos manuales en la interfaz de TouchDesigner (arrastrar `.tox`, activar MCP).
- **Herramientas principales:** `td_execute_python`, `td_create_operator`, `td_set_operator_pars`, `td_get_errors`.

## Etiquetas
#TouchDesigner #MCP #CreativeCoding #Automation #RealTimeVisuals

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\touchdesigner-mcp\SKILL.md`
