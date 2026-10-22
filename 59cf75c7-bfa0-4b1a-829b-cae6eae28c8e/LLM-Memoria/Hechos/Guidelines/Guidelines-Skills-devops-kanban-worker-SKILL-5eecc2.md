---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/devops/kanban-worker/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento detalla las mejores prácticas, trampas comunes y casos de borde para los trabajadores Kanban en el sistema Hermes. Su objetivo es guiar a los agentes sobre cómo manejar espacios de trabajo, aislar inquilinos y estructurar correctamente los informes finales (`kanban_complete`) o bloqueos por revisión humana.

## Datos clave
- **Gestión de espacio**: Diferencia entre `scratch` (temporal), `dir:<path>` (persistente compartido) y `worktree` (Git). Para Git, usar `git worktree add` si no existe el directorio.
- **Aislamiento de inquilinos**: Si `$HERMES_TENANT` está definido, prefiere memorias con prefijo del inquilino (ej: `business-a:`) para evitar fugas de contexto.
- **Manejo de revisiones**: Usar `kanban_block` con el prefijo `review-required:` y detalles en comentarios JSON cuando el código necesita aprobación humana antes de fusionarse.
- **Entregables (`artifacts`)**: Pasar rutas absolutas a archivos finales (PDFs, imágenes) directamente al completar la tarea para que se adjuten automáticamente; evitar rutas relativas o archivos intermedios.
- **Estructura de datos**: El parámetro `metadata` debe ser estrictamente estructurado (diccionarios/JSON) para facilitar el procesamiento automático por otros agentes o sistemas.

## Etiquetas
#devops #kanban #hermes #automatización #mejores-prácticas

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\devops\kanban-worker\SKILL.md`
