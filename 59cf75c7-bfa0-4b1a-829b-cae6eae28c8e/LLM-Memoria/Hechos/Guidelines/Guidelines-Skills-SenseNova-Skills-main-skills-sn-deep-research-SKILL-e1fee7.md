---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-deep-research/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define una habilidad de "investigación profunda" para un sistema multi-agente, diseñada para orquestar análisis complejos mediante la coordinación de roles especializados. Su función principal es automatizar flujos de trabajo rigurosos que incluyen búsqueda de evidencia, verificación cruzada y generación de informes estructurados, activándose automáticamente ante palabras clave específicas o solicitudes de análisis exhaustivo.

## Datos clave
- **Proyecto**: `sn-deep-research` (Skill para investigación profunda).
- **Tecnologías**: Python 3, scripts de eventos (`progress_event.py`, `launch_workbench.py`), gestión de rutas absolutas (`${SKILL_DIR}`), variables de entorno (`.env`).
- **Decisión crítica**: El controlador solo gestiona el flujo; los roles leen archivos grandes directamente vía rutas absolutas para evitar inyección de contenido en mensajes.
- **Rutas y comandos importantes**:
  - Creación de directorio único: `mkdir -p "$report_dir"/sub_reports ...` con ID hexadecimal aleatorio.
  - Lanzamiento del WebUI: `python3 .../launch_workbench.py --deck-dir "{report_dir}" ...`.
  - Actualización de estado: `progress_event.py` con workflow `deep-research`.
- **Pasos clave**: Verificación obligatoria de capacidades Tier 1 (búsqueda, lectura) antes de iniciar; configuración de credenciales en `.env`; selección del "档位" (nivel de complejidad) al inicio.

## Etiquetas
#multi-agent #investigación #automatización #python #orquestación

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-deep-research\SKILL.md`
