---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/INSTALL_CN.md"
tags: [hecho]
---
# INSTALL_CN.md

## Resumen
Este documento guía la instalación y configuración de los agentes OpenClaw o hermes-agent para integrar las habilidades de SenseNova en Windows, macOS y Linux. Permite crear un agente impulsado por habilidades utilizando modelos específicos de SenseNova mediante una API compatible con OpenAI.

## Datos clave
- **Agentes**: Se elige entre OpenClaw (requiere Node.js 24+) o hermes-agent; ambos soportan las mismas habilidades.
- **Configuración API**: Se requiere obtener un API Key y usar los endpoints `token.sensenova.ai/v1` (global) o `token.sensenova.cn/v1` (China), con el modelo `sensenova-6.8-flash-lite`.
- **Instalación rápida**: Agent Pack es una herramienta opcional que automatiza todo el proceso, incluyendo la carga de habilidades en el directorio `skills/`.
- **Preparación por plataforma**: Windows exige WSL2 (`wsl --install`); macOS necesita Xcode CLT y Homebrew; Linux requiere `curl` y `git`.
- **Comandos críticos**: `openclaw onboard --install-daemon`, `nvm install 24`, y scripts de instalación como `curl -fsSL https://openclaw.ai/install.sh | bash`.

## Etiquetas
#OpenClaw #SenseNova #hermes-agent #WSL2 #AgentPack

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\INSTALL_CN.md`
