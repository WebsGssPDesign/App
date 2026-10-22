---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-proactive-agent/references/install/overview.md"
tags: [hecho]
---
# overview.md

## Resumen
Este documento detalla el flujo de instalación y ejecución del agente `sn-proactive-agent`, estableciendo requisitos previos, procedimientos de descarga segura desde GitHub Releases y validación mediante herramientas como `pipx` y `doctor`. Su objetivo es guiar a los administradores para desplegar la versión 0.1.3 correctamente en macOS, Windows o WSL, asegurando la integridad del paquete y la compatibilidad con el entorno Hermes antes de iniciar servicios web y pruebas de diálogo.

## Datos clave
- **Versión actual**: `v0.1.3` (disponible solo en GitHub Releases, no en PyPI).
- **Paquete de instalación**: `sn_proactive_agent-0.1.3-py3-none-any.whl`.
- **Herramientas críticas**: `gh release`, `pipx install --python "$SNPA_PYTHON"`, `sn-proactive-agent doctor`.
- **Validación obligatoria**: Verificación de SHA256 del archivo `.whl` contra el archivo `SHA256SUMS`.
- **Comandos de verificación**: `sn-proactive-agent --version`, `sn-proactive-agent serve --web-only`.
- **Gestión de datos**: Datos almacenados en `.sn-proactive-agent/`; compatibilidad con directorios antiguos `.proactive-memory/`.
- **Desinstalación**: Requiere limpieza manual del Connector antes de ejecutar `pipx uninstall sn-proactive-agent`.

## Etiquetas
#SenseNova #ProactiveAgent #Instalación #DevOps

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-proactive-agent\references\install\overview.md`
