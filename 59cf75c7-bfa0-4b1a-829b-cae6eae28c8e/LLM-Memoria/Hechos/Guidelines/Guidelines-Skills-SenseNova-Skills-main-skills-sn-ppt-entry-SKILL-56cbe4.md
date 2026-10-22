---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-ppt-entry/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define la lógica de entrada para generar presentaciones PPT en el proyecto SenseNova, actuando como un router que gestiona tareas desde cero o edita archivos existentes. Su función es coordinar la investigación, seleccionar parámetros de diseño y enrutar el flujo hacia módulos específicos (standard, dazzle o creative) basándose en las necesidades del usuario.

## Datos clave
- **Proyecto**: SenseNova-Skills (módulo `sn-ppt-entry`).
- **Tecnologías**: Python scripts absolutos (`<ENTRY_SKILL_ROOT>/scripts/`), JSON para estado (`task_pack.json`, `info_pack.json`), Markdown para estructuras.
- **Decisiones de flujo**: Se recomienda automáticamente entre tres niveles de profundidad (draft, standard, deep) y estilos visuales; se priorizan las capacidades nativas del host sobre herramientas empaquetadas.
- **Rutas y comandos**: Uso estricto de `pwd -P` para definir el directorio raíz único (`<workspace_root>/ppt_decks/`). Prohibido usar `$SKILL_DIR` o rutas relativas.
- **Pasos importantes**: 1) Validar si es edición (ruteo a `sn-ppt-edit`) o nueva creación. 2) Crear directorio y escribir `task_pack.json`. 3) Ejecutar investigación externa solo en modos standard/deep. 4) Llamar a `sn-ppt-story` para generar el esquema antes de la producción final.

## Etiquetas
#SenseNova #GeneraciónPPT #Automatización #FlujoDeTrabajo

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-ppt-entry\SKILL.md`
