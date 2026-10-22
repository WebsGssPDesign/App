---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/devops/kanban-orchestrator/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define el manual de juego para un perfil de orquestador en sistemas Kanban, centrado en la regla fundamental de "decomponer y enrutar" en lugar de ejecutar tareas directamente. Su propósito es guiar a los agentes para que identifiquen perfiles disponibles, creen tareas específicas y gestionen dependencias complejas mediante gráficos de trabajo antes de delegar el esfuerzo a especialistas reales.

## Datos clave
- **Regla principal:** Nunca ejecutar la tarea personalmente; siempre crear una tarjeta Kanban asignada.
- **Paso 0 obligatorio:** Descubrir perfiles configurados (`hermes profile list`) antes de planificar para evitar asignaciones fallidas silenciosas.
- **Criterios de creación:** Usar el tablero cuando se necesiten múltiples especialistas, persistencia ante fallos, intervención humana o auditoría (SQLite).
- **Gestión de dependencias:** Usar `parents=[...]` en la llamada `kanban_create`; nunca crear tarjetas independientes que deban esperar a otras.
- **Decomposición:** Extraer carriles de trabajo independientes del prompt del usuario y convertirlos en tarjetas paralelas antes de cualquier ejecución.

## Etiquetas
#devops #kanban #orquestacion #multi-agente

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\devops\kanban-orchestrator\SKILL.md`
