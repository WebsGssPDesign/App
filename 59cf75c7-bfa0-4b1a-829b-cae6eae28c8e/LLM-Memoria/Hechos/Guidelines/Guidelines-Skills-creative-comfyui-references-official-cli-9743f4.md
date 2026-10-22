---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/comfyui/references/official-cli.md"
tags: [hecho]
---
# official-cli.md

## Resumen
Este documento detalla la referencia oficial de comandos para `comfy-cli`, una herramienta diseñada para automatizar la instalación, configuración y gestión del entorno ComfyUI. Sirve como guía principal para usuarios que necesitan desplegar servidores, administrar nodos personalizados o gestionar modelos (checkpoints, LoRAs) mediante línea de comandos sin intervención manual constante.

## Datos clave
- **Instalación preferida**: `pipx install comfy-cli` (entorno aislado).
- **Gestión de workspace**: Prioriza `--workspace`, luego `--recent`, `--here` o rutas por defecto del sistema operativo.
- **Comandos principales**:
  - `comfy install`: Instala ComfyUI y Manager, soportando GPUs NVIDIA, AMD (ROCm), Apple Silicon y CPU.
  - `comfy launch`: Inicia el servidor en primer plano o fondo con opciones de red (`--listen`) y memoria (`--lowvram`).
  - `comfy node`: Gestiona nodos personalizados vía ComfyUI-Manager (instalar, actualizar, bisectar errores).
  - `comfy model`: Descarga modelos desde URLs externas a carpetas específicas del workspace.
- **Resolución de dependencias**: Opciones `--fast-deps` (uv nativo) y `--uv-compile` (unified resolver v4.1+).

## Etiquetas
#ComfyUI #CLI #Automatización #MachineLearning

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\comfyui\references\official-cli.md`
