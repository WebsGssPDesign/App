---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-ppt-tools/references/capability-policy.md"
tags: [hecho]
---
# capability-policy.md

## Resumen
Este documento define las reglas de prioridad para seleccionar capacidades (búsqueda, generación) en el sistema PPT: primero se intenta usar herramientas nativas verificadas; si fallan o no existen, se recurre a scripts empaquetados (`sn-ppt-tools`); finalmente, si todo falla, se detiene la capacidad sin falsificar resultados. Su objetivo es garantizar la integridad de los datos y evitar comportamientos erróneos como la simulación automática de imágenes cuando estas no están disponibles.

## Datos clave
- **Jerarquía de selección**: Native (prioridad alta con verificación) > Bundled (scripts locales) > None (detener capacidad).
- **Ruta de herramientas**: `PPT_TOOLS_DIR = dirname(SKILL_DIR)/sn-ppt-tools`. No se escanean repositorios externos ni se verifica instalación manual.
- **Registro de estado**: Actualizar `task_pack.state.capabilities` con campos `source`, `status` y `last_error` (sin claves secretas).
- **Reglas de fallback prohibidas**: Nunca usar generación de imágenes para simular búsquedas, ni cambiar el modo creativo automáticamente si faltan capacidades visuales.
- **Manejo de errores**: Si no hay imagen, reorganizar el diseño sin dejar espacios vacíos o marcadores de posición; en Creative, marcar estado como `partial` y detener la salida.

## Etiquetas
#PPT #Capacidades #Fallback #SenseNova

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-ppt-tools\references\capability-policy.md`
