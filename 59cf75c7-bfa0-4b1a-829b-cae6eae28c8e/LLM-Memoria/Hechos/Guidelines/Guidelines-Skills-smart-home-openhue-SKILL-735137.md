---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/smart-home/openhue/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía documenta el uso de la línea de comandos OpenHue para controlar luces Philips Hue, escenas y habitaciones desde un terminal local. Su función principal es automatizar tareas de iluminación mediante comandos directos como encender/apagar, ajustar brillo o temperatura y aplicar modos predefinidos sin necesidad de una interfaz gráfica.

## Datos clave
- **Proyecto**: OpenHue CLI (versión 1.0.0).
- **Plataformas soportadas**: Linux, macOS y Windows.
- **Prerrequisitos**: Instalación del binario `openhue` (Linux) o vía Homebrew (macOS); conexión en red local con el puente Hue; pulsación física del botón de emparejamiento al inicio.
- **Comandos principales**: `get light/room/scene` para listar recursos y `set light/room/scene` para controlarlos.
- **Parámetros clave**: Uso de nombres exactos (sensibles a mayúsculas), valores de brillo (0-100) y temperatura en mireds (153-500).
- **Casos de uso**: Automatización con cron jobs, control por habitaciones completas o bombillas individuales.

## Etiquetas
#SmartHome #OpenHue #Automatización #IoT #Linux

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\smart-home\openhue\SKILL.md`
