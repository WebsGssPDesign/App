---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/marketing-skill-claude-marketing-skill-builder-uzp891/state/content-calendar.md"
tags: [hecho]
---
# content-calendar.md

## Resumen
Este archivo actúa como un calendario de contenidos y registro histórico permanente para una estrategia de marketing, donde las filas se acumulan en lugar de eliminarse. Su función principal es indexar publicaciones futuras y pasadas mediante etiquetas breves, mientras que el contenido real reside en archivos separados, asegurando la integridad del flujo de trabajo mediante reglas estrictas de aprobación humana antes del envío.

## Datos clave
- **Proyecto**: Sistema de gestión de calendario de contenidos (`marketing-skill`).
- **Tecnologías/Flujo**: `content-calendar`, `full-pipeline` (Stage 4 fallback), `publish-pipeline`.
- **Reglas críticas**: Separación de deberes; solo `publish-pipeline` puede cambiar el estado a `Approved` tras confirmación humana explícita. Los otros componentes solo pueden escribir estados hasta `Ready for Approval`.
- **Estructura de datos**: El archivo es un índice, no el almacén de contenido. La columna `Notes` debe contener la ruta exacta al archivo del post (ej. `state/posts/<date>-<platform>.md`).
- **Formato**: Uso obligatorio de `\|` para escapar caracteres y evitar corrupción de columnas; textos largos deben ir en los archivos de posts, no en las celdas.

## Etiquetas
#calendario-de-contenidos #gestión-de-publicaciones #flujo-trabajo-marketing #separación-de-deberes

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\marketing-skill-claude-marketing-skill-builder-uzp891\state\content-calendar.md`
