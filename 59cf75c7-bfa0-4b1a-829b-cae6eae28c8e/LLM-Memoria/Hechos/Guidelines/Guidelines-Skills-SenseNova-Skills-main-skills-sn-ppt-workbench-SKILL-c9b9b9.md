---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-ppt-workbench/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía detalla el uso de la interfaz web para editar presentaciones HTML existentes en el proyecto SenseNova, permitiendo inspección y modificación visual sin regenerar diapositivas. Su función principal es iniciar o reutilizar un entorno de trabajo (Workbench) que gestiona la edición a través de URLs locales o remotas, priorizando conexiones seguras como Hermes o Canvas cuando están disponibles.

## Datos clave
- **Proyecto**: SenseNova-Skills (herramienta `sn-ppt-workbench`).
- **Tecnologías**: Python (`open_workbench.py`), Node.js (launcher), Hermes, OpenClaw, Codex, Box Agent.
- **Comandos importantes**:
  - Inicio: `python3 $SKILL_DIR/scripts/open_workbench.py --deck-dir "<ruta>"`.
  - Lanzamiento directo: `node <launcher> start --deck-dir "<ruta>"` (requiere subcomando).
  - Reinicio seguro: Ejecutar `stop` antes de `start` para evitar código obsoleto.
- **Reglas críticas**: No editar archivos HTML manualmente; no ejecutar scripts de generación (`sn-ppt-entry`, etc.).
- **Configuración red**: Usar `WORKENCH_HOST=0.0.0.0` para acceso remoto/LAN en lugar del localhost por defecto.

## Etiquetas
#SenseNova #PresentacionesHTML #Automatización #DevOps

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-ppt-workbench\SKILL.md`
