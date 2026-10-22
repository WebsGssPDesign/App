---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/INSTALL.md"
tags: [hecho]
---
# INSTALL.md

## Resumen
Esta guía detalla cómo instalar y configurar los agentes OpenClaw o hermes-agent en Windows, macOS y Linux para integrarlos con la plataforma SenseNova. El objetivo es establecer un entorno de agente impulsado por habilidades funcional, permitiendo ejecutar tareas automatizadas utilizando modelos específicos de SenseNova sin necesidad de modificar el código de las habilidades.

## Datos clave
- **Agentes compatibles**: OpenClaw o hermes-agent (ambos siguen la convención Agent Skills).
- **Configuración SenseNova**: Se requiere una API Key y un endpoint según la región (International: `token.sensenova.ai`, China: `token.sensenova.cn`). Modelo recomendado: `sensenova-6.8-flash-lite`.
- **Instalación rápida**: Uso de "Agent Pack" para instalar agentes, configurar el proveedor LLM personalizado y cargar habilidades automáticamente sin pasos manuales.
- **Requisitos por plataforma**: Windows requiere WSL2; macOS necesita Xcode CLT y Homebrew; Linux no tiene requisitos previos manuales.
- **Comandos importantes**: Para Linux, `chmod +x AgentPack-*-linux.sh && ./AgentPack-*-linux.sh`.

## Etiquetas
#OpenClaw #hermes-agent #SenseNova #Automatización #WSL2

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\INSTALL.md`
