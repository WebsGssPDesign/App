---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-ppt-standard/references/editing-contract.md"
tags: [hecho]
---
# editing-contract.md

## Resumen
Este documento establece un protocolo para editar presentaciones existentes, definiendo criterios claros para decidir entre una reparación rápida ("Review") o una reestructuración compleja con múltiples agentes ("Orchestrator"). Su objetivo es limitar el alcance de los cambios, preservar la integridad del diseño y garantizar que solo se modifiquen los archivos afectados sin alterar datos no solicitados.

## Datos clave
- **Flujo de trabajo**: Lectura inicial (盘点) -> Determinación de complejidad -> Ejecución (Review u Orchestrator) -> Validación final.
- **Modo Review (Rápido)**: Para cambios menores como correcciones tipográficas, reemplazo de texto local o ajuste de imágenes sin alterar la narrativa ni el estilo global. Requiere ejecutar `deck.py prepare` y `render.py --batch`.
- **Modo Orchestrator (Complejo)**: Activado si hay cambios en la estructura, nuevos datos, activos visuales o modificaciones al sistema de estilos (`base.css`). Utiliza un gráfico de tareas paralelo y evita reescribir todo el proyecto.
- **Comandos críticos**: `deck.py prepare`, `render.py --batch`, `deck.py contact`.
- **Validación estricta**: Verificación de consistencia entre `speech.md`, `present.html` y los archivos PPTX; estado `partial` si la exportación falla sin falsificar rutas.

## Etiquetas
#edición-de-presentaciones #flujos-trabajo-agiles #control-de-cambios

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-ppt-standard\references\editing-contract.md`
