---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/galaxy-io/tempo"
tema: "Temporal Workflow Observability"
tags: [web]
---
# galaxy-io/tempo

## Resumen
Tempo es una interfaz de usuario en terminal (TUI) diseñada para inspeccionar y controlar flujos de trabajo de Temporal. Utiliza un sistema de teclas para navegar, gestionar nombres de espacio y ejecutar acciones como cancelar o señalizar flujos sin necesidad de ratón.

## Datos clave
- **Comandos de instalación**: `go install github.com/galaxy-io/tempo/cmd/tempo@latest`, `brew install galaxy-io/tap/tempo`.
- **Configuración principal**: Archivo `~/.config/tempo/config.yaml` con soporte para múltiples perfiles (TLS, codecs).
- **Teclas principales**: `j/k` (navegación), `T` (seleccionar tema), `P` (cambiar perfil), `c/t/s/d` (cancelar/terminar/señalar/comparar flujos).
- **Temas disponibles**: 26 temas integrados, incluyendo TokyoNight, Catppuccin, Dracula y Nord.
- **Requisitos**: Go 1.21+ y servidor Temporal activo.

## Etiquetas
#Temporal #TUI #DevTools #Go #WorkflowManagement

Fuente: https://github.com/galaxy-io/tempo
