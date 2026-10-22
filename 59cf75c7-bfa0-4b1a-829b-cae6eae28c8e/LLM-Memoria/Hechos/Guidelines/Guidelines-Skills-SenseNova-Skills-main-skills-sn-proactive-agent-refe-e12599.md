---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-proactive-agent/references/install/macos.md"
tags: [hecho]
---
# macos.md

## Resumen
Este documento detalla los pasos específicos para instalar y configurar el agente `sn-proactive-agent` en sistemas macOS, enfocándose en la gestión de entornos Python, dependencias como pipx y variables de entorno críticas. Su objetivo es garantizar una instalación segura que respete las versiones del sistema sin alterar configuraciones globales ni sobrescribir datos existentes.

## Datos clave
- **Requisitos**: Python 3.11 o superior; uso obligatorio de `pipx` para evitar conflictos con el intérprete por defecto.
- **Variables críticas**: `SNPA_PYTHON` (para fijar el intérpreter), `SNPA_PACKAGE`, `SNPA_HERMES_ROOT`, `SN_PROACTIVE_AGENT_DATA_ROOT`.
- **Configuración de entorno**: Uso de `export PATH` para activar comandos de pipx y definición de `SN_PROACTIVE_AGENT_SERVICE_URL` para la conexión con Hermes.
- **Rutas importantes**: Datos por defecto en `~/.sn-proactive-agent/`; interfaz accesible vía `http://127.0.0.1:8080/`.
- **Precauciones**: No modificar el Python del sistema; verificar existencia de archivos antes de instalar; no sobrescribir directorios de memoria previos (`~/.proactive-memory`).

## Etiquetas
#macOS #Python3.11 #pipx #SenseNova #Hermes

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-proactive-agent\references\install\macos.md`
