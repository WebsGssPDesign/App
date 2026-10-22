---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-update/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define la lógica de la habilidad `sn-update`, diseñada para sincronizar y actualizar el paquete de habilidades SenseNova (`sn-*`) en entornos como OpenClaw o hermes-agent. Su función principal es comparar las versiones locales con un repositorio upstream, realizar copias seguras antes de reemplazar archivos y gestionar los backups antiguos para mantener la integridad del sistema.

## Datos clave
- **Proyecto**: SenseNova-Skills (repositorio `OpenSenseNova/SenseNova-Skills`).
- **Agentes objetivo**: Se detecta automáticamente si existen las carpetas `~/.openclaw/skills/` o `~/.hermes/skills/`; si ambas existen, se solicita confirmación al usuario.
- **Mecanismo de comparación**: Prioriza el SHA del commit del árbol (`git log`) sobre etiquetas o campos YAML para determinar qué habilidades están desactualizadas.
- **Proceso de instalación**: Se mueven los archivos existentes a un bucket de backup con timestamp único y se realiza una copia recursiva real (sin enlaces simbólicos) desde la caché al directorio del agente.
- **Gestión de backups**: Se limita estrictamente la retención a los 3 buckets más recientes, eliminando los antiguos tras cada ejecución.
- **Comandos clave**: `git clone --filter=blob:none`, `sparse-checkout`, y la escritura manual del archivo `.sn-version` con el nuevo SHA.

## Etiquetas
#SenseNova #Automatización #GestiónDeVersiones #OpenClaw

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-update\SKILL.md`
