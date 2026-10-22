---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/software-development/simplify-code/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía define un flujo de trabajo automatizado para limpiar y simplificar cambios recientes en el código mediante tres revisores especializados que operan en paralelo. El sistema busca mejorar la reutilización, calidad y eficiencia sin alterar comportamientos existentes, priorizando la seguridad antes de aplicar cualquier modificación.

## Datos clave
- **Proyecto**: Skill `simplify-code` para revisión paralela de cambios.
- **Tecnologías**: Agentes delegados (`delegate_task`), herramientas de terminal y búsqueda (`git`, `grep`).
- **Decisiones**: Se ejecutan tres subagentes simultáneamente (reutilización, calidad, eficiencia) en lugar de uno general para reducir latencia.
- **Rutas/Comandos**:
  - Detección de cambios: `git diff` (por defecto), `git diff HEAD`, o variantes específicas como `--staged`.
  - Análisis crítico: Uso de `git blame` bajo el principio "Chesterton's Fence" antes de eliminar código.
- **Pasos importantes**: Clasificación de hallazgos en SAFE (auto-aplicar), CAREFUL (verificar con tests) o RISKY (revisión humana).

## Etiquetas
#refactor #automated-review #code-quality #parallel-agents

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\software-development\simplify-code\SKILL.md`
