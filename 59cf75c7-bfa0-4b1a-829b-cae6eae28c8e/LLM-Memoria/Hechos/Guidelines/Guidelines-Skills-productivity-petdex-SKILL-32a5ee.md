---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/productivity/petdex/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía describe la habilidad de Petdex para instalar y gestionar mascotas animadas que reaccionan a las actividades del agente Hermes en entornos CLI, TUI y escritorio. Su función principal es permitir al usuario navegar por una galería pública, seleccionar un mascota activa y diagnosticar problemas de renderizado gráfico sin generar sprites manualmente.

## Datos clave
- **Proyecto**: Petdex (integrado en Hermes Agent).
- **Comandos principales**: `hermes pets list`, `install <slug> --select`, `show`, `doctor`.
- **Configuración**: Se gestiona mediante `config.yaml` bajo la sección `display.pet` (propiedades: `enabled`, `slug`, `render_mode`, `scale`).
- **Requisitos técnicos**: Acceso a red para el manifiesto, dependencia de Pillow y terminales gráficos (kitty, Ghostty) o soporte Sixel/Unicode.
- **Rutas de instalación**: `<HERMES_HOME>/pets/<slug>/` (diferente al CLI npm estándar).

## Etiquetas
#hermes #petdex #productivity #automation #cli

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\productivity\petdex\SKILL.md`
