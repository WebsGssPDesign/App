---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-ppt-dazzle/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía define el flujo de trabajo para crear presentaciones HTML dinámicas y visuales ("dazzle") dentro del proyecto SenseNova-Skills. Sirve como protocolo estricto que obliga a ejecutar habilidades previas (`entry` y `story`) antes de generar contenido, asegurando que la estructura base sea respetada sin alteraciones ni invenciones de datos.

## Datos clave
- **Proyecto**: SenseNova-Skills (Skill: sn-ppt-dazzle).
- **Prerrequisitos obligatorios**: Ejecución previa de `sn-ppt-entry` y `sn-ppt-story`. Requiere archivos existentes: `task_pack.json`, `info_pack.json` y `outline.md`.
- **Restricciones estrictas**: No se pueden crear nuevas carpetas, ni omitir pasos previos. El contenido (`outline.md`) es sagrado; no se permite añadir, borrar o reordenar páginas ni inventar datos.
- **Tecnologías permitidas**: Three.js r128, GSAP, ECharts, D3, Google Fonts (CDN). CSS/JS deben estar incrustados. Imágenes solo desde carpeta local `assets/`.
- **Flujo de trabajo (6 fases)**:
  1. Leer `outline.md` y definir estilo/familia visual.
  2. Generar `plan.md` con diseño, paleta y esquema de páginas.
  3. Crear imágenes si es necesario (validación estricta).
  4. Escribir esqueleto HTML (`deck.html`) vacío excepto portada.
  5. Rellenar página por página con ciclo: editar → renderizar → verificar visualmente.
- **Comandos de renderizado**: `python "$SKILL_ROOT/scripts/render_deck.py" ... --page N` o `--all`.
- **Resolución**: Salida única en `<DECK_DIR>/deck.html` (1280×700).

## Etiquetas
#SenseNova #HTML_Dinámico #Presentaciones #Flujo_Trabajo

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-ppt-dazzle\SKILL.md`
