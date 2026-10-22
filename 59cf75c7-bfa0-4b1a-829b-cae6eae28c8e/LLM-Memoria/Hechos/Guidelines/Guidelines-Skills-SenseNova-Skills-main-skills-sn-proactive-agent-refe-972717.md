---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-proactive-agent/references/install/windows.md"
tags: [hecho]
---
# windows.md

## Resumen
Este documento detalla los pasos específicos para instalar el agente `sn-proactive-agent` en entornos nativos de PowerShell y WSL, diferenciando las rutas de ejecución, variables de entorno y verificaciones de versiones. Su objetivo es guiar al usuario a través del despliegue sin mezclar configuraciones entre sistemas operativos, asegurando que Python 3.11+ y pipx estén correctamente configurados antes de instalar los paquetes.

## Datos clave
- **Entornos**: Diferenciación estricta entre PowerShell (Windows) y WSL (Linux). No se deben mezclar rutas ni datos entre ambos.
- **Requisitos**: Python 3.11 o superior; instalación de `pipx` vía el intérprete específico (`py -m pip install` en Windows, `pipx ensurepath` en Linux).
- **Variables críticas**: `$SNPA_PYTHON`, `$SNPA_PACKAGE`, `$SNPA_HERMES_ROOT`, `$env:SN_PROACTIVE_AGENT_SERVICE_URL`.
- **Comandos de verificación**: `Get-Command py, python, pipx`, `wsl --list --verbose`, `python3 --version`.
- **Rutas y datos**: Datos por defecto en `%USERPROFILE%\.sn-proactive-agent` (Windows) o `~/.sn-proactive-agent/` (WSL). El archivo `.whl` y el directorio de Hermes deben existir antes de la instalación.
- **Precauciones**: No usar IDs de sesión de ejemplo; no exponer servicios a internet automáticamente; verificar que los paths sean literales en PowerShell.

## Etiquetas
#instalación-windows #WSL #Python311 #sn-proactive-agent

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-proactive-agent\references\install\windows.md`
