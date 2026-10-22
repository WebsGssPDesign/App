---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/mlops/huggingface-hub/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento es una guía de referencia para la interfaz de línea de comandos (`hf`) del Hugging Face Hub, diseñada para gestionar modelos, conjuntos de datos y repositorios. Sustituye al comando obsoleto `huggingface-cli` y permite automatizar tareas como descargas, autenticación, despliegue de endpoints y gestión de infraestructura mediante un conjunto de comandos centralizados.

## Datos clave
- **Proyecto:** Hugging Face Hub CLI (`hf`).
- **Instalación:** Script `curl -LsSf https://hf.co/cli/install.sh | bash -s`.
- **Autenticación:** Uso del entorno `HF_TOKEN` o flag `--token`; gestión de sesiones con `login`, `logout` y `list`.
- **Comandos principales:** `download`, `upload-large-folder`, `sync` para manejo de archivos; `repos create/delete/duplicate` para repositorios.
- **Funcionalidades especializadas:** Ejecución de SQL sobre datasets (`hf datasets sql`), gestión de Endpoints de inferencia y Jobs computacionales, y control de webhooks para automatización.
- **Flags globales:** `--format json` para salida máquina-legible y `-q` para silenciar salidas.

## Etiquetas
#mlops #huggingface #cli #devops

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\mlops\huggingface-hub\SKILL.md`
