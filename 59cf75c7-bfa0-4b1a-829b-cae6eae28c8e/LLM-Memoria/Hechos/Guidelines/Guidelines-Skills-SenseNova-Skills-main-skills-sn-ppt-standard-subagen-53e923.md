---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-ppt-standard/subagents/slide.md"
tags: [hecho]
---
# slide.md

## Resumen
Esta guía define el protocolo operativo para un agente especializado en la creación de diapositivas HTML dentro del sistema SenseNova. Su función es generar código visualmente fiel a los planes de diseño, asegurando que solo la información final para el público aparezca en pantalla y eliminando cualquier dato interno o metainformación.

## Datos clave
- **Proyecto**: Sistema de generación de presentaciones (SenseNova/Box-Agent).
- **Tecnologías**: HTML, CSS (`base.css`), Python (`render.py`, `deck.py`).
- **Reglas críticas**: Prohibido incluir fuentes, rutas internas o estados de producción en el HTML; las imágenes deben ser assets oficiales del catálogo sin recortes falsos.
- **Flujo de trabajo**: El agente escribe la primera versión HTML, devuelve los números de página y espera a que el padre renderice y verifique visualmente (PNG) antes de realizar correcciones iterativas limitadas a una ronda.
- **Comandos clave**: `python "$SKILL_ROOT/scripts/render.py" --batch "$DECK_DIR" --pages NN`.

## Etiquetas
#SenseNova #DesarrolloFrontend #ControlDeCalidad #DocumentaciónTécnica

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-ppt-standard\subagents\slide.md`
