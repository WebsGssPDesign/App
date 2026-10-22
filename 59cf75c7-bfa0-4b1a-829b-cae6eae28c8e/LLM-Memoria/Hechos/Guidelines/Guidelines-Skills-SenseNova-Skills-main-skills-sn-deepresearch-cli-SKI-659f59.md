---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-deepresearch-cli/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define las directrices operativas para `sn-deepresearch-cli`, una herramienta de línea de comandos que automatiza investigaciones profundas, análisis de mercado y verificación de hechos. Su función principal es gestionar el ciclo completo del estudio: desde la validación del entorno y la instalación segura hasta la ejecución de tareas complejas mediante múltiples agentes (Hermes, Codex, Claude Code, OpenClaw) y la entrega de informes en diversos formatos.

## Datos clave
- **Proyecto:** `SenseNova-Skills-DeepResearch` (npm: `sensenova-skills-deepresearch`).
- **Instalación:** Uso exclusivo del paquete global vía npm; prohibido clonar repositorios o construir localmente salvo instrucciones explícitas del usuario.
- **Agentes/Harness:** Soporte para Hermes, Codex, Claude Code y OpenClaw con estrictos controles de autenticación y permisos de escritura en el workspace.
- **Flujo de trabajo:** Pre-checks de entorno -> Configuración de fuentes (Search/Camofox) -> Confirmación de parámetros (profundidad, formato, idioma) -> Ejecución (`quick` o `web`).
- **Seguridad:** Prohibido mostrar tokens, cookies o credenciales; manejo explícito de tiempos de espera y recuperación de fallos en capas de conexión.

## Etiquetas
#automatización #investigación #sensenova #cli-tools #seguridad

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-deepresearch-cli\SKILL.md`
