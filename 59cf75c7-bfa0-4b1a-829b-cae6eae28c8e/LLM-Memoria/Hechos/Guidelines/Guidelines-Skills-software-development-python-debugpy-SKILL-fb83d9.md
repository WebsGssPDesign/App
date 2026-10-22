---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/software-development/python-debugpy/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento guía el uso de herramientas de depuración para Python, diferenciando entre `pdb` local y `debugpy` remoto. Sirve como referencia rápida para elegir la estrategia adecuada según si se necesita inspeccionar procesos interactivos, scripts existentes o servicios en ejecución que no pueden reiniciarse.

## Datos clave
- **Herramientas**: `breakpoint()` (local), `python -m pdb`, y `debugpy` (remoto/DAP).
- **Comandos pdb esenciales**: `n` (next), `s` (step into), `c` (continue), `p expr` (print), `b file:line` (breakpoint), `interact`.
- **Recetas de uso**: Ejecutar scripts con `-m pdb`, depurar pruebas pytest (`--pdb -p no:xdist`), y post-mortem en excepciones.
- **Debugpy remoto**: Patrones para escuchar puertos (`--listen`), lanzar módulos directamente o inyectarse en un PID existente (`--pid`).
- **Precaución**: `breakpoint()` debe eliminarse antes de commit; `debugpy` requiere instalación previa en el entorno objetivo.

## Etiquetas
#python #debugging #debugpy #pdb #hermes

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\software-development\python-debugpy\SKILL.md`
