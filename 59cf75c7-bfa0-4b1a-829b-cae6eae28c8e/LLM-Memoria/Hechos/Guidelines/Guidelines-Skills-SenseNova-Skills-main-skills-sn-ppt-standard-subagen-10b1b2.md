---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-ppt-standard/subagents/review.md"
tags: [hecho]
---
# review.md

## Resumen
Este documento define el protocolo de operación para un agente "Review" encargado de auditar y corregir la calidad visual, factual y narrativa de una presentación técnica. Su función es garantizar que los entregables finales cumplan con estándares estrictos de fidelidad al contenido, diseño consistente y legibilidad antes de su exportación.

## Datos clave
- **Modos operativos**: `simple_edit` (correcciones locales) y `final_review` (auditoría completa).
- **Flujo crítico**: Listar problemas -> Modificar código/HTML -> Renderizar en lote -> Verificar nueva evidencia visual.
- **Comandos esenciales**:
  - Preparación: `python "$SKILL_ROOT/scripts/deck.py" prepare ...`
  - Renderizado: `python "$SKILL_ROOT/scripts/render.py" --batch ...`
  - Contacto/Enlace: `python "$SKILL_ROOT/scripts/deck.py" contact ...`
- **Reglas de bloqueo**: Retornar `blocked` solo ante errores de sistema, falta de datos o cambios narrativos mayores; ignorar preferencias estéticas menores.
- **Verificación de contenido**: Validación cruzada estricta entre tablas de datos, gráficos (ECharts) y el texto visible en pantalla.

## Etiquetas
#auditoría #calidad #renderizado #presentaciones

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-ppt-standard\subagents\review.md`
